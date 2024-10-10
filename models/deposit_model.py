from datetime import datetime

from pydantic import BaseModel

class DepositModel(BaseModel):
    id: str
    amount: str
    coin: str
    network: str
    status: int
    address: str
    addressTag: str
    txId: str
    insertTime: datetime
    transferType: int
    confirmTimes: str
    unlockConfirm: int
    walletType: int

