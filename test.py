"""
Sources:
https://medium.com/automated-trading/obtain-40-technical-indicators-for-a-stock-using-python-247b32e85f30

"""

# import yfinance as yf
# from ta import add_all_ta_features
# from ta.utils import dropna


# tick = yf.Ticker('MSFT')
# hist_data = tick.history(period="max")  # Tells yfinance what kind of data we want about this stock (In this example, all of the historical data)

# print(hist_data.head()) # Observe the historical stock data

# mom_data = add_all_ta_features(hist_data, open="Open", high="High", low="Low", close="Close", volume='Volume') # Substantiate data with momentum indicators
# print(mom_data.columns)


import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna

# Load datas
df = pd.read_csv('datas.csv', sep=',')

# Clean NaN values
df = dropna(df)

# Add ta features filling NaN values
df = add_all_ta_features(
    df, open="Open", high="High", low="Low", close="Close", volume="Volume_BTC", fillna=True)

print(df)