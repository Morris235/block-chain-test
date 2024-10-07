# This is a sample Python script.
import os
import time
from contextlib import asynccontextmanager
from binance.client import Client
from fastapi import FastAPI
from dotenv import load_dotenv

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f'start server')
    yield
    print(f'stop server')

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

app = FastAPI(title="block_chain_test", version="0.0.1", lifespan=lifespan, debug=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

@app.get("/")
async def read_root():
    return {"message": "Hello World"}

@app.get("/api/key/check")
async def read_root():
    return {"API Key": API_KEY, "API Secret": API_SECRET}

@app.get("/api/account")
async def get_account_info():
    try:
        client = Client(API_KEY, API_SECRET)
        server_time = client.get_server_time()

        server_timestamp = server_time['serverTime']
        current_time = int(time.time() * 1000)

        print('Server timestamp:', server_timestamp)
        print('Current timestamp:', current_time)
        # account_info = await client.futures_account()
        # print(account_info)
        return client.get_account(timestamp=current_time)
    except Exception as e:
        print(e)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
