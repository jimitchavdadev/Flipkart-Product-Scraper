import asyncio
import csv
import json
import os
from bs4 import BeautifulSoup
from scraper import get_soup_async

async def get_num_of_pages(url: str) -> int:
    """Fetches the total number of pages available on Flipkart."""
    soup = await get_soup_async(url)
    if not soup:
        return 1  # Default to 1 page if failed

    pagination_div = soup.find('div', class_='_1G0WLw')
    if pagination_div:
        page_info = pagination_div.find('span')
        if page_info:
            try:
                return int(page_info.text.split()[-1])
            except ValueError:
                return 1  # Default to 1 if parsing fails

    return 1

async def parse_products(soup: BeautifulSoup):
    """Extracts product details from a Flipkart search page."""
    products = soup.find_all('div', class_='col col-7-12')
    prices = soup.find_all('div', class_="Nx9bqj _4b5DiR")
    ratings = soup.find_all('div', class_="XQDdHH")

    extracted_products = []
    for product, price, rating in zip(products, prices, ratings):
        title_tag = product.find('div', class_='KzDlHZ')
        title = title_tag.text.strip() if title_tag else "Title not found"
        price_text = price.text.strip() if price else "Price not found"
        rating_text = rating.text.strip() if rating else "No rating"

        extracted_products.append({
            "Product": title,
            "Price": price_text,
            "Rating": rating_text
        })

    return extracted_products

async def scrape_flipkart(query: str, output_format: str, max_pages: int = 5):
    """Scrapes Flipkart based on user query and saves results."""
    base_url = f"https://www.flipkart.com/search?q={query.replace(' ', '+')}"
    available_pages = await get_num_of_pages(base_url)

    # Validate number of pages
    max_pages = min(max_pages, available_pages) if max_pages else 5

    all_products = []
    for page in range(1, max_pages + 1):
        url = f"{base_url}&page={page}"
        soup = await get_soup_async(url)

        if not soup:
            continue

        products = await parse_products(soup)
        if products:
            all_products.extend(products)

    # Stop if no products found
    if not all_products:
        return None

    # Save the output
    output_folder = "output"
    os.makedirs(output_folder, exist_ok=True)
    filename = os.path.join(output_folder, f"{query}.{output_format}")

    if output_format == "csv":
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=["Product", "Price", "Rating"])
            writer.writeheader()
            writer.writerows(all_products)
    elif output_format == "json":
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(all_products, file, indent=4)
    else:  # txt
        with open(filename, "w", encoding="utf-8") as file:
            for product in all_products:
                file.write(f"Product: {product['Product']}\n")
                file.write(f"Price  : {product['Price']}\n")
                file.write(f"Rating : {product['Rating']}\n")
                file.write("-" * 50 + "\n")

    return all_products
