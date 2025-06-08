import ta
from models.base_model import BaseStrategy

class MovingAverageStrategy(BaseStrategy):
    def generate_signals(self):
        self.data["SMA_5"] = self.data["close"].rolling(window=5).mean()
        self.data["SMA_20"] = self.data["close"].rolling(window=20).mean()
        self.data["RSI"] = ta.momentum.RSIIndicator(close=self.data["close"], window=14).rsi()

        self.data["signal"] = 0

        # Loosen condition: just SMA crossover
        self.data.loc[
            (self.data["SMA_5"] > self.data["SMA_20"]),
            "signal"
        ] = 1

        self.data.loc[
            (self.data["SMA_5"] < self.data["SMA_20"]),
            "signal"
        ] = -1

        # Optional: If you want to combine again later:
        # Add RSI filters like (RSI < 50 for buy) or (RSI > 50 for sell)

        return self.data