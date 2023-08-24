from abcd_script.trading_bot.abcd.pivot_screener.getOpenAndCloseOfCandle import getOpenAndCloseOfCandle
from abcd_script.trading_bot.abcd.pivot_screener.getLowOfCandle import get_low_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.comparePivotToSideBars import comparePivotLowToSideCandles

def get_pivot_low(dataClose, dataOpen, pivotLength: int, lowOfPivot, highOfPivot) -> bool:

    leftBarsVsPivotResult       = comparePivotLowToSideCandles(dataOpen,dataClose,pivotLength,lowOfPivot, 'left')   
    rightBarsVsPivotResult      = comparePivotLowToSideCandles(dataOpen,dataClose,pivotLength,lowOfPivot, 'right')  

    
    if False in leftBarsVsPivotResult or False in rightBarsVsPivotResult:
        return False

    elif False not in leftBarsVsPivotResult or False not in rightBarsVsPivotResult:
        return True
