import logging

from fastapi import APIRouter

from api.v1.client import binance_client

router: APIRouter = APIRouter()

client = binance_client()

# 고려사항
# 수수료 : 출금 시 바이낸스에서 수수료 발생
# 출금 한도 : 계정의 출금 한도와 관련된 규정 고려 필요. 출금 한도는 계정 인증 수준에 따라 달라짐
# 출금 상태 : 출금이 완료된 후 출금 상태를 확인해야 함
# FIXME : 2FA 인증 및 출금 제한 등 보안 관련 설정 필요 -> API management에서 Enable Withdrawals 체크
# TODO: 연결 끊어지는것에 대한 대비 코드가 반드시 필요하다.
@router.post("/api/withdrawal/order", tags=["Withdrawal"])
async def post_withdrawal_order(coin: str, amount: float, address: str, network=None) -> dict:
    try:
        response: dict = client.withdraw(
            coin=coin,
            address=address,
            amount=amount,
            network=network
        )
        print(response)
        return response
    except Exception as e:
        logging.info(e)

@router.get("/api/withdrawal/history", tags=["Withdrawal"])
async def get_withdrawal_history(asset: str) -> list:
    try:
        response: list = client.get_withdraw_history(asset=asset)
        return response
    except Exception as e:
        logging.info(e)