"""Reusable session configuration."""

import logging
import aiohttp
from typing import Optional
from network.user_agent import UserAgentManager

logger = logging.getLogger(__name__)


class SessionManager:
    """Manages HTTP session with common headers and configuration."""

    def __init__(self):
        """Initialize session manager."""
        self.ua_manager = UserAgentManager()
        self.session: Optional[aiohttp.ClientSession] = None

    async def get_session(self) -> aiohttp.ClientSession:
        """Get or create aiohttp session."""
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession()
        return self.session

    def get_headers(self) -> dict:
        """Get default headers with rotating user-agent."""
        return {
            "User-Agent": self.ua_manager.get_random_user_agent(),
            "Accept-Language": "en-US,en;q=0.9",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Referer": "https://www.amazon.com/",
            "DNT": "1",
        }

    async def close(self) -> None:
        """Close the session."""
        if self.session and not self.session.closed:
            await self.session.close()
            logger.info("Session closed")
