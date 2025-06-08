import pandas as pd
from broker.angel_api import AngelAPI
from utils.trade_engine import TradeEngine
from utils.plotting import plot_results

# Import available strategies
from models.rsi_strategy import RSIStrategy
from models.moving_average import MovingAverageStrategy

# --- Load data ---
data = pd.read_csv("data/historical_data.csv")
api = AngelAPI(paper_mode=True)

# --- Ask user for strategy choice ---
print("Choose a strategy to run:")
print("1. RSI Strategy")
print("2. Moving Average Strategy")
choice = input("Enter 1 or 2: ").strip()

if choice == "1":
    strategy = RSIStrategy("RELIANCE", data)
elif choice == "2":
    strategy = MovingAverageStrategy("RELIANCE", data)
else:
    raise ValueError("Invalid choice. Please enter 1 or 2.")

# --- Generate signals ---
df = strategy.generate_signals()
df["date"] = pd.to_datetime(df["date"])

# --- Run trade simulation ---
engine = TradeEngine(api, df, capital=10000, allocation=0.6)
engine.simulate()
engine.summary()

# --- Plot results ---
plot_results(df, engine)

# --- Signal counts ---
print("\n--- SIGNAL SUMMARY ---")
print(df["signal"].value_counts())