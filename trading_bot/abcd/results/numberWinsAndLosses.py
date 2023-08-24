
def winsAndLosses(allTrades):

    total_won = 0
    total_lost = 0
    for trade in allTrades:
        if trade.tradeInfo['tradeResult'] == "Win":
            total_won +=1
        elif trade.tradeInfo['tradeResult'] == "Lose":
            total_lost +=1


    return total_won, total_lost