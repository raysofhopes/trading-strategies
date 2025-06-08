import yfinance as yf
import pandas as pd

# Download historical data for RELIANCE from Yahoo Finance (NSE)
data = yf.download("RELIANCE.NS", start="2024-01-01", end="2024-12-31")

# Format and clean
data = data.reset_index()[["Date", "Open", "High", "Low", "Close", "Volume"]]
data.columns = ["date", "open", "high", "low", "close", "volume"]

# Save to CSV
data.to_csv("data/historical_data.csv", index=False)
print("✅ Data downloaded and saved to data/historical_data.csv")