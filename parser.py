import asyncio
from bs4 import BeautifulSoup
from scraper import get_soup_async

async def num_of_pages(url: str) -> int:
    soup = await get_soup_async(url)
    if not soup:
        return 1  # Default to 1 page if failed

    pagination_div = soup.find('div', class_='_1G0WLw')
    if pagination_div:
        page_info = pagination_div.find('span')
        if page_info:
            return int(page_info.text.split()[-1])

    print("Pagination info not found, defaulting to 1 page.")
    return 1

async def parse_products(soup: BeautifulSoup):
    prices = soup.find_all('div', class_="Nx9bqj _4b5DiR")
    products = soup.find_all('div', class_='col col-7-12')

    extracted_products = []
    for product, price in zip(products, prices):
        title_tag = product.find('div', class_='KzDlHZ')
        title = title_tag.text.strip() if title_tag else "Title not found"
        price_text = price.text.strip() if price else "Price not found"
        extracted_products.append((title, price_text))

    return extracted_products
