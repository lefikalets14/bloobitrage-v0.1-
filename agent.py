import ccxt
import fetch_keys
from order import execute_order

def deposit(exchange_name, currency, amount, address):
    keys = fetch_keys.fetch_keys(exchange_name)
    if not keys:
        raise ValueError("Exchange not found or API keys missing.")

    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class({
        'apiKey': keys['api_key'],
        'secret': keys['api_secret'],
    })

    transaction = exchange.withdraw(currency, amount, address)
    return transaction

def withdraw(exchange_name, currency, amount, address):
    keys = fetch_keys.fetch_keys(exchange_name)
    if not keys:
        raise ValueError("Exchange not found or API keys missing.")

    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class({
        'apiKey': keys['api_key'],
        'secret': keys['api_secret'],
    })

    transaction = exchange.withdraw(currency, amount, address)
    return transaction

if __name__ == "__main__":
    initial_exchange = 'binance'
    currency = 'USDT'
    buy_exchange = input("Enter the exchange to buy at: ").lower()
    sell_exchange = input("Enter the exchange to sell at: ").lower()
    symbol = input("Enter the trading pair (e.g., SEI/USDT): ").upper()
    amount = float(input("Enter the amount to trade: "))
    buy_address = input("Enter the deposit address for the buy exchange: ")
    sell_address = input("Enter the deposit address for the sell exchange: ")

    deposit(initial_exchange, currency, amount, buy_address)
    buy_order = execute_order(buy_exchange, symbol, 'buy', amount)
    print(f"Buy Order: {buy_order}")

    withdraw(buy_exchange, currency, amount, sell_address)
    sell_order = execute_order(sell_exchange, symbol, 'sell', amount)
    print(f"Sell Order: {sell_order}")

    deposit(sell_exchange, currency, amount, buy_address)
