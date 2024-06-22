import unittest
from microcrypta.coin import Coin
from microcrypta.coinmarket import CoinMarket
import pandas as pd 

class TestCoinMarket(unittest.TestCase):

    def setUp(self):
        self.coin = Coin("BTC")
        self.counter_coin = Coin("USDT")
        self.market = CoinMarket(self.coin, self.counter_coin, "1h")

    def test_initialization(self):
        self.assertEqual(self.market.coin, self.coin)
        self.assertEqual(self.market.counter_coin, self.counter_coin)
        self.assertEqual(self.market.time_frame, "1h")

    def test_moving_average(self):
        ma = self.market.moving_average(window=5, ma_type='simple', price_type='close', plot=False)
        self.assertIsInstance(ma, pd.Series)

if __name__ == "__main__":
    unittest.main()
