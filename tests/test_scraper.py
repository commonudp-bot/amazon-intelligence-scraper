"""Tests for Amazon scraper."""

import pytest
import asyncio
from scraper.amazon_scraper import AmazonScraper


@pytest.fixture
def scraper():
    """Create scraper instance."""
    return AmazonScraper()


@pytest.mark.asyncio
async def test_search_products(scraper):
    """Test product search."""
    results = await scraper.search_products("laptop")
    assert isinstance(results, list)


@pytest.mark.asyncio
async def test_get_product_details(scraper):
    """Test getting product details."""
    details = await scraper.get_product_details("B07PYLT6DN")
    assert isinstance(details, dict)


def test_scraper_initialization():
    """Test scraper initializes properly."""
    scraper = AmazonScraper()
    assert scraper.parser is not None
    assert scraper.captcha_detector is not None
    assert scraper.session_manager is not None
