import ccxt

# Global variables for exchange and markets
global EXCH, MARKETS

# Initialize the exchange using ccxt
EXCH = ccxt.binance()

# Load the markets from the exchange
MARKETS = EXCH.load_markets()
