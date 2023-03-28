import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

st.title('Stock screener')
st.header('Access over 6000 different stock data!')

tickers = pd.read_csv('data/tickers.csv')

ticker_option = st.sidebar.selectbox(
    'Pick a stock',
     tickers)

date_slider = st.sidebar.select_slider(
     'Select a period ',
   options=['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max'],
   value='6mo')

st.subheader(f'You have selected: {ticker_option} stock for {date_slider}')

@st.cache_data
def load_data(ticker_option, date_slider):
    return yf.download(ticker_option, period = date_slider)

data_load_state = st.text('Loading data...')
data = load_data(ticker_option, date_slider)
data_load_state.text("Done!")

fig = go.Figure(data=[go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'])])

st.write(fig)

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
