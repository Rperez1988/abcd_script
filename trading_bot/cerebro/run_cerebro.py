import sys
sys.path.append('../')
import abcd_script.trading_bot.abcd.strategy.strategy as strat
from .data_manipulation.first_and_last_date_of_DF import get_first_and_last_data_of_DF
from .data_manipulation.csv_into_backtraderfeeds import csv_into_btfeeds
from abcd_script.trading_bot.abcd.strategy.strategy import *
import backtrader as bt


def prepareDataForStrategy(df,datapath):

    startYear,startMonth,startDays,endingYear,endingMonth,endingDays = get_first_and_last_data_of_DF(df)

    btFeed = csv_into_btfeeds(datapath,startYear,startMonth,startDays,endingYear,endingMonth,endingDays)

    return btFeed

def createCerebro(btFeed, strat, stockName, settings, pattern_A, pattern_AB, pattern_ABC, pattern_ABCD, full_scan, data_length):

 
    cerebro = bt.Cerebro(writer=False)
    cerebro.adddata(btFeed)
    cerebro.addstrategy(strat, 
            data_length = data_length,
            full_scan = full_scan,
            pattern_A = pattern_A,
            pattern_AB = pattern_AB,
            pattern_ABC = pattern_ABC,
            pattern_ABCD = pattern_ABCD,
            settingsName=settings['settingsName'],
            stockName=stockName, 
            market = settings['market'],
            pivotLength= settings['pivotLength'],
            rrr=settings['rrr'],
            sAndR=settings['s&r'],
            maxAtoBLength=settings['maxAtoBLength'],
            maxBtoCLength=settings['maxBtoCLength'],
            maxCtoDLength=settings['maxCtoDLength'],
            entryRSI=settings['entryRSI'],
            abnormalPriceJump=settings['abnormalPriceJump'],
            pivotSteepness=settings['pivotSteepness'],
            aBelowB=settings['aBelowB'],
        )
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
    cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")

    cerebro.run()
 
def runCerebro(stockDF, stockName, csvFilePath, settings, pattern_A, pattern_AB, pattern_ABC, pattern_ABCD, full_scan, data_length):

    btFeed = prepareDataForStrategy(stockDF, csvFilePath)
    
    createCerebro(btFeed, Three_Wave_Down_Trend, stockName, settings, pattern_A, pattern_AB, pattern_ABC, pattern_ABCD, full_scan, data_length)

    return strat.pattern_abcd, strat.pattern_abc, strat.pattern_ab, strat.pattern_a
    