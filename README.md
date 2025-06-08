# 📈 Trading Strategies Backtester

This project is a modular **stock trading strategy backtester** in Python. It allows you to test different algorithmic trading strategies like **RSI** and **Moving Average Crossover** on historical stock data (e.g., Reliance Industries).

You can simulate trades, track P&L, and visualize executed orders, technical indicators, and cash usage over time — all in a clean and extensible structure.

---

## 🚀 Features

- ✅ Strategy selector (RSI or SMA crossover)
- 📊 Visual charts (price, RSI, cash usage)
- 💼 Capital allocation logic
- 🧠 Modular architecture (easy to extend with new strategies)
- 🧪 Paper trading mode with simulated P&L
- 🗂️ Organized project structure
- 🧹 `.gitignore` to keep environments and cache clean

---

## 🧠 Strategies Implemented

| Strategy | Description |
|----------|-------------|
| **RSI Strategy** | Buys when RSI < 30, sells when RSI > 70 |
| **SMA Crossover** | Buys when short SMA crosses above long SMA and RSI confirms |

---

## 📂 Project Structure

```
trading-strategies/
│
├── broker/
│   └── angel_api.py              # Simulated trading API
├── config/
│   └── config.env                # (Optional) API keys or config
├── data/
│   └── historical_data.csv       # Input data (from Yahoo Finance etc.)
├── logs/
│   └── trade_log.txt             # Trade logs (if used)
├── models/
│   ├── moving_average.py         # Moving Average Strategy
│   └── rsi_strategy.py           # RSI Strategy
├── utils/
│   ├── indicators.py             # Indicator calculations
│   ├── plotting.py               # Plotting helper for charts
│   └── trade_engine.py           # Backtest engine
├── main.py                       # Entry point
└── requirements.txt              # Python dependencies
```

---

## 📈 Example Output

- ✅ Executed buy/sell signals on price chart  
- 🟣 RSI chart with oversold/overbought zones  
- 💵 Capital usage (remaining cash vs investment)

![Example Chart](docs/example-chart.png) <!-- Replace with actual image URL or path -->

---

## 🛠️ Setup Instructions

```bash
# Clone repo
git clone https://github.com/raysofhopes/trading-strategies.git
cd trading-strategies

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 📊 Run the Backtester

```bash
python main.py
```

You'll be prompted to select a strategy (`1` for RSI or `2` for SMA Crossover).

---

## ✅ Sample Output

```
--- TRADE STATS ---
Total Trades: 3
Wins: 2 | Losses: 1
Win Rate: 66.67%
Net P&L: ₹350.45
Final Capital from ₹6000.00: ₹6350.45
Currently Invested: ₹0.00
Remaining Cash: ₹6350.45
```

---

## 🤝 Contributions

Want to add Bollinger Bands or MACD strategies? Fork this repo and start building! PRs welcome.

---

## 📧 Contact

**Souvik Ray**  
📧 [souvikray@live.com](mailto:souvikray@live.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/souvik-ray-a74b93162/)

---

## 📌 License

MIT License. Feel free to use, modify, and share this project.