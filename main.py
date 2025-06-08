from broker.angel_api import AngelAPI
from models.moving_average import MovingAverageStrategy
from utils.trade_engine import TradeEngine
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load data
data = pd.read_csv("data/historical_data.csv")

# Setup
api = AngelAPI(paper_mode=True)
strategy = MovingAverageStrategy("RELIANCE", data)
df = strategy.generate_signals()

# Run backtest using TradeEngine with 20% allocation of ₹10,000
engine = TradeEngine(api, df, capital=10000, allocation=0.2)
engine.simulate()
engine.summary()

# Extract only executed trades from engine
executed_buys = [trade["buy_date"] for trade in engine.executed_trades]
executed_buy_prices = [trade["buy_price"] for trade in engine.executed_trades]
executed_sells = [trade["sell_date"] for trade in engine.executed_trades]
executed_sell_prices = [trade["sell_price"] for trade in engine.executed_trades]

# Plot
fig, ax = plt.subplots(figsize=(14, 7))

# Price and SMAs
ax.plot(df["date"], df["close"], label="Close Price", color="blue", linewidth=1.5)
ax.plot(df["date"], df["SMA_5"], label="SMA 5", linestyle="--", linewidth=1, color="orange", alpha=0.7)
ax.plot(df["date"], df["SMA_20"], label="SMA 20", linestyle="--", linewidth=1, color="green", alpha=0.7)

# Executed trades only
ax.scatter(executed_buys, executed_buy_prices, label="Executed Buy", marker="^", color="green", s=80, alpha=0.9, zorder=5)
ax.scatter(executed_sells, executed_sell_prices, label="Executed Sell", marker="v", color="red", s=80, alpha=0.9, zorder=5)

# Format and grid
ax.set_title("Executed Trades with SMA Strategy")
ax.set_xlabel("Date")
ax.set_ylabel("Price")
ax.legend()
ax.grid(True)

# Format x-axis dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

# Signal summary
print("\n--- SIGNAL SUMMARY ---")
print(df["signal"].value_counts())