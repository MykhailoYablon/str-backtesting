from backtesting import Backtest, Strategy
from backtesting.test import GOOG
from BuyAndHold import BuyAndHold

import pandas as pd
# 1. read a csv of minute data, limit to the first month for now
df = pd.read_csv("data/GOOGL.csv", sep=';', parse_dates=['Date'], index_col='Date')

bt = Backtest(df, BuyAndHold, cash=25_000, commission=.002, finalize_trades=True)


# run the strategy
stats = bt.run()

# plot ths strategy
bt.plot()

print(stats)