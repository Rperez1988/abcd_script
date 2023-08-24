from abcd_script.trading_bot.abcd.pivot_screener.getMidOfEachCandle import getMidPointOfEachCandle

def calculatePercentageDifference(close, open, length):

    leftMidPoint, rightMidPoint = getMidPointOfEachCandle(close, open, length)

    leftAverage     = []
    rightAverage    = []

    index = 0
    while index <= (len(leftMidPoint) - 2):

        a = (leftMidPoint[index] - leftMidPoint[index + 1])

        b = (leftMidPoint[index] + leftMidPoint[index + 1]) / 2

        c = (a / b) * 100

        change = c

        leftAverage.append(float("%.2f"%change))
        index +=1
   
    index = 0
    while index <= (len(rightMidPoint) - 2):

        a = (rightMidPoint[index] - rightMidPoint[index + 1])

        b = (rightMidPoint[index] + rightMidPoint[index + 1]) / 2

        c = (a / b) * 100

        change = c

        rightAverage.append(float("%.2f"%change))
        index +=1

    return(leftAverage,rightAverage)
       