import requests

url = "https://api.freeapi.app/api/v1/public/stocks?page=1&limit=2&inc=Symbol%2CName%2CMarketCap%2CCurrentPrice&query=tata"

def fetch_stocks():
    response = requests.get(url).json()
    if response["success"] and "data" in response:
        stock_data = response["data"]
        total_items = stock_data["totalItems"]
        
        stock_list = []
        for stock in stock_data["data"]:
            symbol = stock["Symbol"]
            name = stock["Name"]
            market_cap = stock["MarketCap"]
            current_price = stock["CurrentPrice"]
            stock_dict = [{
                "symbol": symbol,
                "name": name,
                "market_cap": market_cap,
                "current_price": current_price
            }]
            stock_list.append(stock_dict)
        return total_items, stock_list
    else:
        raise Exception("Stock has been fallen down")

def main():
    try:
        total_items, stock_items = fetch_stocks()
        print(f"Total number of items in data are {total_items}")
        # print(stock_items)
        for stocks in stock_items:
            for stock in stocks:
                for key, value in stock.items():
                    print(f"{key}: {value}")
            print()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()