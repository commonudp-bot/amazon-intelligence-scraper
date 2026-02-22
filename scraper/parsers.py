

'''

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

'''

'''

"""HTML parsing logic for Amazon pages."""

import logging
from typing import Dict, List, Any, Optional
from bs4 import BeautifulSoup

logger = logging.getLogger(__name__)


class AmazonParser:
    """Parses Amazon HTML responses."""

    PRODUCT_CONTAINER = "div[data-component-type='s-search-result']"
    TITLE_SELECTOR = "h2 span"
    PRICE_SELECTOR = "span.a-price-whole"
    RATING_SELECTOR = "span.a-icon-alt"
    REVIEW_COUNT_SELECTOR = "span.a-size-base.s-underline-text"

    def parse_search_results(self, html: str) -> List[Dict[str, Any]]:
        soup = BeautifulSoup(html, "html.parser")
        products = []

        containers = soup.select(self.PRODUCT_CONTAINER)
        logger.info(f"Found {len(containers)} containers")

        for container in containers:
            try:
                product = self._parse_product_container(container)
                if product:
                    products.append(product)
            except Exception as e:
                logger.error(f"Error parsing product: {e}")
                continue

        logger.info(f"Parsed {len(products)} products")
        return products

    def _parse_product_container(self, container) -> Optional[Dict[str, Any]]:
        try:
            asin = container.get("data-asin")
            if not asin:
                return None

            title_elem = container.select_one(self.TITLE_SELECTOR)
            price_elem = container.select_one(self.PRICE_SELECTOR)
            rating_elem = container.select_one(self.RATING_SELECTOR)
            review_elem = container.select_one(self.REVIEW_COUNT_SELECTOR)

            return {
                "title": title_elem.get_text(strip=True) if title_elem else None,
                "asin": asin,
                "price": int(price_elem.get_text(strip=True).replace(",", "")) if price_elem else None,
                "rating": float(rating_elem.get_text().split()[0]) if rating_elem else None,
                "review_count": review_elem.get_text(strip=True) if review_elem else None,
                "url": f"https://www.amazon.in/dp/{asin}",
            }

        except Exception as e:
            logger.error(f"Parse error: {e}")
            return None
        
        
'''


'''

        
from bs4 import BeautifulSoup


class AmazonParser:
    """Reliable Amazon search parser."""

    PRODUCT_CONTAINER = "div[data-component-type='s-search-result']"

    def parse_search_results(self, html):
        soup = BeautifulSoup(html, "html.parser")
        products = []

        containers = soup.select(self.PRODUCT_CONTAINER)

        for container in containers:
            asin = container.get("data-asin")
            if not asin:
                continue

            # Title
            title_elem = container.select_one("h2 span")

            # Price
            price_elem = container.select_one(".a-price .a-offscreen")

            # Rating
            rating_elem = container.select_one(".a-icon-alt")

            # Review count
            review_elem = container.select_one(".s-underline-text")

            product = {
                "title": title_elem.text.strip() if title_elem else None,
                "asin": asin,
                "price": self._parse_price(price_elem),
                "rating": self._parse_rating(rating_elem),
                "review_count": review_elem.text.strip() if review_elem else None,
                "url": f"https://www.amazon.in/dp/{asin}",
            }

            products.append(product)

        return products

    def _parse_price(self, elem):
        if not elem:
            return None
        text = elem.text.replace("₹", "").replace(",", "").strip()
        return int(text) if text.isdigit() else None

    def _parse_rating(self, elem):
        if not elem:
            return None
        try:
            return float(elem.text.split()[0])
        except:
            return None
            
            
'''



'''


from bs4 import BeautifulSoup


class AmazonParser:
    PRODUCT_CONTAINER = "div[data-component-type='s-search-result']"

    def parse_search_results(self, html):
        soup = BeautifulSoup(html, "html.parser")
        products = []

        containers = soup.select(self.PRODUCT_CONTAINER)

        for c in containers:
            asin = c.get("data-asin")
            if not asin:
                continue

            title = c.select_one("h2 span")
            price = c.select_one(".a-price .a-offscreen")
            rating = c.select_one(".a-icon-alt")

            products.append({
                "title": title.text.strip() if title else None,
                "asin": asin,
                "price": self._price(price),
                "rating": self._rating(rating),
                "url": f"https://www.amazon.in/dp/{asin}",
            })

        return products

    def _price(self, elem):
        if not elem:
            return None
        return int(elem.text.replace("₹", "").replace(",", "").strip())

    def _rating(self, elem):
        if not elem:
            return None
        try:
            return float(elem.text.split()[0])
        except:
            return None




'''



'''

from bs4 import BeautifulSoup
import re


class AmazonParser:
    PRODUCT_CONTAINER = 'div[data-component-type="s-search-result"]'

    def parse_search_results(self, html):
        soup = BeautifulSoup(html, "html.parser")
        products = []

        containers = soup.select(self.PRODUCT_CONTAINER)

        for c in containers:
            asin = c.get("data-asin")
            if not asin:
                continue

            title = self._text(c, "h2 span")
            price_elem = c.select_one(".a-price .a-offscreen")
            rating_elem = c.select_one(".a-icon-alt")
            reviews_elem = c.select_one(".s-underline-text")

            price, currency = self._price(price_elem)
            rating = self._rating(rating_elem)
            reviews = self._reviews(reviews_elem)

            if title:
                products.append({
                    "title": title,
                    "asin": asin,
                    "price": price,
                    "currency": currency,
                    "rating": rating,
                    "review_count": reviews,
                    "seller": None,
                    "availability": None,
                    "url": f"https://www.amazon.in/dp/{asin}",
                })

        return products

    def _text(self, node, selector):
        el = node.select_one(selector)
        return el.get_text(strip=True) if el else None

    def _price(self, elem):
        if not elem:
            return None, None
        text = elem.text.strip()
        currency = "₹" if "₹" in text else None
        value = re.sub(r"[^\d]", "", text)
        return int(value) if value.isdigit() else None, currency

    def _rating(self, elem):
        if not elem:
            return None
        try:
            return float(elem.text.split()[0])
        except:
            return None

    def _reviews(self, elem):
        if not elem:
            return None
        text = elem.text.replace(",", "")
        return int(text) if text.isdigit() else None
    
    
    
    
    
    
'''

from bs4 import BeautifulSoup
import re


class AmazonParser:
    PRODUCT_CONTAINER = 'div[data-component-type="s-search-result"]'

    def parse_search_results(self, html):
        soup = BeautifulSoup(html, "html.parser")
        products = []

        containers = soup.select(self.PRODUCT_CONTAINER)

        for c in containers:
            asin = c.get("data-asin")
            if not asin:
                continue

            title = self._text(c, "h2 span")
            price_elem = c.select_one(".a-price .a-offscreen")
            rating_elem = c.select_one(".a-icon-alt")

            # ✅ multiple selectors for review count
            reviews_elem = (
                c.select_one(".s-underline-text")
                or c.select_one(".a-size-base.s-underline-text")
                or c.select_one("span[aria-label*='ratings']")
            )

            price, currency = self._price(price_elem)
            rating = self._rating(rating_elem)
            reviews = self._reviews(reviews_elem)

            if title:
                products.append({
                    "title": title,
                    "asin": asin,
                    "price": price,
                    "currency": currency,
                    "rating": rating,
                    "review_count": reviews,
                    "seller": None,        # from product page
                    "availability": None,  # from product page
                    "url": f"https://www.amazon.in/dp/{asin}",
                })

        return products

    # -------------------------
    # Helpers
    # -------------------------

    def _text(self, node, selector):
        el = node.select_one(selector)
        return el.get_text(strip=True) if el else None

    def _price(self, elem):
        if not elem:
            return None, None
        text = elem.get_text(strip=True)
        currency = "₹" if "₹" in text else None
        value = re.sub(r"[^\d]", "", text)
        return int(value) if value.isdigit() else None, currency

    def _rating(self, elem):
        if not elem:
            return None
        try:
            return float(elem.get_text().split()[0])
        except Exception:
            return None

    # ✅ FINAL FIXED VERSION
    def _reviews(self, elem):
        """
        Extract review count from multiple Amazon formats:
        - '1,234'
        - '1,234 ratings'
        - aria-label text
        """
        if not elem:
            return None

        text = elem.get_text(strip=True)

        # remove commas and extract numbers
        numbers = re.findall(r"\d+", text.replace(",", ""))

        return int(numbers[0]) if numbers else None