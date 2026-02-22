"""Proxy rotation and management."""

import logging
from typing import List, Optional
from itertools import cycle

logger = logging.getLogger(__name__)


class ProxyManager:
    """Manages proxy rotation and validation."""

    def __init__(self, proxies: Optional[List[str]] = None):
        """
        Initialize proxy manager.
        
        Args:
            proxies: List of proxy URLs
        """
        self.proxies = proxies or []
        self.proxy_cycle = cycle(self.proxies) if self.proxies else None

    def add_proxy(self, proxy: str) -> None:
        """Add a proxy to the pool."""
        self.proxies.append(proxy)
        self.proxy_cycle = cycle(self.proxies)
        logger.info(f"Added proxy: {proxy}")

    def add_proxies(self, proxies: List[str]) -> None:
        """Add multiple proxies."""
        self.proxies.extend(proxies)
        self.proxy_cycle = cycle(self.proxies)
        logger.info(f"Added {len(proxies)} proxies")

    def get_next_proxy(self) -> Optional[str]:
        """Get next proxy from rotation."""
        if self.proxy_cycle is None:
            return None
        
        return next(self.proxy_cycle)

    def validate_proxy(self, proxy: str) -> bool:
        """
        Validate proxy format.
        
        Args:
            proxy: Proxy URL to validate
            
        Returns:
            True if valid, False otherwise
        """
        # Basic validation
        return proxy.startswith(("http://", "https://", "socks5://"))

    def get_proxy_dict(self, proxy: str) -> dict:
        """Convert proxy URL to requests proxy dict."""
        return {
            "http": proxy,
            "https": proxy,
        }
