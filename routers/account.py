from fastapi import APIRouter

from api.v1.client import client_info
from utils.server_time import api_server_time

router: APIRouter = APIRouter()

@router.get("/api/account/info", tags=["account"])
async def binance_account():
    try:
        account_info = client_info().get_account(timestamp=api_server_time())
        print(account_info)
        return account_info
    except Exception as e:
        print(f"An error occurred: {e}")