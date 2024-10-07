# This is a sample Python script.
import hashlib
import hmac
import os
import time
from contextlib import asynccontextmanager
from http.client import HTTPException

import httpx
from fastapi import FastAPI
from dotenv import load_dotenv
import ccxt

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

@asynccontextmanager
async def lifespan(app: FastAPI):
    # response_get_websocket()
    # key = load_websocket_file()
    print(f'start server')
    yield
    print(f'stop server')

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

app = FastAPI(title="block_chain_test", version="0.0.1", lifespan=lifespan, debug=True)

binance = ccxt.binance(config={
    'apiKey': API_KEY,
    'secret': API_SECRET
})

BASE_URL = "https://api.binance.com/api/v3"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/api-check")
async def read_root():
    return {"API Key": API_KEY, "API Secret": API_SECRET}

@app.get("/api/check/account")
async def check_account():
    balance = binance.fetch_balance()
    return balance

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
