import os

from binance.client import Client
from dotenv import load_dotenv


def binance_client() -> Client:
    load_dotenv()
    api_key: str = os.getenv("BINANCE_API_KEY")
    api_secret: str = os.getenv("BINANCE_API_SECRET")
    client: Client = Client(api_key, api_secret)
    return client