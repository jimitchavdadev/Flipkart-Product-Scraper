import asyncio
import tkinter as tk
from tkinter import ttk, messagebox
from scrapers.flipkart_scraper import scrape_flipkart

def search_flipkart():
    query = entry.get().strip()
    output_format = format_var.get()
    max_pages = pages_entry.get().strip()

    if not query:
        messagebox.showwarning("Input Error", "Please enter a search query!")
        return

    try:
        max_pages = int(max_pages) if max_pages else None  # Convert input to int, allow default
    except ValueError:
        messagebox.showwarning("Input Error", "Number of pages must be a valid number!")
        return

    search_btn.config(state=tk.DISABLED)  # Disable button to prevent multiple clicks

    async def run_scraper():
        results = await scrape_flipkart(query, output_format, max_pages)

        # ✅ Check if first page has products
        if not results or len(results) == 0:
            root.after(0, lambda: messagebox.showinfo("No Results", "No products found."))
            root.after(0, lambda: search_btn.config(state=tk.NORMAL))  # Re-enable button
            return  # Stop further execution

        # ✅ Display "All Products Found" only after successful scraping
        root.after(0, lambda: update_ui(results))
        root.after(0, lambda: messagebox.showinfo("Success", "All products found."))

    asyncio.run(run_scraper())  # Run scraper synchronously

def update_ui(results):
    """Updates the UI with scraped results."""
    search_btn.config(state=tk.NORMAL)  # Re-enable button

    text_output.delete(1.0, tk.END)
    for i, product in enumerate(results, 1):
        text_output.insert(tk.END, f"{i}. {product['Product']}\n")
        text_output.insert(tk.END, f"   Price  : {product['Price']}\n")
        text_output.insert(tk.END, f"   Rating : {product['Rating']}\n")
        text_output.insert(tk.END, "-" * 50 + "\n")  # Separator for readability

# GUI Setup
root = tk.Tk()
root.title("Flipkart Scraper")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

ttk.Label(frame, text="Enter product name:").grid(row=0, column=0, sticky=tk.W)
entry = ttk.Entry(frame, width=30)
entry.grid(row=0, column=1)

ttk.Label(frame, text="Number of pages:").grid(row=1, column=0, sticky=tk.W)
pages_entry = ttk.Entry(frame, width=10)
pages_entry.grid(row=1, column=1)

ttk.Label(frame, text="Select format:").grid(row=2, column=0, sticky=tk.W)
format_var = tk.StringVar(value="csv")
format_menu = ttk.Combobox(frame, textvariable=format_var, values=("csv", "txt", "json"))
format_menu.grid(row=2, column=1)

search_btn = ttk.Button(frame, text="Search", command=search_flipkart)
search_btn.grid(row=3, column=0, columnspan=2)

text_output = tk.Text(root, height=15, width=60)
text_output.grid(row=4, column=0)

root.mainloop()
