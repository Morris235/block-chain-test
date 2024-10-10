import datetime

from fastapi import APIRouter

from api.v1.client import binance_client
from models.deposit_model import DepositModel

router: APIRouter = APIRouter()

client = binance_client()

# 클라이언트의 코인 지갑은 50개
# FIXME: An error occurred: APIError(code=-4093): Deposit for this coin and network has been disabled.
# 요청 제한 사항
# 바이낸스 API : 초당 1200건 (엔드포인트마다 상이할수 있음)
# IP 기반 제한 : 특정 IP 주소에서 요청을 초과할 경우, 해당 IP는 일시적으로 차단될 수 있다.
@router.get("/api/deposit/inquire", tags=["Deposit"])
async def get_deposit_address(symbol: str):
    try:
        deposit_address = client.get_deposit_address(coin=symbol)
        if deposit_address.get('tag'):
            print(f"Deposit tag: {deposit_address['tag']}")
        return {"coin_code" : symbol, "deposit_url" : deposit_address['address']}
    except Exception as e:
        print(f"An error occurred: {e}")

#FIXME: 기간 설정 파라미터로 받기, 테스트 편의상 하드코딩됨
@router.get("/api/deposit/history", tags=["Deposit"])
async def get_deposit_history():
    # 입금 내역 조회 (기간 설정)
    start_time = datetime.datetime(2024, 9, 1)
    start_timestamp = int(start_time.timestamp() * 1000)
    deposit_history_list = []
    try:
        deposits = client.get_deposit_history(startTime=start_timestamp)
        for deposit in deposits:
            deposit_history_list.append(deposit)
        return deposit_history_list
    except Exception as e:
        print(f"An error occurred: {e}")