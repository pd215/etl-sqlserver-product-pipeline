import requests
import json
from utils.logger import get_logger

# ========================
# CONFIG
# ========================
URL = "https://dummyjson.com/products"
OUTPUT_FILE = "products_latest.json"

logger = get_logger()

# ========================
# EXTRACT FUNCTION
# ========================
def extract_data():
    try:
        logger.info("Starting data extraction...")

        response = requests.get(URL)

        if response.status_code != 200:
            raise Exception(f"API request failed: {response.status_code}")

        data = response.json()

        # validera struktur
        if "products" not in data:
            raise Exception("Invalid API response: 'products' key missing")

        # spara fil
        with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

        logger.info(f"Data saved to {OUTPUT_FILE}")
        print(f"Saved: {OUTPUT_FILE}")

    except Exception as e:
        logger.error(f"Extract failed: {e}")
        print(f"ERROR: {e}")


# ========================
# MAIN
# ========================
if __name__ == "__main__":
    extract_data()