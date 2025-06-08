import pandas as pd
import ta  # Make sure 'ta' is installed: pip install ta

class RSIStrategy:
    def __init__(self, symbol, data):
        self.symbol = symbol
        self.data = data

    def generate_signals(self):
        df = self.data.copy()

        # Calculate RSI
        df["RSI"] = ta.momentum.RSIIndicator(df["close"], window=14).rsi()

        # Initialize signals
        df["signal"] = 0

        # Buy when RSI < 30
        df.loc[df["RSI"] < 40, "signal"] = 1

        # Sell when RSI > 60 (less strict to trigger exits)
        df.loc[df["RSI"] > 60, "signal"] = -1

        print(f"RSI Strategy: Buy signals = {df['signal'].eq(1).sum()}")
        print(f"RSI Strategy: Sell signals = {df['signal'].eq(-1).sum()}")

        print("RSI Strategy: Buy signals =", df[df["signal"] == 1]["date"].tolist())
        print("RSI Strategy: Sell signals =", df[df["signal"] == -1]["date"].tolist())

        return df