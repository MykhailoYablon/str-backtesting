from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from SmaCross import SmaCross

import pandas as pd
# 1. read a csv of minute data, limit to the first month for now
df = pd.read_csv("GOOGL.csv", sep=';', parse_dates=['Date'], index_col='Date')

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

bt = Backtest(df, BuyAndHold, cash=25_000, commission=.002, finalize_trades=True)


# run the strategy
stats = bt.run()

# plot ths strategy
bt.plot()

print(stats)