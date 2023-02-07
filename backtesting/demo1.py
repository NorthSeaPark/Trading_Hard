from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import talib as ta

print(GOOG)

class RsiOscillator(Strategy):

    def init(self):
        self.rsi = self.I(ta.RSI, self.data.Close, 14)

    def next(self):
