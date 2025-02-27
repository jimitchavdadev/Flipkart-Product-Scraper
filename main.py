import asyncio
from scrapers.flipkart_scraper import scrape_flipkart

def main():
    query = input("Enter product name: ").strip()
    if not query:
        print("Error: Please enter a valid search query.")
        return

    output_format = input("Enter output format (csv/txt/json): ").strip().lower()
    if output_format not in ["csv", "txt", "json"]:
        print("Invalid format. Defaulting to CSV.")
        output_format = "csv"

    num_pages = input("Enter number of pages to scrape (leave blank for default): ").strip()

    try:
        num_pages = int(num_pages) if num_pages else None  # Convert to int, allow default
    except ValueError:
        print("Invalid input. Using default number of pages.")
        num_pages = None

    print("\nFetching data... Please wait.")

    results = asyncio.run(scrape_flipkart(query, output_format, num_pages))

    if not results:
        print("\nNo products found.")
    else:
        print("\nAll products found. Saved successfully.")

if __name__ == "__main__":
    main()
