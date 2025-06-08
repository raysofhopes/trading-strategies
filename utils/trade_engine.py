class TradeEngine:
    def __init__(self, api, data, capital=10000, allocation=0.2):
        self.api = api
        self.data = data
        self.initial_capital = capital
        self.allocated_capital = capital * allocation
        self.remaining_capital = self.allocated_capital
        self.trades = []
        self.executed_trades = []  # 🔥 NEW: store actual entry/exit pairs

    def simulate(self):
        position = 0
        entry_price = 0
        entry_date = None
        quantity = 0

        print("\n--- TRADE DETAILS ---")

        for index, row in self.data.iterrows():
            signal = row["signal"]
            price = row["close"]
            date = row["date"]

            if signal == 1 and position == 0:
                quantity = int(self.remaining_capital // price)
                if quantity == 0:
                    continue
                entry_price = price
                entry_date = date
                self.remaining_capital -= quantity * price
                position = quantity
                self.api.place_order("RELIANCE", "BUY")

            elif signal == -1 and position > 0:
                exit_price = price
                exit_date = date
                self.remaining_capital += position * exit_price
                pnl = (exit_price - entry_price) * position
                self.trades.append(pnl)

                # 🔥 Track the executed trade pair
                self.executed_trades.append({
                    "buy_date": entry_date,
                    "buy_price": entry_price,
                    "sell_date": exit_date,
                    "sell_price": exit_price,
                })

                print(f"{entry_date} BUY {position} @ ₹{entry_price:.2f} → {exit_date} SELL @ ₹{exit_price:.2f} | P&L: ₹{pnl:.2f}")

                position = 0

    def summary(self):
        total_trades = len(self.trades)
        wins = len([p for p in self.trades if p > 0])
        losses = total_trades - wins
        net_profit = sum(self.trades)
        final_capital = self.remaining_capital
        win_rate = (wins / total_trades) * 100 if total_trades > 0 else 0

        print("\n--- TRADE STATS ---")
        print(f"Total Trades: {total_trades}")
        print(f"Wins: {wins} | Losses: {losses}")
        print(f"Win Rate: {win_rate:.2f}%")
        print(f"Net P&L: ₹{net_profit:.2f}")
        print(f"Final Capital from ₹{self.allocated_capital:.2f}: ₹{final_capital:.2f}")
            