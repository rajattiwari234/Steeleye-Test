import datetime as dt
from http.client import HTTPException
from fastapi import FastAPI
from typing import Union
from typing import Optional
from pydantic import BaseModel, Field

app = FastAPI()

class TradeDetails(BaseModel):
    buySellIndicator: str = Field(description="A value of BUY for buys, SELL for sells.")

    price: float = Field(description="The price of the Trade.")

    quantity: int = Field(description="The amount of units traded.")

class Trade(BaseModel):
    asset_class: Optional[str] = Field(alias="assetClass", default=None, description="The asset class of the instrument traded. E.g. Bond, Equity, FX...etc")

    counterparty: Optional[str] = Field(default=None, description="The counterparty the trade was executed with. May not always be available")

    instrument_id: str = Field(alias="instrumentId", description="The ISIN/ID of the instrument traded. E.g. TSLA, AAPL, AMZN...etc")

    instrument_name: str = Field(alias="instrumentName", description="The name of the instrument traded.")

    trade_date_time: dt.datetime = Field(alias="tradeDateTime", description="The date-time the Trade was executed")

    trade_details: TradeDetails = Field(alias="tradeDetails", description="The details of the trade, i.e. price, quantity")

    trade_id: str = Field(alias="tradeId", default=None, description="The unique ID of the trade")

    trader: str = Field(description="The name of the Trader")


trades = [
{"asset_class": "Equity", "counterparty": "Zerodha", "instrument_id": "AAPL", "instrument_name": "Stock", "trade_date_time": "11111111", "trade_details": "", "trade_id": "1111", "trader": "XXX", "buysellindicator": "BUY", "price": "123", "quantity": "22"},
{"asset_class":u "Equity", "counterparty": "Zerodha", "instrument_id": "AAPL", "instrument_name": "Stock", "trade_date_time": "11111111", "trade_details": "", "trade_id": "1234", "trader": "XXX", "buysellindicator": "BUY", "price": "123", "quantity": "22"},
]

@app.get("/trades/", response_model=list[Trade])
async def read_trades():
    return trades

@app.post("/trades/", response_model=Union[Trade, TradeDetails])
async def create_trade(asset_class: str, counterparty: str, instrument_id: str, instrument_name: str, trade_date_time: dt.datetime,  trade_details: TradeDetails, trade_id: str, trader: str):
    trades[trade_id] = Trade
    return trades[trade_id]

@app.get("/trades/{trade_id}")
async def read_item(trade_id):
    return {"trade_id": trade_id}