import time
import logging
from datetime import datetime
from typing import Optional
from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.responses import JSONResponse

from src.models.schemas import (
    ChatRequest, ChatResponse, SearchRequest, SearchResponse, 
    DatabaseStats, RefreshResponse, HealthResponse, ErrorResponse,
    SessionStats
)
from src.services.chat_service import ChatService
from src.services.rag_service import RAGService
from vector_database import PortfolioVectorDB
from config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize services (will be overridden by dependency injection)
_chat_service: Optional[ChatService] = None
_vector_db: Optional[PortfolioVectorDB] = None

def get_vector_db() -> PortfolioVectorDB:
    """Dependency to get vector database instance."""
    global _vector_db
    if _vector_db is None:
        try:
            _vector_db = PortfolioVectorDB()
            logger.info("Vector database initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize vector database: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to initialize vector database"
            )
    return _vector_db

def get_chat_service(vector_db: PortfolioVectorDB = Depends(get_vector_db)) -> ChatService:
    """Dependency to get chat service instance."""
    global _chat_service
    if _chat_service is None:
        try:
            rag_service = RAGService(vector_db)
            _chat_service = ChatService(vector_db, rag_service)
            logger.info("Chat service initialized successfully")
        except Exception as e:
            logger.error(f"Failed to initialize chat service: {e}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to initialize chat service"
            )
    return _chat_service

# Create API router
router = APIRouter(prefix="/api/v1", tags=["Portfolio RAG Chatbot"])

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service)
) -> ChatResponse:
    """
    Chat with the portfolio AI assistant.
    
    Process user messages and return AI-generated responses based on Mohammed Rishin's portfolio.
    Supports conversation continuity through session management.
    """
    try:
        logger.info(f"Processing chat request: {request.message[:50]}...")
        
        # Validate required settings
        settings.validate_required_settings()
        
        # Process the message
        result = await chat_service.process_message(
            message=request.message,
            session_id=request.session_id
        )
        
        # Convert to response model
        response = ChatResponse(
            response=result['response'],
            sources=[
                {
                    'filename': source['filename'],
                    'category': source['category'],
                    'relevance_score': max(0.0, source['relevance_score']),  # Ensure non-negative
                    'file_path': source['file_path'],
                    'chunk_id': source['chunk_id'],
                    'technologies': source['technologies'].split(', ') if isinstance(source['technologies'], str) else source['technologies']
                }
                for source in result['sources']
            ],
            suggested_questions=result['suggested_questions'],
            session_id=result['session_id'],
            response_time=result['response_time'],
            session_context=result.get('session_context'),
            query_classification=result.get('query_classification')
        )
        
        logger.info(f"Chat response generated successfully in {result['response_time']:.2f}s")
        return response
        
    except ValueError as e:
        logger.error(f"Configuration error in chat endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Configuration error: {str(e)}"
        )
    except Exception as e:
        logger.error(f"Error in chat endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while processing your message"
        )

@router.post("/search", response_model=SearchResponse)
async def search_endpoint(
    request: SearchRequest,
    vector_db: PortfolioVectorDB = Depends(get_vector_db)
) -> SearchResponse:
    """
    Search through Mohammed Rishin's portfolio content.
    
    Perform similarity search across portfolio documents with optional category 
    and technology filtering.
    """
    try:
        start_time = time.time()
        logger.info(f"Processing search request: {request.query[:50]}...")
        
        # Perform search
        results = vector_db.search_similar(
            query=request.query,
            category=request.category,
            n_results=request.limit,
            technologies=request.technologies
        )
        
        # Get query classification
        from src.services.rag_service import RAGService
        rag_service = RAGService(vector_db)
        classification = rag_service.classify_query_intent(request.query)
        
        query_time = time.time() - start_time
        
        # Format response
        search_results = [
            {
                'document': result['document'],
                'metadata': result['metadata'],
                'relevance_score': result['relevance_score']
            }
            for result in results
        ]
        
        response = SearchResponse(
            results=search_results,
            total_results=len(results),
            query_time=query_time,
            query_classification=classification
        )
        
        logger.info(f"Search completed: {len(results)} results in {query_time:.2f}s")
        return response
        
    except Exception as e:
        logger.error(f"Error in search endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while searching"
        )

@router.get("/stats", response_model=DatabaseStats)
async def stats_endpoint(
    vector_db: PortfolioVectorDB = Depends(get_vector_db)
) -> DatabaseStats:
    """
    Get portfolio database statistics.
    
    Returns information about document counts, collections, and available categories.
    """
    try:
        logger.info("Retrieving database statistics")
        
        stats = vector_db.get_statistics()
        
        response = DatabaseStats(
            collections=stats['collections'],
            total_documents=stats['total_documents'],
            categories=stats['categories']
        )
        
        logger.info(f"Database stats retrieved: {stats['total_documents']} total documents")
        return response
        
    except Exception as e:
        logger.error(f"Error in stats endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving statistics"
        )

@router.post("/refresh", response_model=RefreshResponse)
async def refresh_endpoint(
    vector_db: PortfolioVectorDB = Depends(get_vector_db)
) -> RefreshResponse:
    """
    Refresh the portfolio database.
    
    Reprocess all portfolio markdown files and rebuild the vector database.
    This operation may take several seconds to complete.
    """
    try:
        start_time = time.time()
        logger.info("Starting database refresh")
        
        # Refresh the database
        stats = vector_db.refresh_database()
        refresh_time = time.time() - start_time
        
        # Reset global services to reinitialize with fresh data
        global _chat_service
        _chat_service = None
        
        response = RefreshResponse(
            message="Database refreshed successfully",
            stats=stats,
            refresh_time=refresh_time
        )
        
        logger.info(f"Database refresh completed in {refresh_time:.2f}s")
        return response
        
    except Exception as e:
        logger.error(f"Error in refresh endpoint: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while refreshing the database"
        )

@router.get("/health", response_model=HealthResponse)
async def health_endpoint() -> HealthResponse:
    """
    Health check endpoint.
    
    Returns the current status of the API and its dependencies.
    """
    try:
        services_status = {}
        overall_status = "healthy"
        
        # Check vector database
        try:
            vector_db = get_vector_db()
            vector_db.get_statistics()
            services_status["vector_database"] = "healthy"
        except Exception as e:
            logger.warning(f"Vector database health check failed: {e}")
            services_status["vector_database"] = "unhealthy"
            overall_status = "degraded"
        
        # Check Groq API
        try:
            settings.validate_required_settings()
            services_status["groq_api"] = "healthy"
        except Exception as e:
            logger.warning(f"Groq API health check failed: {e}")
            services_status["groq_api"] = "unhealthy"
            overall_status = "degraded"
        
        # Check chat service
        try:
            if _chat_service is not None or services_status.get("vector_database") == "healthy":
                services_status["chat_service"] = "healthy"
            else:
                services_status["chat_service"] = "unknown"
        except Exception as e:
            logger.warning(f"Chat service health check failed: {e}")
            services_status["chat_service"] = "unhealthy"
            overall_status = "degraded"
        
        response = HealthResponse(
            status=overall_status,
            timestamp=datetime.utcnow().isoformat() + "Z",
            version="1.0.0",
            services=services_status
        )
        
        logger.info(f"Health check completed: {overall_status}")
        return response
        
    except Exception as e:
        logger.error(f"Error in health check: {e}")
        return HealthResponse(
            status="unhealthy",
            timestamp=datetime.utcnow().isoformat() + "Z",
            version="1.0.0",
            services={"error": str(e)}
        )

@router.get("/sessions/{session_id}/stats", response_model=SessionStats)
async def session_stats_endpoint(
    session_id: str,
    chat_service: ChatService = Depends(get_chat_service)
) -> SessionStats:
    """
    Get statistics for a specific chat session.
    
    Returns detailed information about a chat session including message counts,
    duration, and conversation context.
    """
    try:
        logger.info(f"Retrieving stats for session: {session_id}")
        
        stats = chat_service.get_session_stats(session_id)
        
        if not stats:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Session not found or expired"
            )
        
        response = SessionStats(**stats)
        
        logger.info(f"Session stats retrieved for {session_id}")
        return response
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error retrieving session stats: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving session statistics"
        )

@router.get("/sessions/stats", response_model=dict)
async def all_sessions_stats_endpoint(
    chat_service: ChatService = Depends(get_chat_service)
) -> dict:
    """
    Get statistics for all active chat sessions.
    
    Returns aggregate information about all active sessions including most 
    discussed topics and technologies.
    """
    try:
        logger.info("Retrieving stats for all sessions")
        
        stats = chat_service.get_all_sessions_stats()
        
        logger.info(f"All sessions stats retrieved: {stats['active_sessions']} active sessions")
        return stats
        
    except Exception as e:
        logger.error(f"Error retrieving all sessions stats: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while retrieving session statistics"
        )

# Note: Exception handlers are in main.py since APIRouter doesn't support them