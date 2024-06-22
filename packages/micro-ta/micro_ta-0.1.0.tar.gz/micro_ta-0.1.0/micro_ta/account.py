from .coinmarket import CoinMarket
from .coin import Coin
from tqdm import tqdm
import pandas as pd
import numpy as np
import seaborn as sns

def correlation_matrix(coins: list[str], time_frame: str = '4h', corr_method: str = 'spearman') -> None:
    """
    Generate a correlation matrix and volatility report for a list of coins.

    Args:
        coins (list[str]): List of coin names.
        time_frame (str, optional): Time frame for fetching market data. Defaults to '4h'.
        corr_method (str, optional): Method to compute correlation. Defaults to 'spearman'.
    """
    coin_len = len(coins)
    coins_return = pd.DataFrame()

    for i in tqdm(range(coin_len)):
        coin = Coin(coins[i])
        base_coin = Coin('USDT')

        coin_mark = CoinMarket(coin, base_coin, time_frame)
        coins_return[coin.name] = coin_mark.close
    
    coins_return = coins_return / coins_return.iloc[0, :]

    sns.heatmap(coins_return.corr(method=corr_method), annot=True, linewidths=0.5)
    daily_pct_change = coins_return.pct_change()
    volatility = round(np.log(daily_pct_change + 1).std() * np.sqrt(252), 5)
    for i in range(coin_len):
        print(f'{coins[i]} VOLATILITY: {volatility[i]}')

class Account:
    """
    This class represents the account of the user.
    
    Args:
        size (float): The total size of the account.
        risk_percentage (float): The percentage of the account to risk per trade.
    """
    
    def __init__(self, size: float, risk_percentage: float):
        self.size = size
        self.risk_percentage = risk_percentage
        
    def get_position_size(self, invalidation_point_percentage: float) -> float:
        """
        Calculate the position size based on the risk and invalidation point percentage.
        
        Args:
            invalidation_point_percentage (float): The percentage of invalidation point.
        
        Returns:
            float: The position size.
        """
        return self.size * (self.risk_percentage / 100) / (invalidation_point_percentage / 100)
