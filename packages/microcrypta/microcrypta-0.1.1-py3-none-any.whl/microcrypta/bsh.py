from . import config
from .coinmarket import CoinMarket
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class BSH:
    """
    This class provides Buy, Sell, or HODL signals.
    It will be used for the Strategy class. The results of
    this class's instances will help with the general strategy
    across many markets.
    """
    
    def __init__(self, coin_market: CoinMarket):
        """
        Initialize with the corresponding market we are working
        and the technical indicators.
        
        Args:
            coin_market (CoinMarket): CoinMarket object.
        """
        self.coin_market = coin_market
        
    def buy_sell_position(self, signal: np.ndarray) -> pd.DataFrame:
        """
        Determine buy and sell positions based on the signal.
        
        Args:
            signal (np.ndarray): Signal array where 1 indicates buy, -1 indicates sell, and 0 indicates hold.
        
        Returns:
            pd.DataFrame: DataFrame containing buy prices, sell prices, signals, and positions.
        """
        pos = np.ones(self.coin_market.num_data)

        for i in np.arange(self.coin_market.num_data):
            if signal[i] == 1:
                pos[i] = 1
            elif signal[i] == -1:
                pos[i] = 0
            else: 
                pos[i] = pos[i-1]
                
        buy_price = np.empty(self.coin_market.num_data)
        buy_price[:] = np.NaN
        
        sell_price = np.empty(self.coin_market.num_data)
        sell_price[:] = np.NaN
        
        signal_buy_index = np.where(signal == 1)
        signal_sell_index = np.where(signal == -1)
        
        buy_price_by_index = np.take(self.coin_market.close.to_numpy(), signal_buy_index)
        sell_price_by_index = np.take(self.coin_market.close.to_numpy(), signal_sell_index)
        
        np.put(buy_price, signal_buy_index, buy_price_by_index)
        np.put(sell_price, signal_sell_index, sell_price_by_index)
        
        df = pd.DataFrame(buy_price, index=self.coin_market.date).rename(columns={0: "Buy Price"})
        df['Sell Price'] = sell_price
        df['Signal'] = signal
        df["Position"] = pos
        
        return df
            
    def awesome_oscillator(self) -> pd.DataFrame:
        """
        Simple BSH Signal for Awesome Oscillator.
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for Awesome Oscillator.
        """
        awesome_oscillator = self.coin_market.awesome_oscillator(plot=False)
        awesome_signal = np.zeros(self.coin_market.num_data)
        signal = 0  # HODL Signal

        for i in np.arange(self.coin_market.num_data):
            if awesome_oscillator[i] > 0 and awesome_oscillator[i-1] < 0 and signal != 1:
                signal = 1
                awesome_signal[i] = signal
            elif awesome_oscillator[i] < 0 and awesome_oscillator[i-1] > 0 and signal != -1:
                signal = -1
                awesome_signal[i] = signal
            else:
                awesome_signal[i] = 0
                
        back_result = self.buy_sell_position(awesome_signal)
        return back_result
    
    def rsi(self, window: int) -> pd.DataFrame:
        """
        BSH Signal for RSI.
        
        Args:
            window (int): Window size for RSI.
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for RSI.
        """
        rsi, rsi_hist = self.coin_market.rsi(window, plot=False)
        rsi_signal = np.zeros(self.coin_market.num_data)
        
        signal = 0
        
        for i in np.arange(self.coin_market.num_data):
            if rsi[i-1] > 30 and rsi[i] < 30 and signal != 1:
                signal = 1
                rsi_signal[i] = signal
            elif rsi[i-1] < 70 and rsi[i] > 70 and signal != -1:
                signal = -1
                rsi_signal[i] = signal
        
        back_result = self.buy_sell_position(rsi_signal)
        return back_result
      
    def moving_average(self, short_window: int = 20, long_window: int = 50) -> pd.DataFrame:
        """
        BSH Signal for Moving Average crossover.
        
        Args:
            short_window (int, optional): Window size for the short moving average. Defaults to 20.
            long_window (int, optional): Window size for the long moving average. Defaults to 50.
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for Moving Average crossover.
        """
        simple_ma_short = self.coin_market.moving_average(window=short_window, ma_type='simple', plot=False)
        simple_ma_long = self.coin_market.moving_average(window=long_window, ma_type='simple', plot=False)
        
        simple_ma_signal = np.zeros(len(simple_ma_long))
        signal = 0

        for i in np.arange(self.coin_market.num_data - len(simple_ma_long), self.coin_market.num_data):
            if simple_ma_short[i] > simple_ma_long[i] and signal != 1:
                signal = 1
                simple_ma_signal[i] = signal
            elif simple_ma_long[i] > simple_ma_short[i] and signal != -1:
                signal = -1
                simple_ma_signal[i] = signal
            else:
                pass
            
        back_result = self.buy_sell_position(simple_ma_signal)
        return back_result
    
    def macd(self, window: np.ndarray = np.array([26, 12, 9])) -> pd.DataFrame:
        """
        BSH Signal for MACD.
        
        Args:
            window (np.ndarray, optional): Window sizes for MACD calculation. Defaults to np.array([26, 12, 9]).
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for MACD.
        """
        macd_line, signal_line = self.coin_market.macd(window, plot=False)

        macd_signal = np.zeros(len(macd_line))
        signal = 0

        for i in np.arange(self.coin_market.num_data):
            if macd_line[i] > signal_line[i] and signal != 1:
                signal = 1
                macd_signal[i] = signal
            elif signal_line[i] > macd_line[i] and signal != -1:
                signal = -1
                macd_signal[i] = signal
            else:
                pass

        back_result = self.buy_sell_position(macd_signal)
        return back_result

    def bollinger_bands(self, window: int = 20) -> pd.DataFrame:
        """
        BSH Signal for Bollinger Bands.
        
        Args:
            window (int, optional): Window size for Bollinger Bands. Defaults to 20.
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for Bollinger Bands.
        """
        upper, lower = self.coin_market.bollinger_bands(window, plot=False)
        
        bollinger_signal = np.zeros(len(upper))
        signal = 0
        
        for i in np.arange(self.coin_market.num_data - len(upper), self.coin_market.num_data):
            if self.coin_market.close[i-1] > lower[i-1] and self.coin_market.close[i] < lower[i] and signal != 1:
                signal = 1
                bollinger_signal[i] = signal
            elif self.coin_market.close[i-1] < upper[i-1] and self.coin_market.close[i] > upper[i] and signal != -1:
                signal = -1
                bollinger_signal[i] = signal
            else:
                pass
            
        back_result = self.buy_sell_position(bollinger_signal)
        return back_result
    
    def stochastic_oscillator(self, window: int = 14, window_d: int = 3, buy_sell_lines: tuple = (80, 20)) -> pd.DataFrame:
        """
        BSH Signal for Stochastic Oscillator.
        
        Args:
            window (int, optional): Window size for %K. Defaults to 14.
            window_d (int, optional): Window size for %D. Defaults to 3.
            buy_sell_lines (tuple, optional): Buy and sell thresholds. Defaults to (80, 20).
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for Stochastic Oscillator.
        """
        k, d = self.coin_market.stochastic_oscillator(window=window, window_d=window_d, buy_sell_lines=buy_sell_lines, plot=False)
        
        stochastic_signal = np.zeros(len(d))
        signal = 0
        
        for i in np.arange(self.coin_market.num_data - len(d), self.coin_market.num_data):
            if k[i] < buy_sell_lines[1] and d[i] < buy_sell_lines[1] and k[i] < d[i] and signal != 1:
                signal = 1
                stochastic_signal[i] = signal
            elif k[i] > buy_sell_lines[0] and d[i] > buy_sell_lines[0] and k[i] > d[i] and signal != -1:
                signal = -1
                stochastic_signal[i] = signal
            else:
                pass
            
        back_result = self.buy_sell_position(stochastic_signal)
        return back_result
    
    def aroon(self, period: int = 25, buy_sell_lines: tuple = (70, 30)) -> pd.DataFrame:
        """
        BSH Signal for Aroon Oscillator.
        
        Args:
            period (int, optional): Period for Aroon Oscillator. Defaults to 25.
            buy_sell_lines (tuple, optional): Buy and sell thresholds. Defaults to (70, 30).
        
        Returns:
            pd.DataFrame: DataFrame with buy, sell, and hold signals for Aroon Oscillator.
        """
        aroon_up, aroon_down = self.coin_market.aroon(period=period, plot=False)
        aroon_signal = np.zeros(len(aroon_up))
        signal = 0
        
        for i in np.arange(self.coin_market.num_data):
            if aroon_up[i] >= buy_sell_lines[0] and aroon_down[i] <= buy_sell_lines[1] and signal != 1:
                signal = 1
                aroon_signal[i] = signal
            elif aroon_up[i] <= buy_sell_lines[1] and aroon_down[i] >= buy_sell_lines[0] and signal != -1:
                signal = -1
                aroon_signal[i] = signal
            else:
                pass
            
        back_result = self.buy_sell_position(aroon_signal)
        return back_result
