import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500

def getDataPoint(quote):
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2  # Calculate an average price
    return stock, bid_price, ask_price, price

def getRatio(price_a, price_b):
    if price_b == 0:
        return 0  # Avoid division by zero
    return price_a / price_b

# Main
if __name__ == "__main__":
    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())
        
        # Get and print each quote's data
        for quote in quotes:
            stock, bid_price, ask_price, price = getDataPoint(quote)
            print("Quoted %s at (bid:%s, ask:%s, price:%s)" % (stock, bid_price, ask_price, price))
        
        # Calculate and print the ratio of the last quote's price to itself
        last_quote = quotes[-1]
        stock, bid_price, ask_price, price = getDataPoint(last_quote)
        ratio = getRatio(price, price)
        print("Ratio %s" % ratio)
