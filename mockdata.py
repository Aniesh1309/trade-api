from datetime import datetime
from schema import Trade, TradeDetails

MOCK_TRADE_DATABASE = {
    "511": Trade(
    assetClass="Bond",
    counterparty="XYZ Corp",
    instrumentId="TSLA",
    instrumentName="ABCD",
    tradeDateTime=datetime.strptime(f'1/1/2021', '%m/%d/%Y'),
    tradeDetails=TradeDetails(price=1000.0, quantity=10,buySellIndicator="Buy"),
    tradeId="511",
    trader="Bob Smith",
),
    "234": Trade(
    assetClass="Equity",
    instrumentId="TSLA",
    instrumentName="ABCD",
    tradeDateTime=datetime.strptime(f'6/6/2023', '%m/%d/%Y'),
    tradeDetails=TradeDetails(price=100.0, quantity=1,buySellIndicator="Sell"),
    tradeId="234",
    trader="Alice James",
),
    "323": Trade(
    assetClass="Fx",
    counterparty="ABC Corp",
    instrumentId="AAPL",
    instrumentName="XYZ",
    tradeDateTime=datetime.strptime(f'1/1/2022', '%m/%d/%Y'),
    tradeDetails=TradeDetails(price=1000.0, quantity=5,buySellIndicator="Buy"),
    tradeId="323",
    trader="Tim Cook",
),
}