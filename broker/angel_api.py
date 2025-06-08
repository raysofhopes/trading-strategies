import os
from dotenv import load_dotenv

load_dotenv()

class AngelAPI:
    def __init__(self, paper_mode=True):
        self.paper_mode = paper_mode
        self.api_key = os.getenv("API_KEY")
        self.client_id = os.getenv("CLIENT_ID")
        self.secret_key = os.getenv("SECRET_KEY")

    def place_order(self, symbol, side):
        if self.paper_mode:
            print(f"[PAPER TRADE] {side} order simulated for {symbol}")
            with open("logs/trade_log.txt", "a") as f:
                f.write(f"Simulated {side} on {symbol}\n")
        else:
            print(f"[LIVE TRADE] {side} order placed for {symbol}")
            # Here you would integrate with the real AngelOne API