from abcd_script.trading_bot.abcd.filters.b_to_short_length import pivotTwotoTradeLength
from abcd_script.trading_bot.abcd.indicators.rsi.getPreviousRSIData import getPreviousRSIData
from abcd_script.trading_bot.abcd.indicators.rsi.getCurrentRSI import getLiveRSI

def checkFiltersBeforeTrade(filter, lengthSetting, pivotPairID, pivotPair, pivotTwotoShortLength, length, close, date):
    
    inLength = pivotTwotoTradeLength(lengthSetting, pivotPair, pivotTwotoShortLength, length)


    if inLength:
        if filter:
  
                
            getPreviousRSIData(pivotPair, close, date)
            getLiveRSI(pivotPair, date, close)

            return True
