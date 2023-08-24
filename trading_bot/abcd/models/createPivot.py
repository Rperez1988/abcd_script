from abcd_script.trading_bot.abcd.pivot_screener.getLowOfCandle import get_low_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import get_high_of_candle
from abcd_script.trading_bot.abcd.tools.getSuppAndResistOfPivot import get_support_and_resistance


# pivot, aORb, pivotType, a_pivots, b_pivots, date, length, close, high, low, open):
def createAorB(pivot, aORb, pivotType, a_pivots, b_pivots, date, length, close, high, low, open, isPaired):


    pivot.aORb                  = aORb
    pivot.length                = length
    pivot.pivotID               = len(a_pivots) if pivotType == 'High' else len(b_pivots) 
    pivot.date                  = date.date(ago=-length)
    pivot.lastCandleDate        = date.date(ago=0)
    pivot.type                  = pivotType
    pivot.snr                   = get_support_and_resistance(length, close)
    pivot.low                   = get_low_of_candle(high[-length],low[-length])
    pivot.high                  = get_high_of_candle(high[-length],low[-length])
    pivot.close                 = close[-length]
    pivot.open                  = open[-length]
    pivot.color                 = 'Red' if pivot.close < pivot.open else 'Green' 
    pivot.priceAtStart          = get_low_of_candle(high[-(length * 2)],low[-(length * 2)])
    pivot.priceAtEnd            = get_low_of_candle(high[0],low[0])      
    pivot.allPrices             = []
    pivot.days_passed           = 0
    pivot.pLtoShortDays         = 0
    pivot.tradeStartDate        = date.date(ago=-length * 2)
    pivot.aToBBars              = 0
    pivot.paired                = False

    for bar in range((length * 2) + 1):
        pivot.allPrices.append(close[-bar])

    return pivot
