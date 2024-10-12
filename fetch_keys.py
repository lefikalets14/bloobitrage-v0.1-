import json

def fetch_keys(exchange):
    with open('api_keys.json') as f:
        keys = json.load(f)
    return keys.get(exchange)

if __name__ == "__main__":
    exchange = input("Enter the exchange name: ").lower()
    keys = fetch_keys(exchange)
    if keys:
        print(f"API Key: {keys['api_key']}")
        print(f"API Secret: {keys['api_secret']}")
    else:
        print("Exchange not found.")
