import pytest
import asyncio
from unittest.mock import Mock, patch, AsyncMock
from src.services.rag_service import RAGService
from vector_database import PortfolioVectorDB
from config import settings

class TestRAGService:
    """Test cases for RAG service functionality."""
    
    @pytest.fixture
    def mock_vector_db(self):
        """Create a mock vector database."""
        mock_db = Mock(spec=PortfolioVectorDB)
        mock_db.search_similar.return_value = [
            {
                'id': 'projects_sample_0',
                'document': 'Sample Node.js project with Express and MongoDB',
                'metadata': {
                    'filename': 'sample_project.md',
                    'category': 'projects',
                    'technologies': ['nodejs', 'express', 'mongodb']
                },
                'relevance_score': 0.95
            }
        ]
        return mock_db
    
    @pytest.fixture
    def mock_groq_client(self):
        """Create a mock Groq client."""
        mock_client = Mock()
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "This is a sample response about Node.js projects."
        
        mock_client.chat.completions.create.return_value = mock_response
        return mock_client
    
    @pytest.fixture
    def rag_service(self, mock_vector_db):
        """Create a RAG service with mocked dependencies."""
        with patch('src.services.rag_service.Groq') as mock_groq_class:
            mock_groq_instance = Mock()
            mock_groq_class.return_value = mock_groq_instance
            
            service = RAGService(vector_db=mock_vector_db)
            service.groq_client = mock_groq_instance
            return service
    
    def test_classify_query_intent(self, rag_service):
        """Test query intent classification."""
        # Test technology-specific query
        result = rag_service.classify_query_intent("Tell me about nodejs projects")
        
        assert 'categories' in result
        assert 'technologies' in result
        assert 'intent_type' in result
        assert result['intent_type'] == 'technology_specific'
        assert 'nodejs' in result['technologies']
        assert 'projects' in result['categories']
    
    def test_classify_query_categories(self, rag_service):
        """Test category classification."""
        test_cases = [
            ("What is his educational background?", ['education']),
            ("Tell me about his work experience", ['experience']),
            ("Show me his certifications", ['certification']),
            ("What hackathons has he participated in?", ['hackathon'])
        ]
        
        for query, expected_categories in test_cases:
            result = rag_service.classify_query_intent(query)
            for category in expected_categories:
                assert category in result['categories']
    
    def test_get_relevant_context(self, rag_service, mock_vector_db):
        """Test context retrieval from vector database."""
        query = "nodejs projects"
        context = rag_service.get_relevant_context(query, max_chunks=3)
        
        assert isinstance(context, list)
        assert len(context) <= 3
        
        # Verify vector DB was called
        assert mock_vector_db.search_similar.called
    
    def test_format_context(self, rag_service):
        """Test context formatting for LLM prompt."""
        context_chunks = [
            {
                'id': 'test_1',
                'document': 'Sample document content',
                'metadata': {'filename': 'test.md', 'category': 'projects'},
                'relevance_score': 0.9
            }
        ]
        
        formatted = rag_service._format_context(context_chunks)
        
        assert 'Source 1' in formatted
        assert 'test.md' in formatted
        assert 'projects' in formatted
        assert 'Sample document content' in formatted
        assert '0.900' in formatted
    
    @pytest.mark.asyncio
    async def test_generate_response(self, rag_service):
        """Test response generation with mocked Groq API."""
        # Mock the Groq client response
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = "Test response about Node.js projects"
        
        rag_service.groq_client.chat.completions.create.return_value = mock_response
        
        # Mock follow-up questions generation
        with patch.object(rag_service, '_generate_follow_up_questions', return_value=['Follow up 1?', 'Follow up 2?']):
            result = await rag_service.generate_response("Tell me about nodejs projects")
        
        assert 'response' in result
        assert 'sources' in result
        assert 'follow_up_questions' in result
        assert 'query_classification' in result
        assert result['response'] == "Test response about Node.js projects"
    
    def test_extract_sources(self, rag_service):
        """Test source extraction from context chunks."""
        context_chunks = [
            {
                'metadata': {
                    'filename': 'project1.md',
                    'category': 'projects',
                    'file_path': '/path/to/project1.md',
                    'chunk_id': 'project1_0',
                    'technologies': ['nodejs', 'react']
                },
                'relevance_score': 0.95
            }
        ]
        
        sources = rag_service._extract_sources(context_chunks)
        
        assert len(sources) == 1
        assert sources[0]['filename'] == 'project1.md'
        assert sources[0]['category'] == 'projects'
        assert sources[0]['relevance_score'] == 0.95
        assert 'nodejs' in sources[0]['technologies']
    
    @pytest.mark.asyncio
    async def test_generate_follow_up_questions(self, rag_service):
        """Test follow-up question generation."""
        # Mock Groq response for follow-up questions
        mock_response = Mock()
        mock_response.choices = [Mock()]
        mock_response.choices[0].message.content = """1. What technologies did he use in these projects?
2. How long did these projects take to complete?
3. What was the most challenging aspect of development?"""
        
        rag_service.groq_client.chat.completions.create.return_value = mock_response
        
        questions = await rag_service._generate_follow_up_questions(
            "Tell me about projects", 
            "Response about projects", 
            "Context about projects"
        )
        
        assert len(questions) <= 3
        assert all(q.endswith('?') for q in questions)
        assert 'technologies' in questions[0].lower()
    
    def test_get_conversation_summary(self, rag_service):
        """Test conversation summary generation."""
        chat_history = [
            {'role': 'user', 'content': 'Tell me about nodejs projects'},
            {'role': 'assistant', 'content': 'Here are his Node.js projects...'},
            {'role': 'user', 'content': 'What about his education?'}
        ]
        
        summary = rag_service.get_conversation_summary(chat_history)
        
        assert isinstance(summary, str)
        assert len(summary) > 0
        
        # Should mention relevant categories
        summary_lower = summary.lower()
        assert 'projects' in summary_lower or 'education' in summary_lower
    
    @pytest.mark.asyncio
    async def test_error_handling(self, rag_service):
        """Test error handling in response generation."""
        # Mock Groq client to raise an exception
        rag_service.groq_client.chat.completions.create.side_effect = Exception("API Error")
        
        result = await rag_service.generate_response("test query")
        
        assert 'error' not in result or result.get('response', '').startswith('I apologize')
        assert 'sources' in result
        assert isinstance(result['sources'], list)

if __name__ == "__main__":
    pytest.main([__file__, "-v"])