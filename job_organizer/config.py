"""
Configuration module for Job Organizer
Supports environment variables for deployment
"""
import os
import logging


def setup_logging():
    """Configure application logging"""
    log_level = os.getenv("LOG_LEVEL", "INFO")
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format=log_format,
        handlers=[
            logging.StreamHandler(),
        ]
    )


class Config:
    """Application configuration with environment variable support"""
    
    # API Configuration
    API_BASE_URL: str = os.getenv("API_BASE_URL", "http://localhost:8000/api")
    API_TIMEOUT: float = float(os.getenv("API_TIMEOUT", "5.0"))
    
    # Reflex Configuration
    REFLEX_FRONTEND_PORT: int = int(os.getenv("PORT", "3000"))
    REFLEX_BACKEND_PORT: int = int(os.getenv("REFLEX_BACKEND_PORT", "8001"))
    
    # Deployment Configuration
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    DEBUG: bool = os.getenv("DEBUG", "True").lower() == "true"
    
    @classmethod
    def is_production(cls) -> bool:
        """Check if running in production environment"""
        return cls.ENVIRONMENT == "production"
    
    @classmethod
    def get_api_url(cls, endpoint: str) -> str:
        """Get full API URL for an endpoint"""
        return f"{cls.API_BASE_URL}/{endpoint.lstrip('/')}"


# Create singleton instance
config = Config()
