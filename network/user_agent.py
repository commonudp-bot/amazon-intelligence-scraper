"""User-agent rotation for requests."""

import random
import logging

logger = logging.getLogger(__name__)


class UserAgentManager:
    """Manages user-agent rotation."""

    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
    ]

    @classmethod
    def get_random_user_agent(cls) -> str:
        """
        Get a random user-agent string.
        
        Returns:
            Random user-agent string
        """
        return random.choice(cls.USER_AGENTS)

    @classmethod
    def add_user_agent(cls, user_agent: str) -> None:
        """Add a custom user-agent."""
        if user_agent not in cls.USER_AGENTS:
            cls.USER_AGENTS.append(user_agent)
            logger.info(f"Added user-agent: {user_agent}")
