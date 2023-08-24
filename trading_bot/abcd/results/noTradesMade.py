def noTradesMade(stockName):

    results         = {}
    results['active']       = False
    results['stock']        = stockName
    results["total_open"]   = 0
    results["total_close"]  = 0
    results["total_won"]    = 0
    results["total_lost"]   = 0
    results["PnL"]          = 0
    results["strike_rate"]  = 0

    return results
