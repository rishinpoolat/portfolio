import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings:
    # Required Environment Variables
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "")
    
    # Paths
    PORTFOLIO_DATA_PATH: str = os.getenv(
        "PORTFOLIO_DATA_PATH", 
        "/Users/mohammedrishinpoolat/Projects/personal-projects/portfolio"
    )
    VECTOR_DB_PATH: str = os.getenv("VECTOR_DB_PATH", "./vector_db")
    
    # API Configuration
    API_HOST: str = os.getenv("API_HOST", "0.0.0.0")
    API_PORT: int = int(os.getenv("API_PORT", "8000"))
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    
    # RAG Settings
    CHUNK_SIZE: int = int(os.getenv("CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "200"))
    RETRIEVAL_K: int = int(os.getenv("RETRIEVAL_K", "5"))
    
    # Model Configuration
    GROQ_MODEL: str = os.getenv("GROQ_MODEL", "llama3-8b-8192")
    EMBEDDING_MODEL: str = os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2")
    
    # Content Categories
    CONTENT_CATEGORIES = ["projects", "education", "experience", "certification", "hackathon"]
    
    # Query Classification Patterns
    CATEGORY_PATTERNS = {
        'projects': [
            'project', 'built', 'developed', 'technology', 'code', 'nodejs', 'python', 
            'react', 'typescript', 'application', 'system', 'app', 'software', 'web',
            'frontend', 'backend', 'fullstack', 'database', 'api', 'framework'
        ],
        'education': [
            'education', 'degree', 'university', 'study', 'academic', 'graduation',
            'school', 'college', 'bachelor', 'master', 'phd', 'course', 'learning'
        ],
        'experience': [
            'experience', 'work', 'job', 'company', 'role', 'professional', 'career',
            'employment', 'position', 'intern', 'volunteer', 'responsibility'
        ],
        'certification': [
            'certification', 'certified', 'credential', 'aws', 'cloud', 'certificate',
            'license', 'qualification', 'training', 'skill'
        ],
        'hackathon': [
            'hackathon', 'competition', 'contest', 'ibm', 'challenge', 'event',
            'coding', 'programming', 'innovation', 'startup'
        ]
    }
    
    def validate_required_settings(self) -> bool:
        """Validate that all required environment variables are set."""
        if not self.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY environment variable is required")
        return True

settings = Settings()