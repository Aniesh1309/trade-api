import mockdata

from fastapi import FastAPI
from datetime import datetime
from schema import Trade
from django.core.paginator import Paginator

tags_metadata = [
    {
        "name": "Bonus",
        "description": "Implement support for pagination and sorting on the list of trades."
    }
]

app = FastAPI(
    title="Trade APIS",
    version="0.0.1",
    contact={
        "name": "Aniesh Thakkar",
        "url": "https://github.com/Aniesh1309/trade-api",
        "email": "anieshthakkar13@gmail.com",
    },
    openapi_tags=tags_metadata
)

@app.get("/trades",response_model=list[Trade], tags=[None])
async def listing_trades():
    return [*mockdata.MOCK_TRADE_DATABASE.values()]

@app.get("/trade/{trade_id}",response_model=Trade, tags=[None])
async def single_trade(trade_id):
    return mockdata.MOCK_TRADE_DATABASE[trade_id]

@app.get("/search",response_model=list[Trade], tags=[None])
async def searching_trades(search_param : str):
    SEARCHER_MOCK_DATA={}
    for trade_data in mockdata.MOCK_TRADE_DATABASE.values():
        if trade_data.counterparty==search_param or trade_data.instrument_id==search_param or trade_data.instrument_name==search_param or trade_data.trader==search_param:
            SEARCHER_MOCK_DATA[trade_data.trade_id] = trade_data
    return [*SEARCHER_MOCK_DATA.values()]

@app.get("/advancesearch",response_model=list[Trade], tags=[None])
async def advance_searching(assetClass: str | None = None, end: datetime | None = None, maxPrice: float | None = None, minPrice: float | None = None, start: datetime | None = None, tradeType: str | None = None):
    SEARCHER_MOCK_DATA=mockdata.MOCK_TRADE_DATABASE
    if assetClass is not None:
        SEARCHER_MOCK_DATA = {k:v for k,v in SEARCHER_MOCK_DATA.items() if v.asset_class==assetClass}
    if tradeType is not None:
        SEARCHER_MOCK_DATA = {k:v for k,v in SEARCHER_MOCK_DATA.items() if v.trade_details.buySellIndicator==tradeType}
    if maxPrice is not None:
        SEARCHER_MOCK_DATA = {k:v for k,v in SEARCHER_MOCK_DATA.items() if v.trade_details.price<=maxPrice}
    if minPrice is not None:
        SEARCHER_MOCK_DATA = {k:v for k,v in SEARCHER_MOCK_DATA.items() if v.trade_details.price>=minPrice}
    if end is not None:
        SEARCHER_MOCK_DATA = {k:v for k,v in SEARCHER_MOCK_DATA.items() if v.trade_date_time<=end}
    if start is not None:
        SEARCHER_MOCK_DATA = {k:v for k,v in SEARCHER_MOCK_DATA.items() if v.trade_date_time>=start}
    return [*SEARCHER_MOCK_DATA.values()]

@app.get("/trades/paginate", response_model=list[Trade], tags=["Bonus"])
async def paginate_trading_list(per_page: int, page_num: int):
    paginator = Paginator([*mockdata.MOCK_TRADE_DATABASE.values()], per_page)
    page_obj = paginator.get_page(page_num)
    return page_obj.object_list

@app.get("/trades/sort", response_model=list[Trade], tags=["Bonus"])
async def sort_trading_list():
    sortedData = sorted(mockdata.MOCK_TRADE_DATABASE.items(), key=lambda x: x[1].trade_id)
    return [*dict(sortedData).values()]