import asyncio
from scrapers.flipkart_scraper import scrape_flipkart

query = input("Enter product name: ").strip()
output_format = input("Enter output format (csv/txt/json): ").strip().lower()
num_pages = input("Enter number of pages to scrape (leave blank for default): ").strip()

try:
    num_pages = int(num_pages) if num_pages else None
except ValueError:
    print("Invalid number, using default pages.")
    num_pages = None

asyncio.run(scrape_flipkart(query, output_format, num_pages))
