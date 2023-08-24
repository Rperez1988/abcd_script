import sys
sys.path.append('../')
import abcd_script.trading_bot.abcd.strategy.strategy as strat

def getTradeResults():

    results = strat.allResults


    allTrades_ = []


    for each in strat.allTrades:
        
       
        trade = {

            'tradeInfo': each.tradeInfo,
            'pivotInfo': each.pivotInfo,
            'settings': each.settings,
            'pnl': each.pnl,
            'retracement': each.retracement,
            'duration': each.duration,
            'enterExitInfo': each.enterExitInfo,
            'movement': each.movement,
            'chartData' : each.chartData,
            'length': each.length
        

        }

        allTrades_.append(trade)

    return results, allTrades_

