"""Environment configuration management."""

import os
from typing import Optional
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings from environment variables."""

    # API Configuration
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000
    DEBUG: bool = False

    # Scraper Configuration
    REQUEST_TIMEOUT: int = 30
    MAX_RETRIES: int = 3
    HEADLESS_BROWSER: bool = True

    # Proxy Configuration
    PROXY_LIST: Optional[str] = None  # Comma-separated proxy list
    USE_PROXY_ROTATION: bool = True

    # Database Configuration
    DATABASE_URL: str = "sqlite:///./data/amazon.db"

    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    LOG_FILE: Optional[str] = None

    # API Keys (if using external services)
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None

    class Config:
        """Pydantic config."""

        env_file = ".env"
        case_sensitive = True

    def get_proxies(self) -> list:
        """Get list of proxies from configuration."""
        if not self.PROXY_LIST:
            return []
        return [p.strip() for p in self.PROXY_LIST.split(",")]


# Global settings instance
settings = Settings()
