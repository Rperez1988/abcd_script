def getTradeCount(trades):

    open = 0 
    closed = 0

    for trade in trades:
        if trade.tradeInfo['tradeOpen'] == True:
            open += 1

        if trade.tradeInfo['tradeClosed'] == True:
            closed += 1
            
    return open, closed
