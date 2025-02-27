# Flipkart-Product-Scraper

Flipkart Product Scraper 🛒✨ – A Python-based web scraper to extract product details from Flipkart, including name, price, and rating. Supports CSV, JSON, and TXT export. Features a CLI &amp; GUI (Tkinter) for user-friendly interaction. Built with asyncio &amp; BeautifulSoup for efficient scraping. 🚀 #Flipkart #WebScraping #Python

# Flipkart Product Scraper 🛒✨

## Overview

Flipkart Product Scraper is a Python-based web scraping tool that extracts product details (name, price, and rating) from Flipkart. It supports multiple output formats (CSV, JSON, TXT) and includes both **CLI and GUI interfaces** for ease of use.

This project is built using `asyncio` and `BeautifulSoup` for efficient data extraction.

## Features 🚀

✅ **Scrapes product details** (name, price, rating) from Flipkart.  
✅ **Supports multiple formats** (CSV, JSON, TXT).  
✅ **GUI (Tkinter) and CLI support** for easy interaction.  
✅ **Handles pagination** for multiple pages.  
✅ **Uses asynchronous requests** (`aiohttp`) for fast scraping.  
✅ **Random User-Agent rotation** for better request handling.  
✅ **Error handling & logging** for smooth execution.

---

## Installation 🛠️

### Prerequisites:

Ensure you have Python 3.7+ installed on your system.

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/flipkart-product-scraper.git
cd flipkart-product-scraper
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage 🖥️

### 1️⃣ **CLI Mode**

Run the scraper via the command line:

```bash
python cli.py
```

- Enter the **product name**.
- Choose the **output format** (csv/txt/json).
- Specify the **number of pages** to scrape (or press Enter for default).

### 2️⃣ **GUI Mode**

Launch the graphical interface:

```bash
python gui.py
```

- Enter the **product name**.
- Select **output format**.
- Specify **number of pages** (optional).
- Click `Search` to start scraping.

### 3️⃣ **Main Script Execution**

You can also run `main.py` directly:

```bash
python main.py
```

---

## Project Structure 📂

```
flipkart-product-scraper/
│── scrapers/
│   ├── flipkart_scraper.py  # Main scraping logic
│── parser.py                 # Parses Flipkart product pages
│── scraper.py                # Handles HTTP requests
│── storage.py                # Saves data in CSV/JSON/TXT
│── config.py                 # Stores User-Agents & Base URL
│── gui.py                    # Tkinter-based GUI
│── cli.py                    # Command Line Interface
│── main.py                   # Entry script for scraping
│── utils.py                   # Helper functions & error handling
│── requirements.txt           # Dependencies list
│── README.md                 # Project Documentation
```

---

## Example Output 📊

### **Sample JSON Output**

```json
[
  {
    "Product": "Samsung Galaxy S23",
    "Price": "₹79,999",
    "Rating": "4.5"
  },
  {
    "Product": "iPhone 15 Pro",
    "Price": "₹1,29,999",
    "Rating": "4.7"
  }
]
```

### **Sample CSV Output**

```csv
Product Name, Price, Rating
Samsung Galaxy S23, ₹79,999, 4.5
iPhone 15 Pro, ₹1,29,999, 4.7
```

---

## Contributing 🤝

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m "Add new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a **Pull Request**.

---

## Disclaimer ⚠️

This project is for **educational purposes only**. Scraping e-commerce sites may violate their terms of service. Use responsibly.

---

## Contact 📩

Have questions or feedback? Reach out via GitHub Issues!
