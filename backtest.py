from backtesting import Backtest
from backtesting.test import GOOG
from SmaCross import SmaCross

bt = Backtest(GOOG, SmaCross, commission=.002)

bt.run()
bt.plot()