from broker.angel_api import AngelAPI
from models.moving_average import MovingAverageStrategy
from utils.trade_engine import TradeEngine
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# --- Load historical stock data ---
data = pd.read_csv("data/historical_data.csv")

# --- Initialize API (paper trading mode) ---
api = AngelAPI(paper_mode=True)

# --- Apply strategy ---
strategy = MovingAverageStrategy("RELIANCE", data)
df = strategy.generate_signals()
df["date"] = pd.to_datetime(df["date"])

# --- Simulate trades ---
engine = TradeEngine(api, df, capital=10000, allocation=0.6)
engine.simulate()
engine.summary()

# --- Executed Trades for Plotting ---
executed_df = pd.DataFrame(engine.executed_trades)
executed_df["entry_date"] = pd.to_datetime(executed_df["entry_date"])
executed_df["exit_date"] = pd.to_datetime(executed_df["exit_date"])

# --- Capital History for Cash Usage Chart ---
capital_df = pd.DataFrame(engine.capital_history)
capital_df["date"] = pd.to_datetime(capital_df["date"])

# --- Create Subplots: Price Chart, RSI Chart, Capital Chart ---
fig, (ax1, ax2, ax3) = plt.subplots(
    3, 1, figsize=(14, 12), sharex=True, 
    gridspec_kw={'height_ratios': [3, 1, 1]}
)

# --- PRICE + TRADE CHART ---
ax1.plot(df["date"], df["close"], label="Close Price", color="blue", linewidth=1.5)
ax1.plot(df["date"], df["SMA_5"], label="SMA 5", linestyle="--", color="orange", alpha=0.7)
ax1.plot(df["date"], df["SMA_20"], label="SMA 20", linestyle="--", color="green", alpha=0.7)

# Executed trades
if not executed_df.empty:
    ax1.scatter(executed_df["entry_date"], executed_df["entry_price"], label="Executed Buy", marker="^", color="green", s=60, zorder=5)
    ax1.scatter(executed_df["exit_date"], executed_df["exit_price"], label="Executed Sell", marker="v", color="red", s=60, zorder=5)

ax1.set_ylabel("Price (₹)")
ax1.set_title("Executed Trades - SMA Crossover with RSI Strategy")
ax1.legend()
ax1.grid(True)

# --- RSI CHART ---
ax2.plot(df["date"], df["RSI"], label="RSI", color="purple", linewidth=1.2)
ax2.axhline(30, color="red", linestyle="--", linewidth=0.8, label="Oversold (30)")
ax2.axhline(70, color="green", linestyle="--", linewidth=0.8, label="Overbought (70)")
ax2.set_ylabel("RSI")
ax2.set_ylim([0, 100])
ax2.grid(True)
ax2.legend()

# --- CAPITAL USAGE CHART ---
ax3.plot(capital_df["date"], capital_df["capital"], label="Remaining Capital", color="black", linewidth=1.5)
ax3.set_ylabel("₹ Cash")
ax3.set_xlabel("Date")
ax3.set_title("Cash Usage Over Time")
ax3.grid(True)
ax3.legend()

# --- Format X-Axis ---
ax3.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax3.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# --- Signal Summary ---
print("\n--- SIGNAL SUMMARY ---")
print(df["signal"].value_counts())