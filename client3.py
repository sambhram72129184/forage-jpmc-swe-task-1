################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import json
import random
import urllib.request

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500 server request
N = 500


def getDataPoint(quote):
    """ Returns the tuple of stock name, bid_price, ask_price, and price. """
    stock = quote['stock']
    bid_price = float(quote['top_bid']['price'])
    ask_price = float(quote['top_ask']['price'])
    price = (bid_price + ask_price) / 2
    return stock, bid_price, ask_price, price


def getRatio(price_a, price_b):
    """ Returns the ratio of price_a and price_b. """
    return price_a / price_b


def main():
    stock_a_prices = []
    stock_b_prices = []

    # Query the price once every N seconds.
    for _ in iter(range(N)):
        quotes = json.loads(urllib.request.urlopen(QUERY.format(random.random())).read())

        stock_a_quote = next(quote for quote in quotes if quote['stock'] == 'ABC')
        stock_b_quote = next(quote for quote in quotes if quote['stock'] == 'DEF')

        stock_a_data = getDataPoint(stock_a_quote)
        stock_b_data = getDataPoint(stock_b_quote)
        ratio = getRatio(stock_a_data[3], stock_b_data[3])

        stock_a_prices.append(stock_a_data[3])
        stock_b_prices.append(stock_b_data[3])

        print("Stock A Info:", stock_a_data)
        print("Stock B Info:", stock_b_data)
        print("Ratio:", ratio)

    avg_stock_a_price = sum(stock_a_prices) / len(stock_a_prices)
    avg_stock_b_price = sum(stock_b_prices) / len(stock_b_prices)
    final_ratio = getRatio(avg_stock_a_price, avg_stock_b_price)

    print("Average Stock A Price:", avg_stock_a_price)
    print("Average Stock B Price:", avg_stock_b_price)
    print("Final Ratio:", final_ratio)


if __name__ == "__main__":
    main()
