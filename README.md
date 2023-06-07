# TRADE APIs

### Fetch All Trades
Returns all the trade items available.

```http
  GET /trades
```
---
### Fetch Single Trade
Returns specific trade item based on key provided.

```http
  GET /trades/${trade_id}
```
| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `trade_id`      | `string` | **Required**. Id of Trade Item |

---
### Searching Trades

Applied `for` loop on trade list and checked if the value paased in `search_param` query parameter exist in `counterparty`, `instrumentId`, `instrumentName`, `trader` for each trade item.
```http
  GET /search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `search_param`      | `string` | **Required**.  |

---

### Filtering Trades
The API recurssively filters the trade list with all the optional query parameters passed. If no URL parameters are passed the returns unfiltered list.

```http
  GET /advancesearch
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `assetClass`      | `string` | **Optional**. Asset class of the trade.|
| `end`      | `string` | **Optional**. The maximum date for the `tradeDateTime` field. |
| `maxPrice`      | `string` | **Optional**. The maximum value for the `tradeDetails.price` field. |
| `minPrice`      | `string` | **Optional**. The minimum value for the `tradeDetails.price` field. |
| `start`      | `string` | **Optional**. The minimum date for the `tradeDateTime` field. |
| `tradeType`      | `string` | **Optional**. The tradeDetails.buySellIndicator is a `BUY` or `SELL` |

---
### Pagination

Used django to implement Paginator.
```http
  GET /search
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `per_page`      | `string` | **Required**.  |
| `page_num`      | `string` | **Required**.  |

---
### Sorting

Used sorted function to sort the trade list based on `tradeId`
```http
  GET /sort
```
