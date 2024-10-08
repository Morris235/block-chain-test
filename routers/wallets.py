from fastapi import APIRouter

from api.v1.client import client_info

router: APIRouter = APIRouter()

@router.get("/api/wallet/spot", tags=["wallet"])
async def get_wallet_spot():
    try:
        coin_list = []
        for balance in client_info().get_account()['balances']:
            asset = balance['asset']
            free_amount = balance['free']
            locked_amount = balance['locked']
            coin_list.append({"Asset": asset, "Free": free_amount, "Locked": locked_amount})
        return coin_list
    except Exception as e:
        print(f"An error occurred: {e}")

@router.get("/api/wallet/margin", tags=["wallet"])
async def get_wallet_margin():
    try:
        margin_info = client_info().get_margin_account()
        coin_list = []
        for asset in margin_info['userAssets']:
            coin_list.append({"Asset": asset['asset'], "Free": asset['free'], "Borrowed": asset['borrowed'], "Interest": asset['interest']})
        return coin_list
    except Exception as e:
        print(f"An error occurred: {e}")
