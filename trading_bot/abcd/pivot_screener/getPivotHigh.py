from abcd_script.trading_bot.abcd.pivot_screener.getOpenAndCloseOfCandle import getOpenAndCloseOfCandle
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import get_high_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.comparePivotToSideBars import comparePivotHighToSideCandles


def get_pivot_high(dataClose, dataOpen, pivotLength: int, lowOfPivot, highOfPivot) -> bool:

    leftBarsVsPivotResult       = comparePivotHighToSideCandles(dataOpen,dataClose,pivotLength,highOfPivot, 'left')   
    rightBarsVsPivotResult      = comparePivotHighToSideCandles(dataOpen,dataClose,pivotLength,highOfPivot, 'right')  

    if False in leftBarsVsPivotResult or False in rightBarsVsPivotResult:
        return False

    elif False not in leftBarsVsPivotResult or False not in rightBarsVsPivotResult:
        return True
