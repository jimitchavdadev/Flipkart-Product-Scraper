import aiohttp
from bs4 import BeautifulSoup

async def get_soup_async(url: str):
    """Fetches and returns a BeautifulSoup object asynchronously."""
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
    }
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status != 200:
                print(f"Failed to fetch {url}, Status Code: {response.status}")
                return None
            
            html = await response.text()
            return BeautifulSoup(html, 'html.parser')
