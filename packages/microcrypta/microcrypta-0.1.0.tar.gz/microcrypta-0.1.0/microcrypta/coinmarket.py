import ccxt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mplfinance as mpf
from .coin import Coin
from . import config


class CoinMarket:

    """
    This class is the decision maker for solely Burak Civitcioglu.
    The class is written by him and licensed under his use only.
    """

    def __init__(self, coin: Coin, counter_coin: Coin, time_frame: str = '1h', plot: bool = False, plot_style: str = 'Solarize_Light2', fig_size: tuple = (20, 5)):
        """
        Initializes the CoinMarket with given parameters.

        Args:
            coin (Coin): The base coin.
            counter_coin (Coin): The counter coin.
            time_frame (str, optional): Time frame for OHLCV data. Defaults to '1h'.
            plot (bool, optional): Whether to plot the initial OHLCV data. Defaults to False.
            plot_style (str, optional): The style of the plot. Defaults to 'Solarize_Light2'.
            fig_size (tuple, optional): The figure size for plots. Defaults to (20, 5).
        """
        self.coin = coin
        self.counter_coin = counter_coin
        self.market_name = f"{coin.name}/{counter_coin.name}"
        self.time_frame = time_frame
        self.plot_style = plot_style
        self.fig_size = fig_size

        # Fetch OHLCV data
        ohlcv = config.EXCH.fetch_ohlcv(self.market_name, timeframe=self.time_frame)
        ohlcv = pd.DataFrame(ohlcv, columns=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
        ohlcv['Date'] = pd.to_datetime(ohlcv['Date'], unit='ms')
        ohlcv.set_index('Date', inplace=True)
        self.ohlcv = ohlcv

        # Set data attributes
        self.num_data = len(ohlcv)
        self.date_init = self.ohlcv.index[0]
        self.date_final = self.ohlcv.index[-1]

        self.date = self.ohlcv.index
        self.open = self.ohlcv['Open']
        self.close = self.ohlcv['Close']
        self.high = self.ohlcv['High']
        self.low = self.ohlcv['Low']
        self.volume = self.ohlcv['Volume']

        # Calculate derived data
        self.average_high_low = (self.high + self.low) / 2
        self.typical_price = (self.high + self.low + self.close) / 3
        self.average_ohlc = (self.open + self.high + self.low + self.close) / 4

        # Plot if required
        if plot:
            mpf.plot(self.ohlcv, type='candle', volume=True, tight_layout=True, style='yahoo')
    
    def moving_average(self, window: int = 30, ma_type: str = 'simple', price_type: str = 'typical', plot: bool = True) -> pd.Series:
        """
        Calculate the moving average of the specified price type.

        Args:
            window (int, optional): The window size for the moving average. Defaults to 30.
            ma_type (str, optional): The type of moving average ('simple' or 'exp'). Defaults to 'simple'.
            price_type (str, optional): The price type for the moving average ('typical', 'average_high_low', 'average_ohlc', 'close'). Defaults to 'typical'.
            plot (bool, optional): Whether to plot the moving average. Defaults to True.

        Raises:
            ValueError: If the 'ma_type' is not 'simple' or 'exp'.
            ValueError: If the 'price_type' is not one of 'typical', 'average_high_low', 'average_ohlc', 'close'.

        Returns:
            pd.Series: The moving average of the specified price type.
        """
        
        # Determine the price data based on the price_type
        if price_type == 'typical':
            price_data = self.typical_price
        elif price_type == 'average_high_low':
            price_data = self.average_high_low
        elif price_type == 'average_ohlc':
            price_data = self.average_ohlc
        elif price_type == 'close':
            price_data = self.close
        else:
            raise ValueError("The argument 'price_type' must be one of 'typical', 'average_high_low', 'average_ohlc', 'close'.")
        
        # Calculate the moving average based on the ma_type
        if ma_type == 'simple':
            ma = price_data.rolling(window).mean()
        elif ma_type == 'exp':
            ma = price_data.ewm(span=window, adjust=False).mean()
        else:
            raise ValueError("The argument 'ma_type' must be 'simple' or 'exp'.")
        
        # Plot the moving average if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.scatter(self.date, price_data, label=price_type.title() + ' Price', marker=".")
            plt.plot(self.date, ma, label=ma_type.title() + ' Moving Average')
            plt.title(f"{self.market_name} {price_type.title()} Price {ma_type.title()} Moving Average")
            plt.legend()
            plt.xlabel('Date')
            plt.ylabel(self.counter_coin.name)
            plt.show()

        return ma
            

    def fibonacci_retracement(self, plot: bool = True) -> pd.DataFrame:
        """
        Calculate the Fibonacci retracement levels.

        Args:
            plot (bool, optional): Whether to plot the Fibonacci retracement levels. Defaults to True.

        Returns:
            pd.DataFrame: A DataFrame containing the Fibonacci retracement levels and their corresponding prices.
        """
        
        # Calculate the Fibonacci levels
        close_max = self.close.max()
        close_min = self.close.min()
        diff = close_max - close_min
        fib_levels = np.array([0, 0.236, 0.382, 0.618, 1])

        prices = [close_max, close_max - fib_levels[1] * diff, close_max - fib_levels[2] * diff, close_max - fib_levels[3] * diff, close_min]
        level_price = pd.DataFrame({'Level': fib_levels, 'Price': prices})

        # Plot the Fibonacci retracement levels if required
        if plot:
            plt.style.use(self.plot_style)
            fig, ax = plt.subplots(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} Fibonacci Retracement Levels")

            ax.plot(self.date, self.close, color='black', label=f'Close Price {self.coin.name}')

            ax.axhspan(prices[1], close_min, alpha=0.4, color='honeydew', label='1st F-Level')
            ax.axhspan(prices[2], prices[1], alpha=0.5, color='coral', label='2nd F-Level')
            ax.axhspan(prices[3], prices[2], alpha=0.5, color='wheat', label='3rd F-Level')
            ax.axhspan(close_max, prices[3], alpha=0.5, color='lavender', label='Max Level')

            plt.legend()
            plt.ylabel(self.counter_coin.name)
            plt.xlabel("Date")
            plt.show()

        return level_price
        
    def macd(self, window: np.ndarray = np.array([26, 12, 9]), plot: bool = True) -> tuple[pd.Series, pd.Series]:
        """
        Calculate the Moving Average Convergence Divergence (MACD).

        Args:
            window (np.ndarray, optional): The window sizes for the long EMA, short EMA, and signal line. Defaults to np.array([26, 12, 9]).
            plot (bool, optional): Whether to plot the MACD and signal line. Defaults to True.

        Returns:
            tuple[pd.Series, pd.Series]: The MACD and signal line as separate Series.
        """
        
        # Calculate EMAs
        ema_long_period = self.high.ewm(span=window[0], adjust=False).mean()
        ema_short_period = self.high.ewm(span=window[1], adjust=False).mean()

        # Calculate MACD and signal line
        macd = ema_short_period - ema_long_period
        signal = macd.ewm(span=window[2], adjust=False).mean()
        
        # Plot MACD and signal line if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} MACD")

            plt.plot(self.date, macd, label='MACD', color='k')
            plt.plot(self.date, signal, label='Signal', color='tab:red')
            plt.legend(loc='upper right')

            plt.ylabel("Signal")
            plt.xlabel("Date")
            plt.show()

        return macd, signal


    def vwap(self, plot: bool = True) -> pd.DataFrame:
        """
        Calculate the Volume Weighted Average Price (VWAP).

        Args:
            plot (bool, optional): Whether to plot the VWAP. Defaults to True.

        Returns:
            pd.DataFrame: The DataFrame containing the OHLCV data with the VWAP included.
        """
        
        # Calculate VWAP
        self.ohlcv['average_price'] = (self.ohlcv['High'] + self.ohlcv['Low'] + self.ohlcv['Close']) / 3
        self.ohlcv['av_price_volume'] = self.ohlcv['average_price'] * self.ohlcv['Volume']
        self.ohlcv['cumulative_av_price_volume'] = self.ohlcv['av_price_volume'].cumsum()
        self.ohlcv['cumulative_volume'] = self.ohlcv['Volume'].cumsum()
        self.ohlcv['VWAP'] = self.ohlcv['cumulative_av_price_volume'] / self.ohlcv['cumulative_volume']
        self.ohlcv.drop(columns=['average_price', 'av_price_volume', 'cumulative_av_price_volume', 'cumulative_volume'], inplace=True)

        # Plot VWAP if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} VWAP")

            plt.scatter(self.date, self.open, label=f'Open Price {self.coin.name}', marker='.')
            plt.plot(self.date, self.ohlcv['VWAP'], label='VWAP', color='k')
            plt.legend()
            plt.ylabel(self.counter_coin.name)
            plt.xlabel("Date")
            plt.show()
            
        return self.ohlcv
    
    def rsi(self, window: int = 14, rsi_type: str = 'simple', plot: bool = True) -> tuple[pd.Series, pd.Series]:
        """
        Calculate the Relative Strength Index (RSI).

        Args:
            window (int, optional): The window size for calculating RSI. Defaults to 14.
            rsi_type (str, optional): The type of RSI ('simple' or 'exp'). Defaults to 'simple'.
            plot (bool, optional): Whether to plot the RSI and RSI Histogram. Defaults to True.

        Raises:
            ValueError: If the 'rsi_type' is not 'simple' or 'exp'.

        Returns:
            tuple[pd.Series, pd.Series]: The RSI and RSI Histogram as separate Series.
        """
        
        # Calculate the differences
        dif = self.close.diff()
        up = dif.clip(lower=0)
        down = -dif.clip(upper=0)

        # Calculate EMAs or SMAs of gains and losses
        if rsi_type == 'simple':
            up_ema = up.rolling(window).mean()
            down_ema = down.rolling(window).mean()
        elif rsi_type == 'exp':
            up_ema = up.ewm(span=window, adjust=False).mean()
            down_ema = down.ewm(span=window, adjust=False).mean()
        else:
            raise ValueError("The argument 'rsi_type' must be either 'simple' or 'exp'.")

        # Calculate RSI and RSI Histogram
        rs = up_ema / down_ema
        rsi = 100.0 - (100.0 / (1.0 + rs))
        rsi_ema = rsi.ewm(span=window, adjust=False).mean()
        rsi_hist = rsi - rsi_ema

        # Plot RSI and RSI Histogram if required
        if plot:
            plt.style.use(self.plot_style)

            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} RSI")
            plt.plot(self.date, rsi, label='RSI', color='tab:blue')
            plt.axhline(y=70, color='tab:green')
            plt.axhline(y=30, color='tab:orange')
            plt.plot(self.date, rsi_ema, label='EMA RSI', color='tab:brown')
            plt.legend()
            plt.ylabel("RSI")
            plt.xlabel("Date")
            
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} RSI Histogram")
            plt.bar(self.date[rsi_hist < 0], rsi_hist[rsi_hist < 0], color='red', width=0.015)
            plt.bar(self.date[rsi_hist >= 0], rsi_hist[rsi_hist >= 0], color='green', width=0.015)
            plt.show()
            
        return rsi, rsi_hist

    def psar(self, plot: bool = True) -> pd.Series:
        """
        Calculate the Parabolic SAR (PSAR).

        Args:
            plot (bool, optional): Whether to plot the PSAR. Defaults to True.

        Returns:
            pd.Series: The PSAR values.
        """
        
        iaf = 0.02 
        maxaf = 0.2
        length = self.num_data

        dates = self.date.to_numpy()
        high = self.high.to_numpy()
        low = self.low.to_numpy()
        close = self.close.to_numpy()

        psar = np.copy(close)
        psarbull = np.full(length, np.nan)
        psarbear = np.full(length, np.nan)
        bull = True
        af = iaf
        hp = high[0]
        lp = low[0]

        for i in range(2, length):
            if bull:
                psar[i] = psar[i - 1] + af * (hp - psar[i - 1])
            else:
                psar[i] = psar[i - 1] + af * (lp - psar[i - 1])

            reverse = False

            if bull:
                if low[i] < psar[i]:
                    bull = False
                    reverse = True
                    psar[i] = hp
                    lp = low[i]
                    af = iaf
            else:
                if high[i] > psar[i]:
                    bull = True
                    reverse = True
                    psar[i] = lp
                    hp = high[i]
                    af = iaf

            if not reverse:
                if bull:
                    if high[i] > hp:
                        hp = high[i]
                        af = min(af + iaf, maxaf)
                    if low[i - 1] < psar[i]:
                        psar[i] = low[i - 1]
                    if low[i - 2] < psar[i]:
                        psar[i] = low[i - 2]
                else:
                    if low[i] < lp:
                        lp = low[i]
                        af = min(af + iaf, maxaf)
                    if high[i - 1] > psar[i]:
                        psar[i] = high[i - 1]
                    if high[i - 2] > psar[i]:
                        psar[i] = high[i - 2]

            if bull:
                psarbull[i] = psar[i]
            else:
                psarbear[i] = psar[i]
                    
        if plot:
            plt.style.use(self.plot_style)

            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} PSAR")

            plt.plot(dates, close, label=f'Close Price {self.coin.name}')
            plt.plot(dates, psarbull, label='Bull')
            plt.plot(dates, psarbear, label='Bear')
            plt.legend()
            plt.ylabel(self.counter_coin.name)
            plt.xlabel("Date")
            plt.show()

        return pd.Series(psar, index=self.date)

    def awesome_oscillator(self, window_1: int = 5, window_2: int = 34, plot: bool = True) -> pd.Series:
        """
        Calculate the Awesome Oscillator.

        Args:
            window_1 (int, optional): The window size for the short period. Defaults to 5.
            window_2 (int, optional): The window size for the long period. Defaults to 34.
            plot (bool, optional): Whether to plot the Awesome Oscillator. Defaults to True.

        Returns:
            pd.Series: The Awesome Oscillator values.
        """
        
        # Calculate the median price
        median_price = self.close.rolling(window=2).median()

        # Calculate short and long period simple moving averages
        short_sma = median_price.rolling(window=window_1).mean()
        long_sma = median_price.rolling(window=window_2).mean()

        # Calculate Awesome Oscillator
        awesome_oscillator = short_sma - long_sma
        
        # Plot Awesome Oscillator if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} Awesome Oscillator")

            colors = ['#f44336' if awesome_oscillator[i] < awesome_oscillator[i - 1] else '#26a69a' for i in range(1, len(awesome_oscillator))]
            plt.bar(self.date[1:], awesome_oscillator[1:], color=colors, width=0.025)
            plt.show()
            
        return awesome_oscillator
    
    def bollinger_bands(self, window: int = 20, plot: bool = True) -> tuple[pd.Series, pd.Series]:
        """
        Calculate the Bollinger Bands.

        Args:
            window (int, optional): The window size for the moving average and standard deviation. Defaults to 20.
            plot (bool, optional): Whether to plot the Bollinger Bands. Defaults to True.

        Returns:
            tuple[pd.Series, pd.Series]: The upper and lower Bollinger Bands as separate Series.
        """
        
        # Calculate the moving average and standard deviation
        sma = self.close.rolling(window=window).mean()
        std = self.close.rolling(window=window).std()
        upper_band = sma + (std * 2)
        lower_band = sma - (std * 2)
        
        # Plot Bollinger Bands if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} Bollinger Bands")

            plt.plot(self.date, self.close, label=f'Close Price {self.coin.name}')
            plt.plot(self.date, upper_band, label='Upper BB', linestyle="--")
            plt.plot(self.date, sma, label='Middle BB', linestyle="--")
            plt.plot(self.date, lower_band, label='Lower BB', linestyle="--")
            
            plt.legend()
            plt.ylabel(self.counter_coin.name)
            plt.xlabel("Date")
            plt.show()
            
        return upper_band, lower_band
    
    def stochastic_oscillator(self, window: int = 14, window_d: int = 3, buy_sell_lines: tuple = (80, 20), plot: bool = True) -> tuple[pd.Series, pd.Series]:
        """
        Calculate the Stochastic Oscillator.

        Args:
            window (int, optional): The window size for calculating %K. Defaults to 14.
            window_d (int, optional): The window size for calculating %D. Defaults to 3.
            buy_sell_lines (tuple, optional): The buy and sell lines for the oscillator. Defaults to (80, 20).
            plot (bool, optional): Whether to plot the Stochastic Oscillator. Defaults to True.

        Returns:
            tuple[pd.Series, pd.Series]: The %K and %D lines as separate Series.
        """
        
        # Calculate %K and %D lines
        high_window = self.high.rolling(window).max()
        low_window = self.low.rolling(window).min()
        
        percent_k = (self.close - low_window) * 100 / (high_window - low_window)
        percent_d = percent_k.rolling(window_d).mean()
        
        # Plot Stochastic Oscillator if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} Stochastic Oscillator")
            
            plt.plot(self.date, percent_k, label='%K')
            plt.plot(self.date, percent_d, label='%D', color='tab:pink')
            plt.axhline(y=buy_sell_lines[0], color='tab:green')
            plt.axhline(y=buy_sell_lines[1], color='tab:orange')

            plt.legend()
            plt.ylabel('Stochastic Oscillator')
            plt.xlabel("Date")
            plt.show()
            
        return percent_k, percent_d
            
    def aroon(self, period: int = 25, plot: bool = True) -> tuple[pd.Series, pd.Series]:
        """
        Calculate the Aroon Oscillator.

        Args:
            period (int, optional): The period for calculating the Aroon Up and Down. Defaults to 25.
            plot (bool, optional): Whether to plot the Aroon Oscillator. Defaults to True.

        Returns:
            tuple[pd.Series, pd.Series]: The Aroon Up and Aroon Down lines as separate Series.
        """
        
        # Calculate Aroon Up and Down
        aroon_up = pd.Series([(100 / period) * (period - np.argmax(self.close[t-period:t])) for t in range(period, len(self.close))], index=self.date[period:])
        aroon_down = pd.Series([(100 / period) * (period - np.argmin(self.close[t-period:t])) for t in range(period, len(self.close))], index=self.date[period:])
        
        # Reindex to match the original date range
        aroon_up = aroon_up.reindex(self.date)
        aroon_down = aroon_down.reindex(self.date)

        # Plot Aroon Oscillator if required
        if plot:
            plt.style.use(self.plot_style)
            plt.figure(figsize=self.fig_size, dpi=80)
            plt.title(f"{self.market_name} Aroon Oscillator")
            
            plt.plot(self.date, aroon_up, label="Aroon Up", color="tab:green")
            plt.plot(self.date, aroon_down, label="Aroon Down", color="tab:red")
            
            plt.legend()
            plt.ylabel('Aroon Oscillator')
            plt.xlabel("Date")
            plt.show()
            
        return aroon_up, aroon_down

    # Here will be AAX index coded.
    
    def list_all_indicators(self) -> None:
        """
        List all available technical indicators.
        """
        
        indicators = [
            "1  - Moving Average",
            "2  - Fibonacci Retracement",
            "3  - MACD",
            "4  - PSAR",
            "5  - VWAP",
            "6  - RSI",
            "7  - Awesome Oscillator",
            "8  - Bollinger Bands",
            "9  - Stochastic Oscillator",
            "10 - Aroon Oscillator"
        ]
        
        print("Currently available indicators are:\n")
        for indicator in indicators:
            print(indicator)

    def technical_summary(self) -> None:
        """
        Display the plots of all available technical indicators.
        """
        
        self.list_all_indicators()
        
        # Display each technical indicator with plotting enabled
        self.moving_average(plot=True)
        self.fibonacci_retracement(plot=True)
        self.macd(plot=True)
        self.psar(plot=True)
        self.vwap(plot=True)
        self.rsi(plot=True)
        self.awesome_oscillator(plot=True)
        self.bollinger_bands(plot=True)
        self.stochastic_oscillator(plot=True)
        self.aroon(plot=True)
