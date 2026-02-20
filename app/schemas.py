"""Pydantic schemas for request/response validation."""

from typing import List, Optional
from pydantic import BaseModel


class ProductData(BaseModel):
    """Product information model."""

    title: str
    asin: str
    price: Optional[float] = None
    currency: Optional[str] = None
    rating: Optional[float] = None
    review_count: Optional[int] = None
    seller: Optional[str] = None
    availability: Optional[str] = None
    url: str


class ProductSearchRequest(BaseModel):
    """Search request schema."""

    query: str
    page: int = 1
    proxy: Optional[str] = None
    timeout: int = 30
    headless: bool = True


class ProductDetailsRequest(BaseModel):
    """Product details request schema."""

    asin: str
    proxy: Optional[str] = None
    timeout: int = 30
    headless: bool = True


class ScrapeResponse(BaseModel):
    """Response schema for scrape operations."""

    success: bool
    data: List[ProductData] = []
    error: Optional[str] = None
    request_id: Optional[str] = None
