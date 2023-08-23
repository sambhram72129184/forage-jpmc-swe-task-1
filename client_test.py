import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        stock_a_data = getDataPoint(quotes[0])
        stock_b_data = getDataPoint(quotes[1])

        self.assertEqual(stock_a_data, ('ABC', 120.48, 121.2, (120.48 + 121.2) / 2))
        self.assertEqual(stock_b_data, ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        stock_a_data = getDataPoint(quotes[0])
        stock_b_data = getDataPoint(quotes[1])

        self.assertEqual(stock_a_data, ('ABC', 120.48, 119.2, (120.48 + 119.2) / 2))
        self.assertEqual(stock_b_data, ('DEF', 117.87, 121.68, (117.87 + 121.68) / 2))

if __name__ == '__main__':
    unittest.main()
