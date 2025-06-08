class BaseStrategy:
    def __init__(self, symbol, data):
        self.symbol = symbol
        self.data = data

    def generate_signals(self):
        raise NotImplementedError("Implement in subclass")
