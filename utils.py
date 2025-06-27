from dotenv import load_dotenv
import os

def load_credentials():
    load_dotenv()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API credentials not found in .env")

    return api_key, api_secret
