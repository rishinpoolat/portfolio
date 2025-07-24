import re
import logging
from typing import List, Dict, Any, Optional, Tuple
from groq import Groq
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.prompts import PromptTemplate
from vector_database import PortfolioVectorDB
from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RAGService:
    """RAG (Retrieval-Augmented Generation) service for portfolio chatbot."""
    
    def __init__(self, vector_db: PortfolioVectorDB = None):
        self.vector_db = vector_db or PortfolioVectorDB()
        self.groq_client = Groq(api_key=settings.GROQ_API_KEY)
        self.model_name = settings.GROQ_MODEL
        self._initialize_prompts()
    
    def _initialize_prompts(self) -> None:
        """Initialize prompt templates for different types of queries."""
        
        self.system_prompt = """You are an intelligent assistant that helps people learn about Mohammed Rishin's professional portfolio. 
You have access to detailed information about his projects, education, work experience, certifications, and hackathon participation.

Guidelines:
- Provide accurate, helpful responses based on the provided context
- If information isn't available in the context, say so clearly
- Focus on technical details when discussing projects and experience
- Maintain a professional but conversational tone
- Always cite sources when possible
- For technology-specific queries, filter and highlight relevant technologies

Context: {context}

Question: {question}

Please provide a comprehensive answer based on the context above."""
        
        self.query_prompt = PromptTemplate(
            input_variables=["context", "question"],
            template=self.system_prompt
        )
        
        self.follow_up_prompt = """Based on the conversation about Mohammed Rishin's portfolio, suggest 3 relevant follow-up questions that would help the user learn more about his background, projects, or experience.

Context: {context}
User Question: {question}
Assistant Response: {response}

Generate exactly 3 follow-up questions that are:
1. Specific and actionable
2. Related to the current topic
3. Help explore different aspects of his portfolio

Follow-up questions:"""

    def classify_query_intent(self, query: str) -> Dict[str, Any]:
        """Classify the query intent and extract relevant information."""
        query_lower = query.lower()
        
        # Initialize classification result
        classification = {
            'categories': [],
            'technologies': [],
            'intent_type': 'general',
            'confidence': 0.0
        }
        
        # Category classification
        category_scores = {}
        for category, patterns in settings.CATEGORY_PATTERNS.items():
            score = sum(1 for pattern in patterns if pattern in query_lower)
            if score > 0:
                category_scores[category] = score / len(patterns)
        
        # Sort categories by relevance
        if category_scores:
            sorted_categories = sorted(category_scores.items(), key=lambda x: x[1], reverse=True)
            classification['categories'] = [cat for cat, score in sorted_categories if score > 0.1]
            classification['confidence'] = sorted_categories[0][1]
        
        # Technology extraction
        all_tech_patterns = []
        for patterns in settings.CATEGORY_PATTERNS.values():
            all_tech_patterns.extend(patterns)
        
        tech_patterns = [
            'node.js', 'nodejs', 'react', 'python', 'typescript', 'javascript',
            'fastapi', 'django', 'flask', 'mongodb', 'postgresql', 'mysql',
            'docker', 'kubernetes', 'aws', 'gcp', 'azure', 'tensorflow',
            'pytorch', 'opencv', 'scikit-learn', 'pandas', 'numpy',
            'express', 'vue', 'angular', 'next.js', 'nuxt', 'svelte'
        ]
        
        found_technologies = [tech for tech in tech_patterns if tech in query_lower]
        classification['technologies'] = found_technologies
        
        # Intent type classification
        if any(word in query_lower for word in ['tell me about', 'what is', 'describe', 'explain']):
            classification['intent_type'] = 'descriptive'
        elif any(word in query_lower for word in ['how', 'why', 'when', 'where']):
            classification['intent_type'] = 'analytical'
        elif any(word in query_lower for word in ['list', 'show me', 'what are']):
            classification['intent_type'] = 'listing'
        elif found_technologies:
            classification['intent_type'] = 'technology_specific'
        
        return classification

    def get_relevant_context(self, query: str, max_chunks: int = 5) -> List[Dict[str, Any]]:
        """Retrieve relevant context from the vector database."""
        try:
            # Classify the query to determine search strategy
            classification = self.classify_query_intent(query)
            
            results = []
            
            # If specific categories are identified, search those first
            if classification['categories']:
                for category in classification['categories'][:2]:  # Limit to top 2 categories
                    category_results = self.vector_db.search_similar(
                        query=query,
                        category=category,
                        n_results=max_chunks // 2,
                        technologies=classification['technologies']
                    )
                    results.extend(category_results)
            
            # Always include unified search for comprehensive results
            unified_results = self.vector_db.search_similar(
                query=query,
                category=None,  # Use unified collection
                n_results=max_chunks,
                technologies=classification['technologies']
            )
            results.extend(unified_results)
            
            # Remove duplicates and sort by relevance
            seen_ids = set()
            unique_results = []
            for result in results:
                if result['id'] not in seen_ids:
                    unique_results.append(result)
                    seen_ids.add(result['id'])
            
            # Sort by relevance score and limit results
            unique_results.sort(key=lambda x: x['relevance_score'], reverse=True)
            return unique_results[:max_chunks]
            
        except Exception as e:
            logger.error(f"Error retrieving context: {e}")
            return []

    def _format_context(self, context_chunks: List[Dict[str, Any]]) -> str:
        """Format retrieved context for the LLM prompt."""
        if not context_chunks:
            return "No relevant context found."
        
        formatted_context = []
        for i, chunk in enumerate(context_chunks, 1):
            metadata = chunk['metadata']
            document = chunk['document']
            score = chunk['relevance_score']
            
            context_entry = f"""[Source {i}: {metadata.get('filename', 'Unknown')} - {metadata.get('category', 'Unknown')} (Relevance: {score:.3f})]
{document}"""
            formatted_context.append(context_entry)
        
        return "\n\n".join(formatted_context)

    async def generate_response(self, query: str, context_chunks: List[Dict[str, Any]] = None, 
                               chat_history: List[Dict[str, str]] = None) -> Dict[str, Any]:
        """Generate a response using Groq LLM with retrieved context."""
        try:
            # Get context if not provided
            if context_chunks is None:
                context_chunks = self.get_relevant_context(query, max_chunks=settings.RETRIEVAL_K)
            
            # Format context for the prompt
            formatted_context = self._format_context(context_chunks)
            
            # Prepare the prompt
            prompt = self.query_prompt.format(context=formatted_context, question=query)
            
            # Add chat history if available
            messages = []
            if chat_history:
                for msg in chat_history[-6:]:  # Limit to last 6 messages
                    messages.append({"role": msg["role"], "content": msg["content"]})
            
            messages.append({"role": "user", "content": prompt})
            
            # Generate response using Groq
            completion = self.groq_client.chat.completions.create(
                model=self.model_name,
                messages=messages,
                temperature=0.3,
                max_tokens=1024,
                top_p=0.9,
                stream=False
            )
            
            response_text = completion.choices[0].message.content
            
            # Generate follow-up questions
            follow_up_questions = await self._generate_follow_up_questions(
                query, response_text, formatted_context
            )
            
            # Extract sources
            sources = self._extract_sources(context_chunks)
            
            return {
                'response': response_text,
                'sources': sources,
                'context_chunks': len(context_chunks),
                'follow_up_questions': follow_up_questions,
                'query_classification': self.classify_query_intent(query)
            }
            
        except Exception as e:
            logger.error(f"Error generating response: {e}")
            return {
                'response': "I apologize, but I encountered an error while processing your question. Please try again.",
                'sources': [],
                'context_chunks': 0,
                'follow_up_questions': [],
                'query_classification': {}
            }

    async def _generate_follow_up_questions(self, query: str, response: str, context: str) -> List[str]:
        """Generate relevant follow-up questions."""
        try:
            prompt = self.follow_up_prompt.format(
                context=context[:1000],  # Limit context length
                question=query,
                response=response[:500]   # Limit response length
            )
            
            completion = self.groq_client.chat.completions.create(
                model=self.model_name,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.5,
                max_tokens=300,
                top_p=0.8
            )
            
            follow_up_text = completion.choices[0].message.content
            
            # Extract questions from the response
            questions = []
            lines = follow_up_text.strip().split('\n')
            for line in lines:
                line = line.strip()
                if line and (line.startswith('1.') or line.startswith('2.') or line.startswith('3.') or 
                           line.startswith('-') or line.endswith('?')):
                    # Clean up the question
                    question = re.sub(r'^[0-9]+\.\s*|\-\s*', '', line).strip()
                    if question and question.endswith('?'):
                        questions.append(question)
            
            return questions[:3]  # Limit to 3 questions
            
        except Exception as e:
            logger.error(f"Error generating follow-up questions: {e}")
            return []

    def _extract_sources(self, context_chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Extract source information from context chunks."""
        sources = []
        for chunk in context_chunks:
            metadata = chunk['metadata']
            sources.append({
                'filename': metadata.get('filename', 'Unknown'),
                'category': metadata.get('category', 'Unknown'),
                'relevance_score': chunk['relevance_score'],
                'file_path': metadata.get('file_path', ''),
                'chunk_id': metadata.get('chunk_id', ''),
                'technologies': metadata.get('technologies', [])
            })
        return sources

    def get_conversation_summary(self, chat_history: List[Dict[str, str]]) -> str:
        """Generate a summary of the conversation for context."""
        if not chat_history:
            return ""
        
        # Extract key topics and themes from chat history
        messages = [msg['content'] for msg in chat_history[-10:]]  # Last 10 messages
        conversation_text = " ".join(messages)
        
        # Simple keyword extraction (could be enhanced with more sophisticated NLP)
        keywords = []
        for category, patterns in settings.CATEGORY_PATTERNS.items():
            if any(pattern in conversation_text.lower() for pattern in patterns):
                keywords.append(category)
        
        if keywords:
            return f"Conversation context: Discussion about {', '.join(keywords)}"
        return "General conversation about Mohammed Rishin's portfolio"