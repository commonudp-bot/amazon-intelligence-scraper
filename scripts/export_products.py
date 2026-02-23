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

    # Export files
    exporter.export_json(products, "output/results.json")
    exporter.export_csv(products, "output/results.csv")
    exporter.export_excel(products, "output/results.xls")  # ✅ NEW

    print("✅ Export completed!")
    print("📁 Files created:")
    print("   - output/results.json")
    print("   - output/results.csv")
    print("   - output/results.xls")  # ✅ NEW


if __name__ == "__main__":
    asyncio.run(run())
