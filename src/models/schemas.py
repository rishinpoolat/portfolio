from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field
from datetime import datetime

class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    message: str = Field(..., min_length=1, max_length=2000, description="User's message")
    session_id: Optional[str] = Field(None, description="Optional session ID for conversation continuity")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "Tell me about Mohammed's Node.js projects",
                "session_id": "550e8400-e29b-41d4-a716-446655440000"
            }
        }

class SourceDocument(BaseModel):
    """Model for source document information."""
    filename: str = Field(..., description="Name of the source file")
    category: str = Field(..., description="Category of the source (projects, education, etc.)")
    relevance_score: float = Field(..., ge=0.0, le=1.0, description="Relevance score between 0 and 1")
    file_path: str = Field(..., description="Path to the source file")
    chunk_id: str = Field(..., description="Unique identifier for the text chunk")
    technologies: List[str] = Field(default_factory=list, description="Technologies mentioned in the source")
    
    class Config:
        json_schema_extra = {
            "example": {
                "filename": "nodejs-project.md",
                "category": "projects",
                "relevance_score": 0.95,
                "file_path": "/path/to/projects/nodejs-project.md",
                "chunk_id": "projects_nodejs_0",
                "technologies": ["nodejs", "express", "mongodb"]
            }
        }

class QueryClassification(BaseModel):
    """Model for query classification information."""
    categories: List[str] = Field(default_factory=list, description="Detected categories")
    technologies: List[str] = Field(default_factory=list, description="Detected technologies")
    intent_type: str = Field(..., description="Type of intent (descriptive, analytical, etc.)")
    confidence: float = Field(..., ge=0.0, le=1.0, description="Classification confidence")
    
    class Config:
        json_schema_extra = {
            "example": {
                "categories": ["projects"],
                "technologies": ["nodejs", "react"],
                "intent_type": "technology_specific",
                "confidence": 0.85
            }
        }

class SessionContext(BaseModel):
    """Model for session context information."""
    topics_discussed: List[str] = Field(default_factory=list, description="Topics discussed in the session")
    technologies_mentioned: List[str] = Field(default_factory=list, description="Technologies mentioned")
    categories_explored: List[str] = Field(default_factory=list, description="Categories explored")
    
    class Config:
        json_schema_extra = {
            "example": {
                "topics_discussed": ["project", "education"],
                "technologies_mentioned": ["nodejs", "python", "react"],
                "categories_explored": ["projects", "education"]
            }
        }

class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    response: str = Field(..., description="AI-generated response")
    sources: List[SourceDocument] = Field(default_factory=list, description="Source documents used")
    suggested_questions: List[str] = Field(default_factory=list, description="Follow-up questions")
    session_id: str = Field(..., description="Session identifier")
    response_time: float = Field(..., description="Response generation time in seconds")
    session_context: Optional[SessionContext] = Field(None, description="Current session context")
    query_classification: Optional[QueryClassification] = Field(None, description="Query classification details")
    
    class Config:
        json_schema_extra = {
            "example": {
                "response": "Mohammed has several Node.js projects including a real-time chat application...",
                "sources": [
                    {
                        "filename": "nodejs-project.md",
                        "category": "projects",
                        "relevance_score": 0.95,
                        "file_path": "/path/to/projects/nodejs-project.md",
                        "chunk_id": "projects_nodejs_0",
                        "technologies": ["nodejs", "express"]
                    }
                ],
                "suggested_questions": [
                    "What technologies did he use in these Node.js projects?",
                    "How long did these projects take to complete?",
                    "What was the most challenging aspect?"
                ],
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "response_time": 1.23,
                "session_context": {
                    "topics_discussed": ["project"],
                    "technologies_mentioned": ["nodejs"],
                    "categories_explored": ["projects"]
                },
                "query_classification": {
                    "categories": ["projects"],
                    "technologies": ["nodejs"],
                    "intent_type": "technology_specific",
                    "confidence": 0.85
                }
            }
        }

class SearchRequest(BaseModel):
    """Request model for search endpoint."""
    query: str = Field(..., min_length=1, max_length=1000, description="Search query")
    category: Optional[str] = Field(None, description="Optional category filter")
    limit: int = Field(default=10, ge=1, le=50, description="Maximum number of results")
    technologies: Optional[List[str]] = Field(None, description="Technology filters")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "machine learning projects",
                "category": "projects", 
                "limit": 5,
                "technologies": ["python", "tensorflow"]
            }
        }

class SearchResult(BaseModel):
    """Model for individual search result."""
    document: str = Field(..., description="Content of the document chunk")
    metadata: Dict[str, Any] = Field(..., description="Document metadata")
    relevance_score: float = Field(..., ge=0.0, le=1.0, description="Relevance score")
    
    class Config:
        json_schema_extra = {
            "example": {
                "document": "Machine learning project using TensorFlow for image classification...",
                "metadata": {
                    "filename": "ml-project.md",
                    "category": "projects",
                    "technologies": ["python", "tensorflow"]
                },
                "relevance_score": 0.92
            }
        }

class SearchResponse(BaseModel):
    """Response model for search endpoint."""
    results: List[SearchResult] = Field(..., description="Search results")
    total_results: int = Field(..., description="Total number of results found")
    query_time: float = Field(..., description="Query execution time in seconds")
    query_classification: Optional[QueryClassification] = Field(None, description="Query classification")
    
    class Config:
        json_schema_extra = {
            "example": {
                "results": [
                    {
                        "document": "Machine learning project using TensorFlow...",
                        "metadata": {"filename": "ml-project.md", "category": "projects"},
                        "relevance_score": 0.92
                    }
                ],
                "total_results": 3,
                "query_time": 0.45,
                "query_classification": {
                    "categories": ["projects"],
                    "technologies": ["python", "tensorflow"],
                    "intent_type": "technology_specific",
                    "confidence": 0.88
                }
            }
        }

class DatabaseStats(BaseModel):
    """Model for database statistics."""
    collections: Dict[str, int] = Field(..., description="Document count per collection")
    total_documents: int = Field(..., description="Total number of documents")
    categories: List[str] = Field(..., description="Available categories")
    
    class Config:
        json_schema_extra = {
            "example": {
                "collections": {
                    "projects": 12,
                    "education": 3,
                    "experience": 4,
                    "certification": 2,
                    "hackathon": 1,
                    "unified": 22
                },
                "total_documents": 22,
                "categories": ["projects", "education", "experience", "certification", "hackathon"]
            }
        }

class RefreshResponse(BaseModel):
    """Response model for database refresh endpoint."""
    message: str = Field(..., description="Status message")
    stats: Dict[str, Any] = Field(..., description="Refresh operation statistics")
    refresh_time: float = Field(..., description="Time taken to refresh in seconds")
    
    class Config:
        json_schema_extra = {
            "example": {
                "message": "Database refreshed successfully",
                "stats": {
                    "total_files": 15,
                    "successful": 15,
                    "failed": 0,
                    "total_chunks": 67
                },
                "refresh_time": 12.34
            }
        }

class HealthResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str = Field(..., description="Service status")
    timestamp: str = Field(..., description="Health check timestamp")
    version: str = Field(..., description="API version")
    services: Dict[str, str] = Field(..., description="Status of individual services")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "healthy",
                "timestamp": "2024-01-15T10:30:00Z",
                "version": "1.0.0",
                "services": {
                    "vector_database": "healthy",
                    "groq_api": "healthy",
                    "chat_service": "healthy"
                }
            }
        }

class ErrorResponse(BaseModel):
    """Model for error responses."""
    error: str = Field(..., description="Error type")
    message: str = Field(..., description="Error message")
    details: Optional[Dict[str, Any]] = Field(None, description="Additional error details")
    timestamp: str = Field(..., description="Error timestamp")
    
    class Config:
        json_schema_extra = {
            "example": {
                "error": "ValidationError",
                "message": "Message cannot be empty",
                "details": {"field": "message", "value": ""},
                "timestamp": "2024-01-15T10:30:00Z"
            }
        }

class SessionStats(BaseModel):
    """Model for session statistics."""
    session_id: str = Field(..., description="Session identifier")
    created_at: str = Field(..., description="Session creation timestamp")
    last_activity: str = Field(..., description="Last activity timestamp")
    duration_seconds: float = Field(..., description="Session duration in seconds")
    total_messages: int = Field(..., description="Total number of messages")
    user_messages: int = Field(..., description="Number of user messages")
    assistant_messages: int = Field(..., description="Number of assistant messages")
    context: SessionContext = Field(..., description="Session context")
    
    class Config:
        json_schema_extra = {
            "example": {
                "session_id": "550e8400-e29b-41d4-a716-446655440000",
                "created_at": "2024-01-15T10:00:00Z",
                "last_activity": "2024-01-15T10:30:00Z",
                "duration_seconds": 1800.0,
                "total_messages": 6,
                "user_messages": 3,
                "assistant_messages": 3,
                "context": {
                    "topics_discussed": ["project", "education"],
                    "technologies_mentioned": ["nodejs", "python"],
                    "categories_explored": ["projects", "education"]
                }
            }
        }