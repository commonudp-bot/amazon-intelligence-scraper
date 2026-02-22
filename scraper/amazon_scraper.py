

'''

"""Amazon scraper orchestrator."""

import logging
from typing import List, Dict, Any, Optional

from network.session import SessionManager
from network.proxy_manager import ProxyManager
from scraper.parsers import AmazonParser
from scraper.captcha_detector import CaptchaDetector

logger = logging.getLogger(__name__)


class AmazonScraper:
    """Orchestrates Amazon scraping with retry and anti-blocking strategies."""

    def __init__(self, proxy_manager: Optional[ProxyManager] = None):
        """
        Initialize the scraper.

        Args:
            proxy_manager: Optional proxy manager for rotation
        """
        self.session_manager = SessionManager()
        self.proxy_manager = proxy_manager or ProxyManager()
        self.parser = AmazonParser()
        self.captcha_detector = CaptchaDetector()

    async def search_products(
        self,
        query: str,
        page: int = 1,
        **kwargs,
    ) -> List[Dict[str, Any]]:
        """
        Search Amazon for products.

        Args:
            query: Search query
            page: Page number
            **kwargs: Additional options

        Returns:
            List of product data
        """
        logger.info(f"Searching Amazon for: {query}")
        # Implementation here
        return []

    async def get_product_details(
        self,
        asin: str,
        **kwargs,
    ) -> Dict[str, Any]:
        """
        Get detailed information for a specific product.

        Args:
            asin: Amazon Standard Identification Number
            **kwargs: Additional options

        Returns:
            Product details dictionary
        """
        logger.info(f"Fetching details for ASIN: {asin}")
        # Implementation here
        return {}


'''


'''

"""Amazon scraper orchestrator."""

import logging
from typing import List, Dict, Any, Optional

from network.session import SessionManager
from network.proxy_manager import ProxyManager
from scraper.parsers import AmazonParser
from scraper.captcha_detector import CaptchaDetector

logger = logging.getLogger(__name__)


class AmazonScraper:
    """Orchestrates Amazon scraping with retry and anti-blocking strategies."""

    BASE_URL = "https://www.amazon.in"

    def __init__(self, proxy_manager: Optional[ProxyManager] = None):
        self.session_manager = SessionManager()
        self.proxy_manager = proxy_manager or ProxyManager()
        self.parser = AmazonParser()
        self.captcha_detector = CaptchaDetector()

    # -----------------------------------------------------
    # SEARCH PRODUCTS
    # -----------------------------------------------------
    async def search_products(
        self,
        query: str,
        page: int = 1,
        **kwargs,
    ) -> List[Dict[str, Any]]:
        """Search Amazon for products."""

        logger.info(f"Searching Amazon for: {query}")

        query_encoded = query.replace(" ", "+")
        url = f"{self.BASE_URL}/s?k={query_encoded}&page={page}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Accept-Language": "en-IN,en;q=0.9",
        }

        # ✅ FIX: get session correctly (do NOT use async with)
        session = await self.session_manager.get_session()

        try:
            async with session.get(url, headers=headers) as response:
                html = await response.text()
        finally:
            await session.close()

        # Debug (optional)
        logger.debug(f"HTML length: {len(html)}")
        logger.debug(f"'s-search-result' in HTML: {'s-search-result' in html}")

        # Detect CAPTCHA
        if self.captcha_detector.is_captcha_page(html):
            logger.warning("CAPTCHA detected — returning empty results")
            return []

        # Parse results
        products = self.parser.parse_search_results(html)

        logger.info(f"Parsed {len(products)} products")
        return products

    # -----------------------------------------------------
    # PRODUCT DETAILS
    # -----------------------------------------------------
    async def get_product_details(
        self,
        asin: str,
        **kwargs,
    ) -> Dict[str, Any]:
        """Get detailed information for a specific product."""

        logger.info(f"Fetching details for ASIN: {asin}")

        url = f"{self.BASE_URL}/dp/{asin}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Accept-Language": "en-IN,en;q=0.9",
        }

        # ✅ FIX: get session correctly
        session = await self.session_manager.get_session()

        try:
            async with session.get(url, headers=headers) as response:
                html = await response.text()
        finally:
            await session.close()

        if self.captcha_detector.is_captcha_page(html):
            logger.warning("CAPTCHA detected on product page")
            return {}

        # ⚠️ You can later implement real parser here
        return {
            "asin": asin,
            "url": url,
            "html_length": len(html),
        }
    


'''

'''


import requests
from scraper.parsers import AmazonParser

class AmazonScraper:
    BASE_URL = "https://www.amazon.in"

    def __init__(self):
        self.parser = AmazonParser()

    async def search_products(self, query: str, page: int = 1):
        url = f"{self.BASE_URL}/s?k={query.replace(' ', '+')}"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-IN,en;q=0.9",
        }

        response = requests.get(url, headers=headers)
        html = response.text

        print("HTML length:", len(html))
        print("Contains results:", "s-search-result" in html)

        return self.parser.parse_search_results(html)
    
    


'''


'''

   
"""Amazon scraper orchestrator."""

import logging
from typing import List, Dict, Any, Optional

from network.session import SessionManager
from network.proxy_manager import ProxyManager
from scraper.parsers import AmazonParser
from scraper.captcha_detector import CaptchaDetector
from scraper.playwright_fallback import PlaywrightFallback

logger = logging.getLogger(__name__)


class AmazonScraper:
    """Orchestrates Amazon scraping with retry and anti-blocking strategies."""

    BASE_URL = "https://www.amazon.in"

    def __init__(self, proxy_manager: Optional[ProxyManager] = None):
        self.session_manager = SessionManager()
        self.proxy_manager = proxy_manager or ProxyManager()
        self.parser = AmazonParser()
        self.captcha_detector = CaptchaDetector()
        self.playwright = PlaywrightFallback()

    async def search_products(self, query: str, page: int = 1) -> List[Dict[str, Any]]:
        logger.info(f"Searching Amazon for: {query}")

        query_encoded = query.replace(" ", "+")
        url = f"{self.BASE_URL}/s?k={query_encoded}&page={page}"

        headers = {
            "User-Agent": "Mozilla/5.0",
            "Accept-Language": "en-IN,en;q=0.9",
        }

        # ---------------------------
        # 1️⃣ Try aiohttp (fast)
        # ---------------------------
        session = await self.session_manager.get_session()

        try:
            async with session.get(url, headers=headers) as response:
                html = await response.text()
        finally:
            await session.close()

        logger.debug(f"HTML length: {len(html)}")

        # ---------------------------
        # 2️⃣ Detect bot HTML / CAPTCHA
        # ---------------------------
        if self.captcha_detector.is_captcha_page(html) or "s-search-result" not in html:
            logger.warning("Bot HTML detected → using Playwright fallback")
            html = await self.playwright.get_page_content(
                url,
                wait_selector="div[data-component-type='s-search-result']"
            )

            if not html:
                logger.error("Playwright failed to fetch content")
                return []

        # ---------------------------
        # 3️⃣ Parse results
        # ---------------------------
        products = self.parser.parse_search_results(html)

        logger.info(f"Parsed {len(products)} products")
        return products
        
        
'''
# working
"""Amazon scraper orchestrator."""

import logging
from typing import List, Dict, Any, Optional

from network.session import SessionManager
from network.proxy_manager import ProxyManager
from scraper.parsers import AmazonParser
from scraper.captcha_detector import CaptchaDetector
from scraper.playwright_fallback import PlaywrightFallback

logger = logging.getLogger(__name__)


class AmazonScraper:
    """Orchestrates Amazon scraping with retry and anti-blocking strategies."""

    BASE_URL = "https://www.amazon.in"

    def __init__(self, proxy_manager: Optional[ProxyManager] = None):
        self.session_manager = SessionManager()
        self.proxy_manager = proxy_manager or ProxyManager()
        self.parser = AmazonParser()
        self.captcha_detector = CaptchaDetector()
        self.playwright = PlaywrightFallback()

    async def search_products(
        self,
        query: str,
        page: int = 1
    ) -> List[Dict[str, Any]]:
        """Search Amazon for products."""

        logger.info(f"Searching Amazon for: {query}")

        query_encoded = query.replace(" ", "+")
        url = f"{self.BASE_URL}/s?k={query_encoded}&page={page}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Accept-Language": "en-IN,en;q=0.9",
        }

        # -------------------------------------------------
        # 1️⃣ Try aiohttp first (fast)
        # -------------------------------------------------
        html = ""
        try:
            session = await self.session_manager.get_session()
            async with session.get(url, headers=headers) as response:
                html = await response.text()
        except Exception as e:
            logger.warning(f"aiohttp fetch failed: {e}")
        finally:
            try:
                await session.close()
            except:
                pass

        logger.info(f"aiohttp HTML length: {len(html)}")

        # -------------------------------------------------
        # 2️⃣ Detect bot HTML or missing results
        # -------------------------------------------------
        needs_fallback = (
            not html
            or self.captcha_detector.is_captcha_page(html)
            or 'data-component-type="s-search-result"' not in html
        )

        if needs_fallback:
            logger.warning("Using Playwright fallback...")

            html = await self.playwright.get_page_content(
                url,
                wait_selector='div[data-component-type="s-search-result"]'
            )

            if not html:
                logger.error("Playwright failed to fetch content")
                return []

            logger.info(f"Playwright HTML length: {len(html)}")

        # -------------------------------------------------
        # 3️⃣ Parse results
        # -------------------------------------------------
        products = self.parser.parse_search_results(html)

        logger.info(f"Parsed {len(products)} products")
        return products

