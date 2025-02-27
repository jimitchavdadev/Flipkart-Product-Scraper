import json
import csv
import os

def save_to_json(data, filename="products.json"):
    """Saves product data to a JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename="products.csv"):
    """Saves product data to a CSV file."""
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Product Name", "Price"])
        writer.writerows(data)
    print(f"Data saved to {filename}")

def save_to_txt(data, filename="products.txt"):
    """Saves product data to a text file."""
    with open(filename, "w", encoding="utf-8") as file:
        for item in data:
            file.write(f"{item[0]} - {item[1]}\n")
    print(f"Data saved to {filename}")

def ensure_directory(directory="output"):
    """Creates a directory if it doesn't exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)
