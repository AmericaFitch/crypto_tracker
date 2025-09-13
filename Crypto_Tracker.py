import requests

URL = "https://api.coingecko.com/api/v3/simple/price"

class Coin:
    def __init__(self, name, symbol, currency = "USD"):
        self.name = name.lower()            # Name Of Our Coin
        self.symbol = symbol.upper()        # Symbol Of Our Symbol
        self.currency = currency.lower()
        self.price = None                   # The Price Must Be Filled Later Through The API

    def update_price(self):
        """To get the current price from CoinGecko API"""
        params = {  "ids": self.name,
                  "vs_currencies" : self.currency
        }
        response = requests.get(URL, params=params)
        data = response.json()
        if self.name in data:
            self.price = data[self.name][self.currency]


    def display(self):
        """Print out the Coins current price"""
        if self.price is not None:
            print(f"{self.name.capitalize()} ({self.symbol}) Price ({self.currency.upper()}): {self.price}")
        else:
            print(f"Price not available for {self.name}")

coin_id = input("Enter the cryptocurrency id (e.g., bitcoin, ethereum, solana): ")
symbol = input("Enter the symbol (e.g., BTC, ETH, SOL): ")

user_coin = Coin(coin_id, symbol)
user_coin.update_price()
user_coin.display()