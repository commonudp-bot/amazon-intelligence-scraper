
'''

"""Playwright fallback for JavaScript-rendered content."""

import logging
from typing import Optional
from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)


class PlaywrightFallback:
    """Fallback handler using Playwright for JS-heavy pages."""

    def __init__(self, headless: bool = True):
        """
        Initialize Playwright fallback.

        Args:
            headless: Whether to run browser in headless mode
        """
        self.headless = headless

    async def get_page_content(
        self,
        url: str,
        timeout: int = 30000,
        wait_selector: Optional[str] = None,
    ) -> Optional[str]:
        """
        Get page content using Playwright.

        Args:
            url: URL to fetch
            timeout: Timeout in milliseconds
            wait_selector: Optional CSS selector to wait for

        Returns:
            Page HTML content or None if failed
        """
        async with async_playwright() as p:
            try:
                browser = await p.chromium.launch(headless=self.headless)
                page = await browser.new_page()

                await page.goto(url, wait_until="networkidle", timeout=timeout)

                if wait_selector:
                    await page.wait_for_selector(wait_selector, timeout=timeout)

                content = await page.content()
                await browser.close()

                return content

            except Exception as e:
                logger.error(f"Playwright error: {e}")
                return None



'''

"""Playwright fallback for JavaScript-rendered content."""

import logging
from typing import Optional
from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)


class PlaywrightFallback:
    """Fallback handler using Playwright for JS-heavy pages."""

    def __init__(self, headless: bool = True):
        self.headless = headless

    async def get_page_content(
        self,
        url: str,
        timeout: int = 30000,
        wait_selector: Optional[str] = None,
    ) -> Optional[str]:
        async with async_playwright() as p:
            try:
                browser = await p.chromium.launch(headless=self.headless)
                context = await browser.new_context(
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                )
                page = await context.new_page()

                await page.goto(url, wait_until="networkidle", timeout=timeout)

                if wait_selector:
                    await page.wait_for_selector(wait_selector, timeout=timeout)

                content = await page.content()
                await browser.close()

                return content

            except Exception as e:
                logger.error(f"Playwright error: {e}")
                return None