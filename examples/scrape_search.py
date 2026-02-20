"""Example: Search Amazon and scrape results."""

import asyncio
import logging
from scraper.amazon_scraper import AmazonScraper
from storage.exporter import DataExporter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    """Example usage of AmazonScraper for search results."""
    scraper = AmazonScraper()

    try:
        # Search for products
        query = "laptop"
        logger.info(f"Searching for: {query}")

        products = await scraper.search_products(query, page=1)

        if products:
            logger.info(f"Found {len(products)} products")

            # Export to both JSON and CSV
            exporter = DataExporter()
            exporter.export_json(products, "output/search_results.json")
            exporter.export_csv(products, "output/search_results.csv")

            logger.info("Results exported to output/")
        else:
            logger.warning("No products found")

    except Exception as e:
        logger.error(f"Error: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
