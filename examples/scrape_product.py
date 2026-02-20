"""Example: Scrape detailed information for a specific product."""

import asyncio
import logging
from scraper.amazon_scraper import AmazonScraper
from storage.exporter import DataExporter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Example usage of AmazonScraper for product details."""
    scraper = AmazonScraper()

    try:
        # Scrape a specific product by ASIN
        asin = "B07PYLT6DN"  # Example: Echo Dot
        logger.info(f"Fetching details for ASIN: {asin}")

        product_data = await scraper.get_product_details(asin)

        if product_data:
            logger.info(f"Successfully scraped product: {product_data.get('title')}")

            # Export to JSON
            exporter = DataExporter()
            exporter.export_json(
                [product_data],
                "output/product_details.json",
            )

            logger.info("Data exported to output/product_details.json")
        else:
            logger.warning("Failed to scrape product details")

    except Exception as e:
        logger.error(f"Error: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
