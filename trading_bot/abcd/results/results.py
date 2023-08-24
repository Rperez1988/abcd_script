from abcd_script.trading_bot.abcd.results.tradeCount import getTradeCount
from abcd_script.trading_bot.abcd.results.numberWinsAndLosses import winsAndLosses
from abcd_script.trading_bot.abcd.results.noTradesMade import noTradesMade
from abcd_script.trading_bot.abcd.results.tradesMade import tradesMade


def get_strategy_results(allTrades, stockName):

    open,closed = getTradeCount(allTrades)
    wins, lost = winsAndLosses(allTrades)
    
    pnl = []
    for each in allTrades:
        pnl.append(float('%.2f'% float(each.pnl['pnl'])))
  

    if ((open + closed) == 0):
        print(stockName, open + closed ,'No Trades Were Made!')
        return noTradesMade(stockName)

    if ((open + closed) > 0):
        print(stockName,open + closed ,'Trades Made!')
        results = tradesMade(stockName, open, closed, wins, lost, pnl)
        return results

