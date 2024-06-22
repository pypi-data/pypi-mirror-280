import unittest
from microcrypta.coin import Coin
from microcrypta.coinmarket import CoinMarket
from microcrypta.backtest import Backtest
from microcrypta.bsh import BSH
import numpy as np

class TestBacktest(unittest.TestCase):

    def setUp(self):
        coin = Coin("BTC")
        counter_coin = Coin("USDT")
        market = CoinMarket(coin, counter_coin, "1h")
        self.bsh = BSH(market)
        self.signal = self.bsh.moving_average(short_window=5, long_window=10)
        self.backtest = Backtest(market, self.signal, "Moving Average")

    def test_backtest(self):
        position_size, coin_count, percent_gain = self.backtest.backtest(plot=False)
        self.assertIsInstance(position_size, np.ndarray)
        self.assertIsInstance(coin_count, np.ndarray)
        self.assertIsInstance(percent_gain, float)

if __name__ == "__main__":
    unittest.main()
