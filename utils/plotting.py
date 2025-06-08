import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd


def plot_results(df, engine):
    # --- Executed Trades ---
    executed_df = pd.DataFrame(engine.executed_trades)
    if not executed_df.empty:
        executed_df["entry_date"] = pd.to_datetime(executed_df["entry_date"])
        executed_df["exit_date"] = pd.to_datetime(executed_df["exit_date"])

    # --- Capital Usage ---
    capital_df = pd.DataFrame(engine.capital_history)
    capital_df["date"] = pd.to_datetime(capital_df["date"])

    # --- Plotting Setup ---
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12), sharex=True, gridspec_kw={'height_ratios': [3, 1, 1]})

    # --- PRICE PLOT + TRADE MARKERS ---
    ax1.plot(df["date"], df["close"], label="Close Price", color="blue", linewidth=1.5)

    if not executed_df.empty:
        ax1.scatter(executed_df["entry_date"], executed_df["entry_price"], label="Buy", marker="^", color="green", s=60)
        ax1.scatter(executed_df["exit_date"], executed_df["exit_price"], label="Sell", marker="v", color="red", s=60)

    # Open buy positions
    if hasattr(engine, "positions") and engine.positions:
        open_df = pd.DataFrame(engine.positions)
        open_df["entry_date"] = pd.to_datetime(open_df["entry_date"])
        ax1.scatter(open_df["entry_date"], open_df["entry_price"], label="Open Buy", marker="o", color="orange", s=60, edgecolor="black")

    ax1.set_ylabel("Price (₹)")
    ax1.set_title("Executed Trades")
    ax1.grid(True)
    ax1.legend()

    # --- RSI PLOT ---
    ax2.plot(df["date"], df["RSI"], label="RSI", color="purple", linewidth=1.2)
    ax2.axhline(30, linestyle="--", color="red", linewidth=0.8, label="Oversold (30)")
    ax2.axhline(70, linestyle="--", color="green", linewidth=0.8, label="Overbought (70)")
    ax2.set_ylabel("RSI")
    ax2.set_ylim([0, 100])
    ax2.grid(True)
    ax2.legend()

    # --- REMAINING CASH PLOT ONLY ---
    ax3.plot(capital_df["date"], capital_df["cash"], label="Remaining Cash", color="black", linewidth=1.2)
    ax3.set_ylabel("₹")
    ax3.set_xlabel("Date")
    ax3.set_title("Cash Balance Over Time")
    ax3.grid(True)
    ax3.legend()

    # --- X-Axis Formatting ---
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax3.xaxis.set_major_locator(mdates.WeekdayLocator(interval=1))
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()