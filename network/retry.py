"""Retry logic with exponential backoff."""

import asyncio
import logging
import random
from typing import Callable, Any, TypeVar, Optional

logger = logging.getLogger(__name__)

T = TypeVar("T")


class RetryConfig:
    """Retry configuration."""

    def __init__(
        self,
        max_retries: int = 3,
        initial_delay: float = 1.0,
        max_delay: float = 60.0,
        exponential_base: float = 2.0,
        jitter: bool = True,
    ):
        """
        Initialize retry config.
        
        Args:
            max_retries: Maximum number of retries
            initial_delay: Initial delay in seconds
            max_delay: Maximum delay in seconds
            exponential_base: Base for exponential backoff
            jitter: Whether to add random jitter
        """
        self.max_retries = max_retries
        self.initial_delay = initial_delay
        self.max_delay = max_delay
        self.exponential_base = exponential_base
        self.jitter = jitter


async def retry_with_backoff(
    func: Callable[..., Any],
    config: Optional[RetryConfig] = None,
    *args,
    **kwargs,
) -> Any:
    """
    Execute function with retry and exponential backoff.
    
    Args:
        func: Async function to execute
        config: Retry configuration
        *args: Function arguments
        **kwargs: Function keyword arguments
        
    Returns:
        Function result
    """
    config = config or RetryConfig()
    
    for attempt in range(config.max_retries + 1):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            if attempt == config.max_retries:
                logger.error(f"Max retries exceeded: {e}")
                raise
            
            delay = min(
                config.initial_delay * (config.exponential_base ** attempt),
                config.max_delay,
            )
            
            if config.jitter:
                delay *= (0.5 + random.random())
            
            logger.warning(
                f"Attempt {attempt + 1} failed, retrying in {delay:.2f}s: {e}"
            )
            await asyncio.sleep(delay)
