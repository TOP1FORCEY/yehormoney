import requests

def crypto_price():
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=dogecoin&vs_currencies=usd"
    price = requests.get(url)
    data = price.json()

    return round((data["dogecoin"]["usd"] - 0.3825) * 2000, 3)

if __name__ == "__main__":
    main()