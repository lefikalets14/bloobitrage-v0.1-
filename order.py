import ccxt
import fetch_keys

def execute_order(exchange_name, symbol, order_type):
    keys = fetch_keys.fetch_keys(exchange_name)
    if not keys:
        raise ValueError("Exchange not found or API keys missing.")

    exchange_class = getattr(ccxt, exchange_name)
    exchange = exchange_class({
        'apiKey': keys['api_key'],
        'secret': keys['api_secret'],
    })

    balance = exchange.fetch_balance()
    currency = symbol.split('/')[1] if order_type == 'buy' else symbol.split('/')[0]
    amount = balance['free'][currency]

    if order_type == 'buy':
        order = exchange.create_market_buy_order(symbol, amount)
    elif order_type == 'sell':
        order = exchange.create_market_sell_order(symbol, amount)
    else:
        raise ValueError("Invalid order type. Use 'buy' or 'sell'.")

    return order

if __name__ == "__main__":
    buy_exchange = input("Enter the exchange to buy at: ").lower()
    sell_exchange = input("Enter the exchange to sell at: ").lower()
    symbol = input("Enter the trading pair (e.g., SEI/USDT): ").upper()

    buy_order = execute_order(buy_exchange, symbol, 'buy')
    print(f"Buy Order: {buy_order}")

    sell_order = execute_order(sell_exchange, symbol, 'sell')
    print(f"Sell Order: {sell_order}")
