"""Application constants and selectors."""

# Amazon URLs
AMAZON_BASE_URL = "https://www.amazon.com"
AMAZON_SEARCH_URL = f"{AMAZON_BASE_URL}/s"
AMAZON_PRODUCT_URL = f"{AMAZON_BASE_URL}/dp"

# CSS Selectors for parsing
SELECTORS = {
    "search_results": {
        "product_container": "div[data-component-type='s-search-result']",
        "title": "h2 a span",
        "price": "span.a-price-whole",
        "rating": "span[aria-label*='stars']",
        "review_count": "span[aria-label*='ratings']",
        "seller": "span[data-a-color='base']",
        "availability": "span.a-size-base",
    },
    "product_details": {
        "title": "h1.product-title",
        "price": "span.a-price.a-text-price.a-size-medium",
        "rating": "span.a-star-small",
        "description": "div.feature-bullets-btf",
    },
}

# Request headers defaults
DEFAULT_HEADERS = {
    "Accept-Language": "en-US,en;q=0.9",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Referer": "https://www.amazon.com/",
    "DNT": "1",
}

# Error messages
ERROR_MESSAGES = {
    "captcha_detected": "CAPTCHA challenge detected - cannot proceed",
    "request_blocked": "Request was blocked by Amazon",
    "timeout": "Request timeout - server took too long to respond",
    "connection_error": "Failed to connect to server",
}

# Retry configuration defaults
RETRY_DEFAULTS = {
    "max_retries": 3,
    "initial_delay": 1.0,
    "max_delay": 60.0,
    "exponential_base": 2.0,
}

# Rate limiting
REQUESTS_PER_MINUTE = 10
MIN_REQUEST_DELAY = 0.5  # seconds
