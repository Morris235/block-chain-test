from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import account, wallets, deposit


@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f'start server')
    yield
    print(f'stop server')

app = FastAPI(title="block_chain_test", version="0.0.1", lifespan=lifespan, debug=True)

app.include_router(account.router)
app.include_router(wallets.router)
app.include_router(deposit.router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}