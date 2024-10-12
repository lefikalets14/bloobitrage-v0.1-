import ccxt
import fetch_keys

def get_balance(exchange_name, currency):
    keys = fetch_keys.fetch_keys(exchange_name)
    if not keys:
        raise ValueError("Exchange not found or API keys missing.")

    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class({
        'apiKey': keys['api_key'],
        'secret': keys['api_secret'],
    })

    balance = exchange.fetch_balance()
    return balance['total'][currency]

def get_price(exchange_name, symbol):
    keys = fetch_keys.fetch_keys(exchange_name)
    if not keys:
        raise ValueError("Exchange not found or API keys missing.")

    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class({
        'apiKey': keys['api_key'],
        'secret': keys['api_secret'],
    })

    ticker = exchange.fetch_ticker(symbol)
    return ticker['last']

if __name__ == "__main__":
    exchange = input("Enter the exchange name: ").lower()
    currency = input("Enter the currency (e.g., USDT): ").upper()
    symbol = input("Enter the trading pair (e.g., SEI/USDT): ").upper()

    balance = get_balance(exchange, currency)
    price = get_price(exchange, symbol)

    print(f"Balance: {balance} {currency}")
    print(f"Current price of {symbol} on {exchange}: {price}")
