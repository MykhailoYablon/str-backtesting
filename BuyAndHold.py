from backtesting import Strategy

# 2. create a strategy class
class BuyAndHold(Strategy):
    risk_percent = 0.01
    take_profit_multiple = 10

    # what do we want to initialize at the beginning
    def init(self):
        print("going long")
        order = self.buy(size=100)

    def next(self):
        # get the timestamp and extract the date
        t = self.data.index[-1]
        current_bar_date = t.date()

        # Buying and holding everyday
        print(f"Position {self.position} and time {t.date()}")