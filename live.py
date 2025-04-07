# Live Data Dashboard using Streamlit and yfinance

import streamlit as st
import yfinance as yf
import pandas as pd
import time

st.set_page_config(page_title="Live Stock Dashboard 1", layout="wide")

st.title("📈 Live Stock Price Dashboard 2")
st.markdown("Get real-time stock data using [Yahoo Finance](https://finance.yahoo.com/)")

# Sidebar for user input
symbol = st.sidebar.text_input("Enter stock symbol (e.g., AAPL, MSFT, TSLA):", "AAPL")
refresh_rate = st.sidebar.slider("Refresh every X seconds", 5, 60, 10)

placeholder = st.empty()

# Live updating section
while True:
    try:
        data = yf.download(tickers=symbol, period="1d", interval="1m")
        if data.empty:
            st.error("No data found for the given symbol.")
            break

        with placeholder.container():
            st.subheader(f"Live data for: {symbol}")
            st.line_chart(data["Close"], use_container_width=True)
            st.write("Latest Data:", data.tail(1))
        time.sleep(refresh_rate)

    except Exception as e:
        st.error(f"Error fetching data: {e}")
        break
