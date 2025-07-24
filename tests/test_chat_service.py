import pytest
import time
from unittest.mock import Mock, AsyncMock, patch
from src.services.chat_service import ChatService, ChatMessage, ChatSession
from src.services.rag_service import RAGService
from vector_database import PortfolioVectorDB

class TestChatService:
    """Test cases for chat service functionality."""
    
    @pytest.fixture
    def mock_rag_service(self):
        """Create a mock RAG service."""
        mock_rag = Mock(spec=RAGService)
        mock_rag.classify_query_intent.return_value = {
            'categories': ['projects'],
            'technologies': ['nodejs'],
            'intent_type': 'technology_specific',
            'confidence': 0.8
        }
        mock_rag.generate_response = AsyncMock(return_value={
            'response': 'Test response about Node.js projects',
            'sources': [{'filename': 'test.md', 'category': 'projects'}],
            'follow_up_questions': ['What else would you like to know?'],
            'context_chunks': 2,
            'query_classification': {'categories': ['projects']}
        })
        return mock_rag
    
    @pytest.fixture
    def chat_service(self, mock_rag_service):
        """Create a chat service with mocked dependencies."""
        with patch('src.services.chat_service.PortfolioVectorDB'):
            service = ChatService()
            service.rag_service = mock_rag_service
            return service
    
    def test_create_session(self, chat_service):
        """Test session creation."""
        session_id = chat_service.create_session()
        
        assert isinstance(session_id, str)
        assert len(session_id) > 0
        assert session_id in chat_service.sessions
        
        session = chat_service.sessions[session_id]
        assert session.session_id == session_id
        assert len(session.messages) == 0
        assert 'topics_discussed' in session.context
    
    def test_get_session(self, chat_service):
        """Test session retrieval."""
        session_id = chat_service.create_session()
        
        # Test valid session
        session = chat_service.get_session(session_id)
        assert session is not None
        assert session.session_id == session_id
        
        # Test invalid session
        invalid_session = chat_service.get_session("invalid-id")
        assert invalid_session is None
    
    def test_add_message(self, chat_service):
        """Test adding messages to a session."""
        session_id = chat_service.create_session()
        
        # Add user message
        success = chat_service.add_message(session_id, 'user', 'Hello, tell me about projects')
        assert success is True
        
        session = chat_service.get_session(session_id)
        assert len(session.messages) == 1
        assert session.messages[0].role == 'user'
        assert session.messages[0].content == 'Hello, tell me about projects'
        
        # Add assistant message
        chat_service.add_message(session_id, 'assistant', 'Here are the projects...')
        assert len(session.messages) == 2
    
    def test_session_context_update(self, chat_service):
        """Test session context updates based on user messages."""
        session_id = chat_service.create_session()
        
        # Add message about Node.js projects
        chat_service.add_message(session_id, 'user', 'Tell me about nodejs projects')
        
        session = chat_service.get_session(session_id)
        
        # Check that context was updated
        assert 'projects' in session.context['categories_explored']
        assert 'nodejs' in session.context['technologies_mentioned']
    
    @pytest.mark.asyncio
    async def test_process_message(self, chat_service, mock_rag_service):
        """Test message processing and response generation."""
        result = await chat_service.process_message("Tell me about nodejs projects")
        
        assert 'response' in result
        assert 'session_id' in result
        assert 'sources' in result
        assert 'suggested_questions' in result
        assert 'response_time' in result
        
        # Verify RAG service was called
        mock_rag_service.generate_response.assert_called_once()
        
        # Check that session was created and message was added
        session_id = result['session_id']
        session = chat_service.get_session(session_id)
        assert len(session.messages) == 2  # User message + assistant response
    
    @pytest.mark.asyncio
    async def test_process_message_with_existing_session(self, chat_service):
        """Test processing message with an existing session."""
        # Create session and add initial message
        session_id = chat_service.create_session()
        chat_service.add_message(session_id, 'user', 'First message')
        chat_service.add_message(session_id, 'assistant', 'First response')
        
        # Process new message with existing session
        result = await chat_service.process_message("Second message", session_id)
        
        assert result['session_id'] == session_id
        
        # Check that session now has 4 messages (2 old + 2 new)
        session = chat_service.get_session(session_id)
        assert len(session.messages) == 4
    
    def test_get_session_history(self, chat_service):
        """Test retrieving session history."""
        session_id = chat_service.create_session()
        
        # Add some messages
        chat_service.add_message(session_id, 'user', 'Message 1')
        chat_service.add_message(session_id, 'assistant', 'Response 1')
        chat_service.add_message(session_id, 'user', 'Message 2')
        
        history = chat_service.get_session_history(session_id)
        
        assert len(history) == 3
        assert history[0]['role'] == 'user'
        assert history[0]['content'] == 'Message 1'
        assert 'timestamp' in history[0]
        assert 'datetime' in history[0]
    
    def test_get_session_stats(self, chat_service):
        """Test session statistics."""
        session_id = chat_service.create_session()
        
        # Add messages
        chat_service.add_message(session_id, 'user', 'User message 1')
        chat_service.add_message(session_id, 'assistant', 'Assistant response 1')
        chat_service.add_message(session_id, 'user', 'User message 2')
        
        stats = chat_service.get_session_stats(session_id)
        
        assert stats['session_id'] == session_id
        assert stats['total_messages'] == 3
        assert stats['user_messages'] == 2
        assert stats['assistant_messages'] == 1
        assert 'created_at' in stats
        assert 'duration_seconds' in stats
        assert 'context' in stats
    
    def test_session_expiry(self, chat_service):
        """Test session expiry functionality."""
        # Create session with short timeout
        chat_service.session_timeout = 1  # 1 second
        session_id = chat_service.create_session()
        
        # Verify session exists
        assert chat_service.get_session(session_id) is not None
        
        # Wait for session to expire
        time.sleep(1.1)
        
        # Session should now be expired
        assert chat_service.get_session(session_id) is None
    
    def test_cleanup_expired_sessions(self, chat_service):
        """Test cleanup of expired sessions."""
        # Create multiple sessions with short timeout
        chat_service.session_timeout = 0.5  # 0.5 seconds
        
        session_ids = []
        for i in range(3):
            session_id = chat_service.create_session()
            session_ids.append(session_id)
        
        # Wait for sessions to expire
        time.sleep(0.6)
        
        # Cleanup expired sessions
        removed_count = chat_service.cleanup_expired_sessions()
        
        assert removed_count == 3
        assert len(chat_service.sessions) == 0
    
    def test_get_all_sessions_stats(self, chat_service):
        """Test getting statistics for all sessions."""
        # Create multiple sessions with messages
        for i in range(2):
            session_id = chat_service.create_session()
            chat_service.add_message(session_id, 'user', f'nodejs project question {i}')
        
        stats = chat_service.get_all_sessions_stats()
        
        assert 'active_sessions' in stats
        assert 'total_messages' in stats
        assert 'most_discussed_categories' in stats
        assert 'most_mentioned_technologies' in stats
        assert stats['active_sessions'] == 2
        assert stats['total_messages'] == 2
    
    def test_search_conversations(self, chat_service):
        """Test searching through conversation history."""
        session_id = chat_service.create_session()
        
        # Add messages with searchable content
        chat_service.add_message(session_id, 'user', 'Tell me about nodejs projects')
        chat_service.add_message(session_id, 'assistant', 'Here are his Node.js projects...')
        chat_service.add_message(session_id, 'user', 'What about Python projects?')
        
        # Search for nodejs
        results = chat_service.search_conversations('nodejs')
        
        assert len(results) >= 1
        assert any('nodejs' in result['message']['content'].lower() for result in results)
    
    def test_export_session(self, chat_service):
        """Test session export functionality."""
        session_id = chat_service.create_session()
        
        # Add some messages
        chat_service.add_message(session_id, 'user', 'Test message')
        chat_service.add_message(session_id, 'assistant', 'Test response')
        
        exported = chat_service.export_session(session_id)
        
        assert exported is not None
        assert exported['session_id'] == session_id
        assert 'created_at' in exported
        assert 'messages' in exported
        assert len(exported['messages']) == 2
        assert 'context' in exported
    
    @pytest.mark.asyncio
    async def test_error_handling_in_process_message(self, chat_service, mock_rag_service):
        """Test error handling during message processing."""
        # Make RAG service raise an exception
        mock_rag_service.generate_response.side_effect = Exception("RAG service error")
        
        result = await chat_service.process_message("Test message")
        
        assert 'error' in result or result['response'].startswith('I apologize')
        assert 'session_id' in result
        assert 'response_time' in result

if __name__ == "__main__":
    pytest.main([__file__, "-v"])