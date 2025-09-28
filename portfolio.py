import requests
import json

# Load portfolio from JSON file
with open("portfolio.json", "r") as f:
    portfolio = json.load(f)

# Fetch prices from CoinGecko API
ids = ",".join(portfolio.keys())
url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
response = requests.get(url).json()

# Calculate total value
total_value = 0
print("💰 Portfolio value:\n")
for coin, amount in portfolio.items():
    price = response[coin]["usd"]
    value = price * amount
    total_value += value
    print(f"{coin.upper()}: {amount} coins × ${price:.2f} = ${value:.2f}")

print(f"\nTOTAL: ${total_value:.2f}")
