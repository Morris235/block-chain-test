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

@app.webhooks.post("new-subscription")
def new_subscription(body: DepositModel):
    """
    사용자 코인 입금시 작동
    """

app.include_router(account.router)
app.include_router(wallets.router)
app.include_router(deposit.router)
app.include_router(withdrawal.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}