from .prepare_data import prepareDataForStrategy
from .create_cerebro import createCerebro
from .trade_results import getTradeResults
import sys
sys.path.append('../')
from abcd_script.trading_bot.abcd.strategy.strategy import *

def runCerebro(stockDF, stockName, csvFilePath, settings):

    btFeed = prepareDataForStrategy(stockDF, csvFilePath)
    
    createCerebro(btFeed, Three_Wave_Down_Trend, stockName, settings)

    totalStatistics, allTrades = getTradeResults()

    return totalStatistics, allTrades
    




