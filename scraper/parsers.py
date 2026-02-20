"""HTML parsing logic for Amazon pages."""

import logging
from typing import Dict, List, Any, Optional
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class AmazonParser:
    """Parses Amazon HTML responses."""

    # CSS selectors for product data
    PRODUCT_CONTAINER = "div[data-component-type='s-search-result']"
    TITLE_SELECTOR = "h2 a span"
    PRICE_SELECTOR = "span.a-price-whole"
    RATING_SELECTOR = "span[aria-label*='stars']"
    REVIEW_COUNT_SELECTOR = "span[aria-label*='ratings']"

    def parse_search_results(self, html: str) -> List[Dict[str, Any]]:
        """
        Parse search results page.
        
        Args:
            html: HTML content of search results page
            
        Returns:
            List of parsed product data
        """
        soup = BeautifulSoup(html, "html.parser")
        products = []

        containers = soup.select(self.PRODUCT_CONTAINER)
        logger.info(f"Found {len(containers)} products")

        for container in containers:
            try:
                product = self._parse_product_container(container)
                if product:
                    products.append(product)
            except Exception as e:
                logger.error(f"Error parsing product: {e}")
                continue

        return products

    def parse_product_details(self, html: str) -> Dict[str, Any]:
        """
        Parse detailed product page.
        
        Args:
            html: HTML content of product details page
            
        Returns:
            Product details dictionary
        """
        soup = BeautifulSoup(html, "html.parser")
        # Implementation here
        return {}

    def _parse_product_container(
        self, container
    ) -> Optional[Dict[str, Any]]:
        """Parse a single product container."""
        try:
            title = container.select_one(self.TITLE_SELECTOR)
            price = container.select_one(self.PRICE_SELECTOR)

            return {
                "title": title.get_text(strip=True) if title else None,
                "price": price.get_text(strip=True) if price else None,
            }
        except Exception as e:
            logger.error(f"Parse error: {e}")
            return None
