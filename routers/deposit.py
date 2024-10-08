import datetime

from fastapi import APIRouter

from api.v1.client import client_info

router: APIRouter = APIRouter()

# # 클라이언트의 코인 지갑은 50개
@router.get("/api/deposit/all", tags=["deposit"])
async def get_deposit_address(symbol: str):
    try:
        deposit_address = client_info().get_deposit_address(coin=symbol)
        if deposit_address.get('tag'):
            print(f"Deposit tag: {deposit_address['tag']}")
        return {"coin_code" : symbol, "deposit_url" : deposit_address['address']}
    except Exception as e:
        print(f"An error occurred: {e}")

@router.get("/api/deposit/history", tags=["deposit"])
async def get_deposit_history():
    # 입금 내역 조회 (기간 설정)
    start_time = datetime.datetime(2024, 9, 1)
    start_timestamp = int(start_time.timestamp() * 1000)
    coin_list = []
    try:
        deposits = client_info().get_deposit_history(startTime=start_timestamp)
        for deposit in deposits:
            asset = deposit['asset']
            amount = deposit['amount']
            tx_id = deposit['txId']  # 입금의 고유한 ID 값
            status = deposit['status']
            timestamp = deposit['insertTime']
            coin_list.append({"Asset": asset, "Amount": amount, "TxID": tx_id, "Status": status, "Time": timestamp})
        return coin_list
    except Exception as e:
        print(f"An error occurred: {e}")