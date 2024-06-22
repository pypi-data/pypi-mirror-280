import unittest
from microcrypta.coin import Coin
from microcrypta.coinmarket import CoinMarket
from microcrypta.bsh import BSH
import pandas as pd

class TestBSH(unittest.TestCase):

    def setUp(self):
        coin = Coin("BTC")
        counter_coin = Coin("USDT")
        market = CoinMarket(coin, counter_coin, "1h")
        self.bsh = BSH(market)

    def test_moving_average(self):
        signal = self.bsh.moving_average(short_window=5, long_window=10)
        self.assertIsInstance(signal, pd.DataFrame)

if __name__ == "__main__":
    unittest.main()
