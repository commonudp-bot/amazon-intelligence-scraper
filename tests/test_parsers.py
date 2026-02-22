"""Tests for HTML parsers."""

import pytest
from scraper.parsers import AmazonParser


@pytest.fixture
def parser():
    """Create parser instance."""
    return AmazonParser()


def test_parse_search_results(parser):
    """Test parsing search results HTML."""
    # Mock HTML would be provided here
    html = "<html></html>"
    results = parser.parse_search_results(html)
    assert isinstance(results, list)


def test_parse_product_details(parser):
    """Test parsing product details HTML."""
    html = "<html></html>"
    details = parser.parse_product_details(html)
    assert isinstance(details, dict)


def test_valid_selectors(parser):
    """Test that CSS selectors are properly defined."""
    assert parser.PRODUCT_CONTAINER
    assert parser.TITLE_SELECTOR
    assert parser.PRICE_SELECTOR
