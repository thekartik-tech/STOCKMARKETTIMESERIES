
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Multi-Stock Market Forecasting Dashboard")

symbols = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'TSLA']
symbol = st.selectbox("Select stock:", symbols)

try:
    filepath = f'../data/processed/{symbol}_cleaned.csv'
    data = pd.read_csv(filepath, parse_dates=['Date'])
    data.set_index('Date', inplace=True)

    st.line_chart(data['Close'])

except FileNotFoundError:
    st.error(f"Processed file for {symbol} not found. Please run preprocessing notebook first.")
