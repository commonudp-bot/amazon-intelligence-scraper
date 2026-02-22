import asyncio
import os

from scraper.amazon_scraper import AmazonScraper
from storage.exporter import DataExporter


async def run():
    query = "bluetooth speaker"

    print(f"🔎 Searching for: {query}")

    scraper = AmazonScraper()
    products = await scraper.search_products(query, page=1)

    # Debug print
    print(f"Found {len(products)} products")

    if not products:
        print("❌ No data to export")
        return

    # Ensure output folder exists
    os.makedirs("output", exist_ok=True)

    exporter = DataExporter()
    exporter.export_json(products, "output/results.json")
    exporter.export_csv(products, "output/results.csv")

    print("✅ Export completed!")
    print("📁 Files created:")
    print("   - output/results.json")
    print("   - output/results.csv")


if __name__ == "__main__":
    asyncio.run(run())