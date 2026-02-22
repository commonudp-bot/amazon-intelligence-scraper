# Amazon Intelligence Scraper

Production-ready Amazon scraping system designed for market research, competitor monitoring, and e-commerce intelligence.

Built with scalability, anti-blocking strategies, and API access in mind.

---

## 🚀 Features

- **Extract product data:**
  - Title
  - Price
  - Rating
  - Review count
  - ASIN
  - Seller
  - Availability

- **Anti-blocking strategies:**
  - Proxy rotation support
  - User-agent rotation
  - Retry with exponential backoff
  - CAPTCHA detection
  - Playwright fallback for blocked pages

- **Data export:**
  - JSON export
  - CSV export
  - Database storage (SQLite/PostgreSQL)

- **API & Deployment:**
  - FastAPI REST API
  - Docker support
  - Production-ready configuration

- **Architecture:**
  - Modular and scalable
  - Async/await support
  - Comprehensive logging

---

## 🧩 Use Cases

### E-commerce sellers
- Monitor competitor pricing
- Track rating changes
- Identify market gaps

### Market research teams
- Category trend analysis
- Brand share monitoring
- Price trend forecasting

### Dropshipping businesses
- Product research automation
- Profit margin analysis
- Inventory monitoring

---

## 🏗 Project Structure

```
amazon-intelligence-scraper/
│
├── app/                        # API layer
│   ├── main.py                 # FastAPI entry point
│   ├── routes.py               # API endpoints
│   ├── schemas.py              # Request/response models
│
├── scraper/                    # Scraping logic
│   ├── amazon_scraper.py       # Orchestrator
│   ├── parsers.py              # HTML parsing
│   ├── playwright_fallback.py  # JS-render fallback
│   ├── captcha_detector.py     # CAPTCHA detection
│
├── network/                    # Request handling
│   ├── proxy_manager.py        # Proxy rotation
│   ├── user_agent.py           # User-agent rotation
│   ├── retry.py                # Retry with backoff
│   ├── session.py              # Reusable session config
│
├── storage/                    # Data persistence
│   ├── exporter.py             # JSON/CSV export
│   ├── database.py             # SQLite/PostgreSQL support
│
├── core/                       # Shared utilities
│   ├── config.py               # Environment config
│   ├── logger.py               # Logging setup
│   ├── constants.py            # Selectors/constants
│
├── examples/                   # Usage examples
│   ├── scrape_product.py
│   ├── scrape_search.py
│
├── tests/                      # Unit tests
│   ├── test_parsers.py
│   ├── test_scraper.py
│
├── docker/                     # Deployment configs
│   ├── Dockerfile
│   ├── docker-compose.yml
│
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

### Prerequisites
- Python 3.9+
- pip or conda
- Docker (optional, for containerized deployment)

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/amazon-intelligence-scraper.git
cd amazon-intelligence-scraper
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your configuration
```

5. **Install Playwright browsers (for JavaScript-heavy pages):**
```bash
playwright install chromium
```

---

## 🚀 Quick Start

### Using the API

1. **Start the FastAPI server:**
```bash
python -m uvicorn app.main:app --reload
```

2. **Access the API documentation:**
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

3. **Example API calls:**
```bash
# Search for products
curl -X POST "http://localhost:8000/api/v1/search" \
  -H "Content-Type: application/json" \
  -d '{"query": "laptop", "page": 1}'

# Get product details
curl -X POST "http://localhost:8000/api/v1/product" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B07PYLT6DN"}'
```

### Using the Library Directly

**Search products:**
```python
import asyncio
from scraper.amazon_scraper import AmazonScraper

async def search():
    scraper = AmazonScraper()
    results = await scraper.search_products("laptop")
    return results

asyncio.run(search())
```

**Get product details:**
```python
import asyncio
from scraper.amazon_scraper import AmazonScraper

async def get_details():
    scraper = AmazonScraper()
    product = await scraper.get_product_details("B07PYLT6DN")
    return product

asyncio.run(get_details())
```

---

## 🐳 Docker Deployment

### Quick Start with Docker Compose

```bash
# Build and start the services
docker-compose -f docker/docker-compose.yml up -d

# Check logs
docker-compose -f docker/docker-compose.yml logs -f api

# Stop services
docker-compose -f docker/docker-compose.yml down
```

### Build Docker Image Manually

```bash
docker build -f docker/Dockerfile -t amazon-scraper:latest .
docker run -p 8000:8000 -e DEBUG=false amazon-scraper:latest
```

---

## 🔧 Configuration

### Environment Variables

Key configuration options in `.env`:

| Variable | Default | Description |
|----------|---------|-------------|
| `API_HOST` | 0.0.0.0 | API server host |
| `API_PORT` | 8000 | API server port |
| `DEBUG` | false | Debug mode |
| `REQUEST_TIMEOUT` | 30 | Request timeout in seconds |
| `MAX_RETRIES` | 3 | Maximum retry attempts |
| `PROXY_LIST` | (empty) | Comma-separated proxy URLs |
| `DATABASE_URL` | sqlite:///./data/amazon.db | Database connection URL |
| `LOG_LEVEL` | INFO | Logging level |

### Proxy Configuration

```env
# Single proxy
PROXY_LIST=http://proxy.example.com:8080

# Multiple proxies (comma-separated)
PROXY_LIST=http://proxy1.com:8080,http://proxy2.com:8080,socks5://proxy3.com:1080

# Enable proxy rotation
USE_PROXY_ROTATION=true
```

### Database Configuration

**SQLite (default):**
```env
DATABASE_URL=sqlite:///./data/amazon.db
```

**PostgreSQL:**
```env
DATABASE_URL=postgresql://user:password@localhost:5432/amazon
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=. --cov-report=html

# Run specific test file
pytest tests/test_scraper.py

# Run with verbose output
pytest -v
```

---

## 📊 API Endpoints

### Search Products
- **Endpoint:** `POST /api/v1/search`
- **Request:**
```json
{
  "query": "laptop",
  "page": 1,
  "timeout": 30,
  "headless": true
}
```
- **Response:**
```json
{
  "success": true,
  "data": [
    {
      "title": "Dell XPS 13",
      "asin": "B07PYLT6DN",
      "price": 999.99,
      "rating": 4.5,
      "review_count": 1250,
      "seller": "Amazon",
      "availability": "In Stock",
      "url": "https://amazon.com/dp/B07PYLT6DN"
    }
  ],
  "error": null
}
```

### Get Product Details
- **Endpoint:** `POST /api/v1/product`
- **Request:**
```json
{
  "asin": "B07PYLT6DN",
  "timeout": 30,
  "headless": true
}
```
- **Response:** Same format as search results

### Check Status
- **Endpoint:** `GET /api/v1/status`
- **Response:**
```json
{
  "status": "operational",
  "requests_made": 150,
  "blocked_count": 2,
  "captcha_detected": 1
}
```

---

## ⚠️ Important Notes

### Legal and Ethical Considerations

- **Terms of Service:** This tool should only be used in accordance with Amazon's Terms of Service
- **Robots.txt:** Respect Amazon's `robots.txt` and rate limits
- **Rate Limiting:** Implement appropriate delays between requests
- **User-Agent Rotation:** Always use realistic user-agents
- **CAPTCHA Handling:** Do not attempt to bypass CAPTCHAs programmatically

### Rate Limiting Best Practices

1. **Implement delays** between requests (minimum 0.5-1 second)
2. **Rotate proxies** to distribute load
3. **Monitor for blocks** and back off gracefully
4. **Use headless browsing** for complex interactions

### Handling CAPTCHA

The scraper includes CAPTCHA detection but **cannot bypass** Amazon's security measures. When a CAPTCHA is detected:

1. The scraper logs a warning
2. Falls back to Playwright if configured
3. Waits and retries after a delay
4. Returns an error if unable to proceed

---

## 🔍 Examples

### Example 1: Search and Export

```python
import asyncio
from scraper.amazon_scraper import AmazonScraper
from storage.exporter import DataExporter

async def search_and_export():
    scraper = AmazonScraper()
    products = await scraper.search_products("gaming laptop", page=1)
    
    exporter = DataExporter()
    exporter.export_json(products, "output/results.json")
    exporter.export_csv(products, "output/results.csv")

asyncio.run(search_and_export())
```

### Example 2: Monitor Product Prices

```python
import asyncio
from scraper.amazon_scraper import AmazonScraper
from storage.database import DatabaseManager

async def monitor_prices():
    scraper = AmazonScraper()
    db = DatabaseManager("sqlite:///./data/amazon.db")
    
    asins = ["B07PYLT6DN", "B08H2FBNSN"]
    for asin in asins:
        product = await scraper.get_product_details(asin)
        db.insert_products([product])
    
    db.close()

asyncio.run(monitor_prices())
```

---

## 📈 Performance Tips

1. **Use connection pooling** for database operations
2. **Implement caching** for frequently accessed data
3. **Use async operations** for concurrent requests
4. **Monitor memory usage** for long-running processes
5. **Enable logging** to track performance issues

---

## 🐛 Troubleshooting

### Common Issues

**Issue: CAPTCHA detected**
- Solution: Use proxy rotation, increase delays, or switch to Playwright fallback

**Issue: Connection timeout**
- Solution: Increase `REQUEST_TIMEOUT`, check proxy connectivity

**Issue: Import errors**
- Solution: Ensure all dependencies are installed: `pip install -r requirements.txt`

**Issue: Playwright errors**
- Solution: Install browsers: `playwright install chromium`

---

## 📝 Logging

View logs in real-time during development:

```python
from core.logger import setup_logging

logger = setup_logging(__name__)
logger.info("Starting scraper...")
logger.warning("CAPTCHA detected")
logger.error("Failed to fetch page")
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write tests
5. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Disclaimer

This tool is provided for educational and research purposes. Users are responsible for:

- Complying with Amazon's Terms of Service
- Respecting rate limits and robots.txt
- Using the tool ethically and legally
- Being aware of potential legal implications

The authors are not responsible for misuse of this tool.

---

## 📞 Support

For issues, questions, or suggestions:

1. Check the [Issues](https://github.com/yourusername/amazon-intelligence-scraper/issues) page
2. Create a detailed bug report
3. Include logs and configuration details
4. Provide steps to reproduce

---

## 🔄 Changelog

### v1.0.0 (Initial Release)
- Core scraping functionality
- API endpoints
- Proxy and user-agent rotation
- CAPTCHA detection
- Export to JSON/CSV
- Docker support
- Comprehensive documentation

---

**Built with ❤️ for intelligent web scraping**
