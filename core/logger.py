"""Logging configuration and setup."""

import logging
import sys
from typing import Optional
from core.config import settings


def setup_logging(
    name: str,
    log_level: Optional[str] = None,
    log_file: Optional[str] = None,
) -> logging.Logger:
    """
    Configure logger with console and optional file handlers.
    
    Args:
        name: Logger name (typically __name__)
        log_level: Log level (uses settings.LOG_LEVEL if not specified)
        log_file: Optional file path for log output
        
    Returns:
        Configured logger instance
    """
    log_level = log_level or settings.LOG_LEVEL
    log_file = log_file or settings.LOG_FILE

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level))

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(getattr(logging, log_level))

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(formatter)

    # Add console handler
    if not logger.handlers:
        logger.addHandler(console_handler)

    # File handler (optional)
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(getattr(logging, log_level))
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


# Application logger
app_logger = setup_logging(__name__)
