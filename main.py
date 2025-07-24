import logging
import time
import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.responses import JSONResponse
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

from src.api.routes import router
from config import settings

# Configure logging
logging.basicConfig(
    level=getattr(logging, settings.LOG_LEVEL.upper()),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Manage application lifespan events."""
    # Startup
    logger.info("Starting Portfolio RAG Chatbot API")
    logger.info(f"Portfolio data path: {settings.PORTFOLIO_DATA_PATH}")
    logger.info(f"Vector database path: {settings.VECTOR_DB_PATH}")
    
    try:
        # Validate configuration
        settings.validate_required_settings()
        logger.info("Configuration validated successfully")
        
        # Initialize vector database on startup
        from vector_database import PortfolioVectorDB
        vector_db = PortfolioVectorDB()
        stats = vector_db.get_statistics()
        logger.info(f"Vector database initialized: {stats['total_documents']} documents loaded")
        
        yield
        
    except Exception as e:
        logger.error(f"Failed to initialize application: {e}")
        raise
    
    # Shutdown
    logger.info("Shutting down Portfolio RAG Chatbot API")

# Create FastAPI application
app = FastAPI(
    title="Portfolio RAG Chatbot API",
    description="""
    Intelligent conversational AI system for Mohammed Rishin's professional portfolio.
    
    This API provides endpoints to chat with an AI assistant that has comprehensive knowledge 
    about Mohammed's projects, education, work experience, certifications, and hackathon participation.
    
    ## Features
    
    - **Intelligent Chat**: Natural language conversations about portfolio content
    - **Technology-Specific Queries**: Ask about specific technologies like Node.js, Python, React
    - **Category Filtering**: Focus on projects, education, experience, certifications, or hackathons  
    - **Session Management**: Maintain conversation context across multiple interactions
    - **Source Citations**: All responses include references to original portfolio documents
    - **Follow-up Questions**: AI suggests relevant follow-up questions to continue the conversation
    
    ## Tech Stack
    
    - **Backend**: FastAPI with async/await support
    - **Vector Database**: ChromaDB for semantic search
    - **LLM**: Groq API with llama3-8b-8192 model
    - **Embeddings**: sentence-transformers (all-MiniLM-L6-v2)
    - **RAG Framework**: LangChain for retrieval-augmented generation
    """,
    version="1.0.0",
    contact={
        "name": "Mohammed Rishin Poolat",
        "url": "https://github.com/rishinpoolat/portfolio",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    },
    lifespan=lifespan
)

# Add middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(GZipMiddleware, minimum_size=1000)

# Custom middleware for request logging
@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Log all incoming requests."""
    start_time = time.time()
    
    # Log request
    logger.info(f"{request.method} {request.url.path} - {request.client.host}")
    
    # Process request
    response = await call_next(request)
    
    # Log response
    process_time = time.time() - start_time
    logger.info(f"Completed in {process_time:.2f}s - Status: {response.status_code}")
    
    return response

# Include API routes
app.include_router(router)

# Root endpoint
@app.get("/", tags=["Root"])
async def root():
    """Welcome endpoint with API information."""
    return {
        "message": "Welcome to Portfolio RAG Chatbot API",
        "description": "Intelligent AI assistant for Mohammed Rishin's professional portfolio",
        "version": "1.0.0",
        "docs_url": "/docs",
        "health_check": "/api/v1/health",
        "endpoints": {
            "chat": "/api/v1/chat",
            "search": "/api/v1/search", 
            "stats": "/api/v1/stats",
            "refresh": "/api/v1/refresh",
            "health": "/api/v1/health"
        }
    }

# Custom OpenAPI schema
def custom_openapi():
    """Generate custom OpenAPI schema with additional information."""
    if app.openapi_schema:
        return app.openapi_schema
    
    openapi_schema = get_openapi(
        title="Portfolio RAG Chatbot API",
        version="1.0.0",
        description=app.description,
        routes=app.routes,
    )
    
    # Add custom schema information
    openapi_schema["info"]["x-logo"] = {
        "url": "https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png"
    }
    
    # Add server information
    openapi_schema["servers"] = [
        {
            "url": f"http://{settings.API_HOST}:{settings.API_PORT}",
            "description": "Development server"
        }
    ]
    
    # Add examples to schemas
    openapi_schema["components"]["examples"] = {
        "ChatRequestExample": {
            "summary": "Example chat request",
            "value": {
                "message": "Tell me about Mohammed's Node.js projects",
                "session_id": "550e8400-e29b-41d4-a716-446655440000"
            }
        },
        "SearchRequestExample": {
            "summary": "Example search request",
            "value": {
                "query": "machine learning projects",
                "category": "projects",
                "limit": 5,
                "technologies": ["python", "tensorflow"]
            }
        }
    }
    
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Error handlers
@app.exception_handler(404)
async def not_found_handler(request: Request, exc):
    """Handle 404 errors."""
    return JSONResponse(
        status_code=404,
        content={
            "error": "NotFound",
            "message": f"The requested path '{request.url.path}' was not found",
            "available_endpoints": [
                "/",
                "/docs",
                "/api/v1/chat",
                "/api/v1/search",
                "/api/v1/stats",
                "/api/v1/refresh",
                "/api/v1/health"
            ]
        }
    )

@app.exception_handler(500)
async def internal_error_handler(request: Request, exc):
    """Handle 500 errors."""
    logger.error(f"Internal server error: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "InternalServerError",
            "message": "An internal server error occurred",
            "request_path": str(request.url.path)
        }
    )

if __name__ == "__main__":
    
    logger.info("=" * 60)
    logger.info("Portfolio RAG Chatbot API")
    logger.info("=" * 60)
    logger.info(f"Host: {settings.API_HOST}")
    logger.info(f"Port: {settings.API_PORT}")
    logger.info(f"Log Level: {settings.LOG_LEVEL}")
    logger.info(f"Portfolio Path: {settings.PORTFOLIO_DATA_PATH}")
    logger.info(f"Vector DB Path: {settings.VECTOR_DB_PATH}")
    logger.info("=" * 60)
    
    # Run the application
    uvicorn.run(
        "main:app",
        host=settings.API_HOST,
        port=settings.API_PORT,
        reload=True,
        log_level=settings.LOG_LEVEL.lower(),
        access_log=True
    )