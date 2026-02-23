
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

