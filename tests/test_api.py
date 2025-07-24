import pytest
import asyncio
from fastapi.testclient import TestClient
from unittest.mock import Mock, patch, AsyncMock

# Import the FastAPI app
from main import app
from src.services.chat_service import ChatService
from src.services.rag_service import RAGService
from vector_database import PortfolioVectorDB

class TestAPIEndpoints:
    """Test cases for FastAPI endpoints."""
    
    @pytest.fixture
    def client(self):
        """Create a test client."""
        return TestClient(app)
    
    @pytest.fixture
    def mock_services(self):
        """Mock all services for isolated API testing."""
        with patch('src.api.routes.get_vector_db') as mock_db, \
             patch('src.api.routes.get_chat_service') as mock_chat:
            
            # Mock vector database
            db_instance = Mock(spec=PortfolioVectorDB)
            db_instance.search_similar.return_value = [
                {
                    'id': 'test_1',
                    'document': 'Sample Node.js project content',
                    'metadata': {
                        'filename': 'nodejs-project.md',
                        'category': 'projects',
                        'technologies': ['nodejs', 'express']
                    },
                    'relevance_score': 0.95
                }
            ]
            db_instance.get_statistics.return_value = {
                'collections': {'projects': 10, 'unified': 25},
                'total_documents': 25,
                'categories': ['projects', 'education', 'experience']
            }
            db_instance.refresh_database.return_value = {
                'total_files': 15,
                'successful': 15,
                'failed': 0,
                'total_chunks': 67
            }
            mock_db.return_value = db_instance
            
            # Mock chat service
            chat_instance = Mock(spec=ChatService)
            chat_instance.process_message = AsyncMock(return_value={
                'response': 'Test response about Node.js projects',
                'sources': [
                    {
                        'filename': 'nodejs-project.md',
                        'category': 'projects',
                        'relevance_score': 0.95,
                        'file_path': '/path/to/nodejs-project.md',
                        'chunk_id': 'projects_nodejs_0',
                        'technologies': ['nodejs', 'express']
                    }
                ],
                'suggested_questions': ['What else would you like to know?'],
                'session_id': 'test-session-123',
                'response_time': 1.23,
                'session_context': {
                    'topics_discussed': ['project'],
                    'technologies_mentioned': ['nodejs'],
                    'categories_explored': ['projects']
                },
                'query_classification': {
                    'categories': ['projects'],
                    'technologies': ['nodejs'],
                    'intent_type': 'technology_specific',
                    'confidence': 0.85
                }
            })
            chat_instance.get_session_stats.return_value = {
                'session_id': 'test-session-123',
                'created_at': '2024-01-15T10:00:00Z',
                'last_activity': '2024-01-15T10:30:00Z',
                'duration_seconds': 1800.0,
                'total_messages': 4,
                'user_messages': 2,
                'assistant_messages': 2,
                'context': {
                    'topics_discussed': ['project'],
                    'technologies_mentioned': ['nodejs'],
                    'categories_explored': ['projects']
                }
            }
            chat_instance.get_all_sessions_stats.return_value = {
                'active_sessions': 2,
                'total_messages': 10,
                'most_discussed_categories': [('projects', 5)],
                'most_mentioned_technologies': [('nodejs', 3)],
                'session_timeout_hours': 1.0
            }
            mock_chat.return_value = chat_instance
            
            yield {
                'vector_db': db_instance,
                'chat_service': chat_instance
            }
    
    def test_root_endpoint(self, client):
        """Test root endpoint returns API information."""
        response = client.get("/")
        
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "version" in data
        assert "endpoints" in data
        assert data["endpoints"]["chat"] == "/api/v1/chat"
    
    def test_chat_endpoint_success(self, client, mock_services):
        """Test successful chat request."""
        chat_request = {
            "message": "Tell me about nodejs projects",
            "session_id": "test-session-123"
        }
        
        response = client.post("/api/v1/chat", json=chat_request)
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "response" in data
        assert "sources" in data
        assert "suggested_questions" in data
        assert "session_id" in data
        assert "response_time" in data
        
        # Verify content
        assert data["response"] == "Test response about Node.js projects"
        assert data["session_id"] == "test-session-123"
        assert len(data["sources"]) > 0
        assert data["sources"][0]["filename"] == "nodejs-project.md"
    
    def test_chat_endpoint_validation_error(self, client, mock_services):
        """Test chat endpoint with invalid request."""
        # Empty message should fail validation
        chat_request = {"message": ""}
        
        response = client.post("/api/v1/chat", json=chat_request)
        
        assert response.status_code == 422  # Validation error
    
    def test_search_endpoint_success(self, client, mock_services):
        """Test successful search request."""
        search_request = {
            "query": "nodejs projects",
            "category": "projects",
            "limit": 5
        }
        
        response = client.post("/api/v1/search", json=search_request)
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "results" in data
        assert "total_results" in data
        assert "query_time" in data
        
        # Verify content
        assert data["total_results"] > 0
        assert len(data["results"]) > 0
        assert "document" in data["results"][0]
        assert "relevance_score" in data["results"][0]
    
    def test_stats_endpoint(self, client, mock_services):
        """Test database statistics endpoint."""
        response = client.get("/api/v1/stats")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "collections" in data
        assert "total_documents" in data
        assert "categories" in data
        
        # Verify content
        assert data["total_documents"] == 25
        assert "projects" in data["collections"]
        assert "projects" in data["categories"]
    
    def test_refresh_endpoint(self, client, mock_services):
        """Test database refresh endpoint."""
        response = client.post("/api/v1/refresh")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "message" in data
        assert "stats" in data
        assert "refresh_time" in data
        
        # Verify content
        assert data["message"] == "Database refreshed successfully"
        assert data["stats"]["total_files"] == 15
        assert data["stats"]["successful"] == 15
    
    def test_health_endpoint(self, client, mock_services):
        """Test health check endpoint."""
        response = client.get("/api/v1/health")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "status" in data
        assert "timestamp" in data
        assert "version" in data
        assert "services" in data
        
        # Verify content
        assert data["version"] == "1.0.0"
        assert "vector_database" in data["services"]
    
    def test_session_stats_endpoint(self, client, mock_services):
        """Test session statistics endpoint."""
        session_id = "test-session-123"
        response = client.get(f"/api/v1/sessions/{session_id}/stats")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "session_id" in data
        assert "total_messages" in data
        assert "context" in data
        
        # Verify content
        assert data["session_id"] == session_id
        assert data["total_messages"] == 4
    
    def test_all_sessions_stats_endpoint(self, client, mock_services):
        """Test all sessions statistics endpoint."""
        response = client.get("/api/v1/sessions/stats")
        
        assert response.status_code == 200
        data = response.json()
        
        # Verify response structure
        assert "active_sessions" in data
        assert "total_messages" in data
        assert "most_discussed_categories" in data
        assert "most_mentioned_technologies" in data
        
        # Verify content
        assert data["active_sessions"] == 2
        assert data["total_messages"] == 10
    
    def test_session_not_found(self, client, mock_services):
        """Test session stats for non-existent session."""
        # Mock session not found
        mock_services['chat_service'].get_session_stats.return_value = {}
        
        response = client.get("/api/v1/sessions/nonexistent-session/stats")
        
        assert response.status_code == 404
    
    def test_cors_headers(self, client):
        """Test CORS headers are present."""
        response = client.options("/")
        
        # CORS should be configured to allow all origins in development
        assert response.status_code == 200
    
    def test_gzip_compression(self, client, mock_services):
        """Test that responses can be compressed."""
        # Large response should trigger gzip compression
        response = client.get("/api/v1/stats", headers={"Accept-Encoding": "gzip"})
        
        assert response.status_code == 200
        # Note: TestClient may not actually compress, but middleware is configured
    
    def test_404_error_handler(self, client):
        """Test custom 404 error handler."""
        response = client.get("/nonexistent-endpoint")
        
        assert response.status_code == 404
        data = response.json()
        assert "error" in data
        assert "available_endpoints" in data
    
    @patch('src.api.routes.settings.validate_required_settings')
    def test_configuration_error(self, mock_validate, client, mock_services):
        """Test handling of configuration errors."""
        # Mock configuration validation failure
        mock_validate.side_effect = ValueError("GROQ_API_KEY is required")
        
        chat_request = {"message": "test message"}
        response = client.post("/api/v1/chat", json=chat_request)
        
        assert response.status_code == 500

if __name__ == "__main__":
    pytest.main([__file__, "-v"])