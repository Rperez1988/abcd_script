def tradesMade(stockName, open, closed, wins, lost, pnl):

    totalTrades =  open + closed
    winRate = 0

    if wins == 0:
        winRate = 0
    
    else:
        winRate = (wins /totalTrades) * 100

    results = {}
    results['active']       = True
    results['stock']        = stockName
    results["total_open"]   = '%.2f' % open
    results["total_close"]  = '%.2f' % closed
    results["total_won"]    = '%.2f' % wins
    results["total_lost"]   = '%.2f' % lost
    results["PnL"]          = '%.2f' % sum(pnl)
    results["strike_rate"]  = '%.2f' % winRate



    return results
