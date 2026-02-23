
'''


# working

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
                
                
'''

# working

"""Playwright fallback for JavaScript-rendered content."""

import logging
import platform
from typing import Optional
from playwright.async_api import async_playwright, TimeoutError as PlaywrightTimeoutError

logger = logging.getLogger(__name__)


class PlaywrightFallback:
    """Fallback handler using Playwright for JS-heavy pages."""

    def __init__(self, headless: bool = True):
        self.headless = headless
        self.use_webkit = platform.system() == "Darwin"  # Auto-use WebKit on macOS

    async def get_page_content(
        self,
        url: str,
        timeout: int = 30000,
        wait_selector: Optional[str] = None,
    ) -> Optional[str]:
        async with async_playwright() as p:
            browser = None
            context = None
            page = None

            try:
                # ✅ Auto-select stable browser
                browser_type = p.webkit if self.use_webkit else p.chromium

                logger.info("Using %s browser for fallback", "WebKit" if self.use_webkit else "Chromium")

                browser = await browser_type.launch(headless=self.headless)

                context = await browser.new_context(
                    user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                    viewport={"width": 1280, "height": 800},
                )

                page = await context.new_page()

                await page.goto(url, wait_until="domcontentloaded", timeout=timeout)

                if wait_selector:
                    await page.wait_for_selector(wait_selector, timeout=timeout)

                # small delay improves stability
                await page.wait_for_timeout(1000)

                content = await page.content()
                return content

            except PlaywrightTimeoutError:
                logger.warning("Playwright timeout while loading: %s", url)
                return None

            except Exception as e:
                logger.error("Playwright error: %s", e)
                return None

            finally:
                try:
                    if page:
                        await page.close()
                    if context:
                        await context.close()
                    if browser:
                        await browser.close()
                except Exception:
                    pass

