import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from .coinmarket import CoinMarket
from . import config

class Backtest:
    """
    Class for backtesting trading signals.
    
    Args:
        coin_market (CoinMarket): The CoinMarket object containing market data.
        bsh_signal (pd.DataFrame): DataFrame containing buy/sell/hold signals.
        signal_name (str): Name of the signal.
        initial_position_size (float, optional): Initial position size in currency. Defaults to 1000.
        initial_num_coin (float, optional): Initial number of coins. Defaults to 0.
    """
    
    def __init__(self, coin_market: CoinMarket, bsh_signal: pd.DataFrame, signal_name: str, initial_position_size: float = 1000, initial_num_coin: float = 0):
        self.coin_market = coin_market
        self.bsh_signal = bsh_signal
        self.signal_name = signal_name
        
        self.position = bsh_signal["Position"]
        self.first_valid_index = bsh_signal["Buy Price"].first_valid_index()
        self.last_valid_index = bsh_signal["Sell Price"].last_valid_index()
        
        self.backtest_data = bsh_signal.loc[self.first_valid_index:self.last_valid_index]
        self.backtest_data_size = len(self.backtest_data)
        
        self.initial_position_size = initial_position_size
        self.initial_num_coin = initial_num_coin
        
        self.current_position_size = initial_position_size
        self.current_num_coin = initial_num_coin
        self.commission_rate_percent = 0.001
        
    def backtest(self, plot: bool = True) -> tuple[np.ndarray, np.ndarray, float]:
        """
        Run the backtest and calculate position size, number of coins, and percentage gain.
        
        Args:
            plot (bool, optional): Whether to plot the backtest results. Defaults to True.
        
        Returns:
            tuple[np.ndarray, np.ndarray, float]: History of position sizes, number of coins, and percentage gain.
        """
        
        history_total_position = np.empty(self.backtest_data_size)
        history_total_position[:] = np.NaN
        
        history_position_size = [self.current_position_size]
        history_num_coin = [self.current_num_coin]
        
        for i in range(self.backtest_data_size):
            if self.backtest_data.iloc[i]["Position"] == 1 and not np.isnan(self.backtest_data.iloc[i]["Buy Price"]):
                self.current_num_coin = self.current_position_size / self.backtest_data.iloc[i]["Buy Price"]
                self.current_position_size = 0
                
                history_position_size.append(self.current_position_size - self.commission_rate_percent * self.current_position_size)
                history_num_coin.append(self.current_num_coin)
                
            elif self.backtest_data.iloc[i]["Position"] == 0 and not np.isnan(self.backtest_data.iloc[i]["Sell Price"]):
                self.current_position_size = self.current_num_coin * self.backtest_data.iloc[i]["Sell Price"] - (self.commission_rate_percent * self.current_num_coin * self.backtest_data.iloc[i]["Sell Price"])
                self.current_num_coin = 0                    
                history_total_position[i] = self.current_position_size 
                history_position_size.append(self.current_position_size - self.commission_rate_percent * self.current_position_size)
                history_num_coin.append(self.current_num_coin)
        
        history_position_size = np.array(history_position_size)
        history_num_coin = np.array(history_num_coin)
        percent_gain = 100 * ((self.current_position_size - self.initial_position_size) / self.initial_position_size)
        
        print(f'The percentage of gain of {self.signal_name} in {self.last_valid_index - self.first_valid_index} is {percent_gain:.2f}%\n')
        
        if plot:
            plt.style.use(self.coin_market.plot_style)
            plt.figure(figsize=(20, 5), dpi=80)
            mask = np.isfinite(history_total_position)
            plt.plot(self.backtest_data.index[mask], history_total_position[mask])
            plt.scatter(self.backtest_data.index.to_numpy()[mask], history_total_position[mask], label="Position Size")

            plt.title(f"Percent Gain with {self.signal_name.title()}")
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel(self.coin_market.counter_coin.name)
            plt.show()

        return history_position_size, history_num_coin, percent_gain
    
    def plot_signal(self) -> None:
        """
        Plot the buy/sell signals on the price chart.
        """
        
        plt.style.use(self.coin_market.plot_style)
        plt.figure(figsize=(20, 5), dpi=80)
        plt.title(f"{self.coin_market.market_name} {self.signal_name.title()} Signal")
        plt.plot(self.coin_market.date, self.coin_market.close, label=self.coin_market.coin.name)
        plt.plot(self.coin_market.date, self.bsh_signal['Buy Price'], marker='^', markersize=12, color='#26a69a', linewidth=0, label='Buy Signal')
        plt.plot(self.coin_market.date, self.bsh_signal['Sell Price'], marker='v', markersize=12, color='#f44336', linewidth=0, label='Sell Signal')
        plt.legend()
        plt.show()
