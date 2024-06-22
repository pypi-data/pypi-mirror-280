from . import config
from typing import List
import numpy as np


def get_all_markets() -> np.ndarray:
    """
    Fetch all markets and return their symbols as a numpy array.

    Returns:
        np.ndarray: An array of market symbols.
    """
    list_markets = np.array(config.EXCH.fetch_markets())
    list_symbols = [market['symbol'] for market in list_markets]
    return list_symbols  # Return a list instead of an np.array


class Coin:
    """
    This class is the decision maker for solely Burak Civitcioglu.
    The class is written by him and licensed under his use only.

    Attributes:
        name (str): The name of the coin.
    """
    
    def __init__(self, coin_name: str):
        """
        Initializes the Coin with a given name.

        Args:
            coin_name (str): The name of the coin.
        """
        self.name = coin_name
    
    def get_markets(self, print_market: bool = False) -> np.ndarray:
        """
        Get the markets that include the coin's name.

        Args:
            print_market (bool, optional): If True, prints each market. Defaults to False.

        Returns:
            np.ndarray: An array of markets that include the coin's name.
        """
        m2r = [market for market in config.MARKETS if self.name in market]
        if print_market:
            for market in m2r:
                print(market)
        return m2r  # Ensure this returns a list
