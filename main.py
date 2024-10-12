import asyncio
import time
from fetch_keys import fetch_keys
from order import execute_order
from agent import deposit, withdraw
from monitor import get_balance, get_price

async def main():
    buy_exchange = input("Enter the exchange to buy at: ").lower()
    sell_exchange = input("Enter the exchange to sell at: ").lower()
    symbol = input("Enter the trading pair (e.g., SEI/USDT): ").upper()
    buy_address = input("Enter the deposit address for the buy exchange: ")
    sell_address = input("Enter the deposit address for the sell exchange: ")

    initial_exchange = 'binance'
    currency = symbol.split('/')[1]  # Use the quote currency for initial deposit

    # Initial deposit to buy exchange
    amount = get_balance(initial_exchange, currency)
    deposit(initial_exchange, currency, amount, buy_address)

    while True:
        try:
            # Check balance on buy exchange
            balance = get_balance(buy_exchange, currency)
            if balance < 1:  # Use a small threshold to avoid issues with very small balances
                print(f"Insufficient balance on {buy_exchange}.")
                break

            # Fetch current prices
            buy_price = get_price(buy_exchange, symbol)
            sell_price = get_price(sell_exchange, symbol)

            # Calculate potential profit
            profit_potential = ((sell_price - buy_price) / buy_price) * 100
            print(f"Current profit potential: {profit_potential:.2f}%")

            # Check if profit potential is greater than threshold (e.g., 0.5%)
            if profit_potential > 0.5:
                # Execute buy order
                buy_order = execute_order(buy_exchange, symbol, 'buy')
                print(f"Buy Order: {buy_order}")

                # Withdraw to sell exchange
                withdraw(buy_exchange, currency, balance, sell_address)

                # Execute sell order
                sell_order = execute_order(sell_exchange, symbol, 'sell')
                print(f"Sell Order: {sell_order}")

                # Withdraw back to initial exchange
                amount = get_balance(sell_exchange, currency)
                deposit(sell_exchange, currency, amount, buy_address)

            # Sleep for a while before checking again
            time.sleep(60)

        except Exception as e:
            print(f"Error: {str(e)}")
            break

if __name__ == "__main__":
    asyncio.run(main())
