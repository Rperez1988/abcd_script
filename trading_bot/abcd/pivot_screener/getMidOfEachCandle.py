from abcd_script.trading_bot.abcd.pivot_screener.getOpenAndCloseOfPivot import getLeftAndRightOpenAndClosesOfPivot
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import get_high_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.getLowOfCandle import get_low_of_candle


def getMidPointOfEachCandle(close, open, length):

    leftMidPoint    = []
    rightMidPoint   = []

    rightSideOpen, rightSideClose, leftSideOpen, leftSideClose = getLeftAndRightOpenAndClosesOfPivot(close, open, length)


    for each in range(length):
   
        high = get_high_of_candle(leftSideOpen[each],leftSideClose[each])
        low  = get_low_of_candle(leftSideOpen[each],leftSideClose[each])

        leftMidNum = ((float(high) - float(low)) / 2) + float(low)
        leftMidPoint.append(float("%.2f"%leftMidNum))

    for each in range(length):

        high = get_high_of_candle(rightSideOpen[each],rightSideClose[each])
        low  = get_low_of_candle(rightSideOpen[each],rightSideClose[each])

        rightMidNum = (float(high) - float(low) / 2) + float(low)
        rightMidPoint.append(float("%.2f"%rightMidNum))

    return leftMidPoint, rightMidPoint
