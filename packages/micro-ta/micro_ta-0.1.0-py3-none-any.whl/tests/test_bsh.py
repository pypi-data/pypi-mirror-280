import unittest
from micro_ta.coin import Coin
from micro_ta.coinmarket import CoinMarket
from micro_ta.bsh import BSH
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
