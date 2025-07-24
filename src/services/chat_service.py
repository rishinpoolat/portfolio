import uuid
import time
import logging
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from src.services.rag_service import RAGService
from vector_database import PortfolioVectorDB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class ChatMessage:
    """Represents a single chat message."""
    role: str  # 'user' or 'assistant'
    content: str
    timestamp: float
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

@dataclass
class ChatSession:
    """Represents a chat session with conversation history."""
    session_id: str
    created_at: float
    last_activity: float
    messages: List[ChatMessage]
    context: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.context is None:
            self.context = {}

class ChatService:
    """Service for managing chat conversations and session state."""
    
    def __init__(self, vector_db: PortfolioVectorDB = None, rag_service: RAGService = None):
        self.vector_db = vector_db or PortfolioVectorDB()
        self.rag_service = rag_service or RAGService(self.vector_db)
        self.sessions: Dict[str, ChatSession] = {}
        self.session_timeout = 3600  # 1 hour in seconds
        
    def create_session(self) -> str:
        """Create a new chat session and return session ID."""
        session_id = str(uuid.uuid4())
        current_time = time.time()
        
        session = ChatSession(
            session_id=session_id,
            created_at=current_time,
            last_activity=current_time,
            messages=[],
            context={
                'topics_discussed': [],
                'technologies_mentioned': [],
                'categories_explored': []
            }
        )
        
        self.sessions[session_id] = session
        logger.info(f"Created new chat session: {session_id}")
        return session_id
    
    def get_session(self, session_id: str) -> Optional[ChatSession]:
        """Get a chat session by ID."""
        if session_id not in self.sessions:
            return None
        
        session = self.sessions[session_id]
        
        # Check if session has expired
        if time.time() - session.last_activity > self.session_timeout:
            logger.info(f"Session {session_id} expired, removing")
            del self.sessions[session_id]
            return None
        
        return session
    
    def add_message(self, session_id: str, role: str, content: str, metadata: Dict[str, Any] = None) -> bool:
        """Add a message to the chat session."""
        session = self.get_session(session_id)
        if not session:
            return False
        
        message = ChatMessage(
            role=role,
            content=content,
            timestamp=time.time(),
            metadata=metadata or {}
        )
        
        session.messages.append(message)
        session.last_activity = time.time()
        
        # Update session context based on message
        if role == 'user':
            self._update_session_context(session, content)
        
        return True
    
    def _update_session_context(self, session: ChatSession, user_message: str) -> None:
        """Update session context based on user message."""
        # Classify the query to extract topics and technologies
        classification = self.rag_service.classify_query_intent(user_message)
        
        # Update context with new information
        if classification['categories']:
            for category in classification['categories']:
                if category not in session.context['categories_explored']:
                    session.context['categories_explored'].append(category)
        
        if classification['technologies']:
            for tech in classification['technologies']:
                if tech not in session.context['technologies_mentioned']:
                    session.context['technologies_mentioned'].append(tech)
        
        # Simple topic extraction (could be enhanced)
        user_lower = user_message.lower()
        topic_keywords = ['project', 'education', 'experience', 'work', 'skill', 'certification']
        for keyword in topic_keywords:
            if keyword in user_lower and keyword not in session.context['topics_discussed']:
                session.context['topics_discussed'].append(keyword)
    
    async def process_message(self, message: str, session_id: Optional[str] = None) -> Dict[str, Any]:
        """Process a user message and generate a response."""
        start_time = time.time()
        
        # Create session if not provided
        if not session_id:
            session_id = self.create_session()
        
        session = self.get_session(session_id)
        if not session:
            # Create new session if the provided one doesn't exist or expired
            session_id = self.create_session()
            session = self.get_session(session_id)
        
        # Add user message to session
        self.add_message(session_id, 'user', message)
        
        try:
            # Prepare chat history for RAG service
            chat_history = []
            for msg in session.messages[-10:]:  # Last 10 messages
                chat_history.append({
                    'role': msg.role,
                    'content': msg.content
                })
            
            # Generate response using RAG service
            response_data = await self.rag_service.generate_response(
                query=message,
                chat_history=chat_history[:-1]  # Exclude the current user message
            )
            
            # Add assistant response to session
            self.add_message(
                session_id, 
                'assistant', 
                response_data['response'],
                metadata={
                    'sources': response_data['sources'],
                    'context_chunks': response_data['context_chunks'],
                    'query_classification': response_data['query_classification']
                }
            )
            
            response_time = time.time() - start_time
            
            return {
                'response': response_data['response'],
                'sources': response_data['sources'],
                'suggested_questions': response_data['follow_up_questions'],
                'session_id': session_id,
                'response_time': response_time,
                'session_context': session.context,
                'query_classification': response_data['query_classification']
            }
            
        except Exception as e:
            logger.error(f"Error processing message: {e}")
            error_response = "I apologize, but I encountered an error while processing your question. Please try again."
            
            # Add error response to session
            self.add_message(session_id, 'assistant', error_response)
            
            return {
                'response': error_response,
                'sources': [],
                'suggested_questions': [],
                'session_id': session_id,
                'response_time': time.time() - start_time,
                'session_context': session.context,
                'query_classification': {},
                'error': str(e)
            }
    
    def get_session_history(self, session_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """Get chat history for a session."""
        session = self.get_session(session_id)
        if not session:
            return []
        
        messages = session.messages[-limit:] if limit else session.messages
        return [
            {
                'role': msg.role,
                'content': msg.content,
                'timestamp': msg.timestamp,
                'datetime': datetime.fromtimestamp(msg.timestamp).isoformat(),
                'metadata': msg.metadata
            }
            for msg in messages
        ]
    
    def get_session_stats(self, session_id: str) -> Dict[str, Any]:
        """Get statistics for a chat session."""
        session = self.get_session(session_id)
        if not session:
            return {}
        
        user_messages = [msg for msg in session.messages if msg.role == 'user']
        assistant_messages = [msg for msg in session.messages if msg.role == 'assistant']
        
        duration = session.last_activity - session.created_at
        
        return {
            'session_id': session_id,
            'created_at': datetime.fromtimestamp(session.created_at).isoformat(),
            'last_activity': datetime.fromtimestamp(session.last_activity).isoformat(),
            'duration_seconds': duration,
            'total_messages': len(session.messages),
            'user_messages': len(user_messages),
            'assistant_messages': len(assistant_messages),
            'context': session.context
        }
    
    def cleanup_expired_sessions(self) -> int:
        """Remove expired sessions and return count of removed sessions."""
        current_time = time.time()
        expired_sessions = []
        
        for session_id, session in self.sessions.items():
            if current_time - session.last_activity > self.session_timeout:
                expired_sessions.append(session_id)
        
        for session_id in expired_sessions:
            del self.sessions[session_id]
            logger.info(f"Removed expired session: {session_id}")
        
        return len(expired_sessions)
    
    def get_all_sessions_stats(self) -> Dict[str, Any]:
        """Get statistics for all active sessions."""
        current_time = time.time()
        
        # Clean up expired sessions first
        self.cleanup_expired_sessions()
        
        total_messages = sum(len(session.messages) for session in self.sessions.values())
        
        categories_stats = {}
        technologies_stats = {}
        
        for session in self.sessions.values():
            for category in session.context.get('categories_explored', []):
                categories_stats[category] = categories_stats.get(category, 0) + 1
            
            for tech in session.context.get('technologies_mentioned', []):
                technologies_stats[tech] = technologies_stats.get(tech, 0) + 1
        
        return {
            'active_sessions': len(self.sessions),
            'total_messages': total_messages,
            'most_discussed_categories': sorted(categories_stats.items(), key=lambda x: x[1], reverse=True)[:5],
            'most_mentioned_technologies': sorted(technologies_stats.items(), key=lambda x: x[1], reverse=True)[:10],
            'session_timeout_hours': self.session_timeout / 3600
        }
    
    def search_conversations(self, query: str, session_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Search through conversation history."""
        results = []
        
        sessions_to_search = [self.sessions[session_id]] if session_id and session_id in self.sessions else self.sessions.values()
        
        for session in sessions_to_search:
            for message in session.messages:
                if query.lower() in message.content.lower():
                    results.append({
                        'session_id': session.session_id,
                        'message': {
                            'role': message.role,
                            'content': message.content,
                            'timestamp': message.timestamp,
                            'datetime': datetime.fromtimestamp(message.timestamp).isoformat()
                        }
                    })
        
        return results[:50]  # Limit results
    
    def export_session(self, session_id: str) -> Optional[Dict[str, Any]]:
        """Export a complete session for analysis or backup."""
        session = self.get_session(session_id)
        if not session:
            return None
        
        return {
            'session_id': session.session_id,
            'created_at': datetime.fromtimestamp(session.created_at).isoformat(),
            'last_activity': datetime.fromtimestamp(session.last_activity).isoformat(),
            'context': session.context,
            'messages': [
                {
                    'role': msg.role,
                    'content': msg.content,
                    'timestamp': msg.timestamp,
                    'datetime': datetime.fromtimestamp(msg.timestamp).isoformat(),
                    'metadata': msg.metadata
                }
                for msg in session.messages
            ]
        }