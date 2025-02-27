import time
import logging
from functools import wraps

import random
from config import USER_AGENTS

def get_random_user_agent():
    """Returns a random user-agent string."""
    return random.choice(USER_AGENTS)

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def retry_on_failure(retries=3, delay=2):
    """Decorator to retry a function on failure (useful for requests)."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    logging.warning(f"Error: {e}. Retrying ({attempts+1}/{retries})...")
                    time.sleep(delay)
                    attempts += 1
            logging.error("Max retries reached. Function failed.")
            return None
        return wrapper
    return decorator

def clean_text(text):
    """Cleans and formats extracted text."""
    return text.strip().replace("\n", " ").replace("\t", " ") if text else "N/A"
