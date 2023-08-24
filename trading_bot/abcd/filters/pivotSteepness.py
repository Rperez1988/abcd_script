
from abcd_script.trading_bot.abcd.tools.percente import calculatePercentageDifference
from abcd_script.trading_bot.abcd.pivot_screener.getMidOfEachCandle import getMidPointOfEachCandle
import statistics


def checkPivotSideSteepness(setting, close, open, length, percentageChange):

    match setting:

        case True:
            
            leftMidPoint, rightMidPoint = calculatePercentageDifference(close, open, length)

            if leftMidPoint:
                if rightMidPoint:
                    

                    LmidPoints = leftMidPoint[::-1]
                    leftSideAverage = float("%.2f"%statistics.mean(LmidPoints))

                    RmidPoints = rightMidPoint[::-1]
                    rightSideAverage = float("%.2f"%statistics.mean(RmidPoints))
         
                    if leftSideAverage >= percentageChange and rightSideAverage >= percentageChange :
               
                        calculatePercentageDifference(close, open, length)
    
    
                        return True, leftSideAverage, rightSideAverage

                    else:

                        return False, 0, 0

            
            else:
                return False, 0, 0

        case False:

            leftMidPoint, rightMidPoint = getMidPointOfEachCandle(close, open, length)

            if leftMidPoint:
                if rightMidPoint:

                    LmidPoints = leftMidPoint[::-1]
                    leftSideAverage = float("%.2f"%statistics.mean(LmidPoints))

                    RmidPoints = rightMidPoint[::-1]
                    rightSideAverage = float("%.2f"%statistics.mean(RmidPoints))
                
                    return True, leftSideAverage, rightSideAverage
            return True, 0, 0
