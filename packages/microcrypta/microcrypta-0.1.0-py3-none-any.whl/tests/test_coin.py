import unittest
from microcrypta.coin import Coin

class TestCoin(unittest.TestCase):

    def test_coin_initialization(self):
        coin = Coin("BTC")
        self.assertEqual(coin.name, "BTC")

    def test_get_markets(self):
        coin = Coin("BTC")
        markets = coin.get_markets()
        self.assertIsInstance(markets, list)  # Ensure markets is a list

if __name__ == "__main__":
    unittest.main()
