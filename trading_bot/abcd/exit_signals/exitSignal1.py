def closeSignal(trade, filter, close,open):

    if trade.closingTradeType == 'Bull':

        
        if close[0] > float(trade.takeProfit) and open[0] > float(trade.takeProfit):
     
            return 'Win'

        if close[0] < float(trade.stopLoss) and open[0] < float(trade.stopLoss):

            return 'Loss'


    elif trade.closingTradeType == 'Bear':


        if close[0] < float(trade.takeProfit) and open[0] < float(trade.takeProfit):
            return 'Win'

        if close[0] > float(trade.stopLoss) and open[0] > float(trade.stopLoss):
            return 'Loss'

  

