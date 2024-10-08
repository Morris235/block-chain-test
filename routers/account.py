from fastapi import APIRouter

from api.v1.client import binance_client
from utils.server_time import api_server_time

router: APIRouter = APIRouter()

# FIXME : binance_client는 singleton 적용
client = binance_client()

@router.get("/api/account/info", tags=["Account"])
async def get_binance_account():
    try:
        account_info = client.get_account(timestamp=api_server_time())
        return account_info
    except Exception as e:
        print(f"An error occurred: {e}")