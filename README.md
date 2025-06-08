# 🧠 Trading Strategies with AngelOne API

A modular and extensible Python trading bot that simulates and visualizes **technical trading strategies** using historical stock data. Built with **paper trading** support, strategy injection, capital tracking, and chart visualizations.

---

## 🚀 Features

- ✅ SMA crossover strategy (SMA 5 vs SMA 20)
- ✅ Capital allocation (e.g., 20% of ₹10,000)
- ✅ Paper trading simulation (no real trades)
- ✅ Executed trade logs and performance stats
- ✅ Clean chart with only actual trades
- ✅ Easily extendable with new strategies

---

## 📊 Strategy Logic

**Current Strategy: SMA Crossover**
- **Buy** when `SMA_5 > SMA_20`
- **Sell** when `SMA_5 < SMA_20`
- Optional: Combine with RSI filters (available in `moving_average.py`)

---

## 📁 Folder Structure

```
trading-strategies/
├── broker/
│   └── angel_api.py              # AngelOne API wrapper
├── models/
│   ├── base_model.py             # Strategy base class
│   └── moving_average.py         # SMA strategy implementation
├── utils/
│   └── trade_engine.py           # Core trading simulation engine
├── data/
│   └── historical_data.csv       # Example dataset
├── main.py                       # Run your simulation here
├── requirements.txt              # Install dependencies
└── README.md                     # This file
```

---

## 🛠 Getting Started

### 1. Install requirements
```bash
pip install -r requirements.txt
```

### 2. Add your API credentials to `config.env` (if using AngelOne live later)

### 3. Run the bot
```bash
python main.py
```

---

## 📈 Example Output

- P&L report in terminal
- Trade chart showing **only executed trades**
- Strategy visualization with SMA and Buy/Sell markers

---

## 📸 Sample Chart

> Replace this with your own screenshot when ready

![Sample Chart](https://user-images.githubusercontent.com/placeholder/chart.png)

---

## 👤 Author

**Souvik Ray**  
📧 souvikray@live.com  
🔗 [LinkedIn](https://www.linkedin.com/in/souvik-ray-a74b93162/)

---

## 📌 Future Plans

- [ ] Add RSI, MACD, Bollinger Band strategies  
- [ ] Add Streamlit dashboard  
- [ ] Add real-time trade execution via SmartAPI  
- [ ] Add logging & backtest export to CSV  

---

## 📃 License

MIT — feel free to use, fork, and build on top of it.
