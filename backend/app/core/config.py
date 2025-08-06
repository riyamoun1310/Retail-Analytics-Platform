from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    # Database - Use SQLite for Vercel deployment or PostgreSQL for production
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", 
        "sqlite:///./retail_analytics.db"
    )
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # OpenAI
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    
    # Environment
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    # CORS - Updated for Vercel deployment
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000", 
        "http://localhost:5173",
        "https://vercel.app",
        "https://*.vercel.app"
    ]
    
    # ML Models
    MODEL_PATH: str = "./models/"
    RETRAIN_INTERVAL_HOURS: int = 24
    
    class Config:
        env_file = "../.env"
        case_sensitive = True

# Create settings instance
settings = Settings()
