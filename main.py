from contextlib import asynccontextmanager
from fastapi import FastAPI

from models.deposit_model import DepositModel
from routers import account, wallets, deposit, withdrawal


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f'start server')
    yield
    print(f'stop server')

app = FastAPI(title="Block chain API test", version="0.0.1", lifespan=lifespan, debug=True)

# FIXME: 수동으로 트리거를 만들어서 사용해야함.
# FIXME: webhook을 이렇게 만드는건지 확실치 않음. 말이 webhook이지 바이낸스 API에서 입금 알림을 제공하지 않는다.
# FIXME: 따라서 결국엔 개발 API에서 입금을 수신해야 한다.
@app.post("/webhook/deposit", tags=["Webhook"])
async def deposit_webhook(request: DepositModel):
    """
    사용자 코인 입금시 작동
    """
    data = request.model_dump_json()
    return {"data" : data}

@app.post("/webhook/withdrawal", tags=["Webhook"])
async def withdrawal_webhook(request: DepositModel):
    """
    사용자 코인 입금시 작동
    """
    data = request.model_dump_json()
    return {"data" : data}

app.include_router(account.router)
app.include_router(wallets.router)
app.include_router(deposit.router)
app.include_router(withdrawal.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}