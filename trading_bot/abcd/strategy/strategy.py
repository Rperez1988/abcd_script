import backtrader as bt
from datetime import datetime
import sys
sys.path.append('../')
from abcd_script.trading_bot.abcd.filters.a_to_b_length import filter_getAtoBLength
from abcd_script.trading_bot.abcd.filters.preventBarsFromBack import preventPullingBarsFromBack
from abcd_script.trading_bot.abcd.filters.abnormalPriceJump import abnormalPriceJump
from abcd_script.trading_bot.abcd.filters.pivotSteepness import checkPivotSideSteepness
from abcd_script.trading_bot.abcd.filters.getRestrictionArea import filter_RestrictionArea
from abcd_script.trading_bot.abcd.filters.aBelowb import check_pivot_b_position
from abcd_script.trading_bot.abcd.pivot_screener.findPivot import findPivot
from abcd_script.trading_bot.abcd.pivot_screener.getLowOfCandle import get_low_of_candle
from abcd_script.trading_bot.abcd.models.createPivot import createAorB
from abcd_script.trading_bot.abcd.pivot_screener.findPivot import findPivot
from abcd_script.trading_bot.abcd.results.results import get_strategy_results
from abcd_script.trading_bot.abcd.results.gatherAllTrades import gatherAllTrades
from abcd_script.trading_bot.abcd.exit_signals.exitSignal1 import closeSignal
from abcd_script.trading_bot.abcd.enter_signals.sellSignal import isSupportAndResistanceHit
from abcd_script.trading_bot.abcd.enter_signals.checkFiltersBeforeTrade import checkFiltersBeforeTrade
from abcd_script.trading_bot.abcd.tools.setBeginTrading import setDateTestingCanStart
from abcd_script.trading_bot.abcd.models.createTrade import createTrade
from abcd_script.trading_bot.abcd.models.A_PivotSingle import A_PivotSingle
from abcd_script.trading_bot.abcd.models.AB_PivotPair import AB_PivotPair
from abcd_script.trading_bot.abcd.models.trade import Trade
from abcd_script.trading_bot.abcd.models.ABC_PivotTrio import ABC_PivotTrio
from abcd_script.trading_bot.abcd.models.ABCD_PivotQuad import ABCD_PivotQuad
from abcd_script.trading_bot.abcd.models.ABCD_Open import ABCD_Open
from abcd_script.trading_bot.abcd.strategy.check_for_pivot_B import *
from abcd_script.trading_bot.abcd.strategy.check_for_pivot_C import *
from abcd_script.trading_bot.abcd.strategy.check_for_pivot_D import *
from abcd_script.trading_bot.abcd.strategy.abcd_entry import *
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import *
from abcd_script.trading_bot.abcd.indicators.rsi .getPreviousRSIData import *

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
from typing import List, Dict

settings        = {'length': None, 'support&resistance': None, }
closedTrades    = []
openTrades      = []
allResults      = []
chartData       = []
allTrades       = []

class Three_Wave_Down_Trend(bt.Strategy):

    params = dict(
        settingsName=None,
        stockName = None,
        market = None,
        pivotLength=None,
        rrr=None,
        sAndR=None,
        maxAtoBLength=None,
        maxBtoCLength=None,
        maxCtoDLength=None,
        entryRSI=None,
        abnormalPriceJump=None,
        pivotSteepness=None,
        aBelowB=None,
    )

    def __init__(self) -> None:      

        del chartData[:]
        del allTrades[:]
        del allResults[:]

        self.index = 0
        self.counter: int = 0   
        self.first_close_price_counter = 0
        self.first_close_price = None
        self.dateCanStart: str = None
        self.a_pivots: list = []
        self.b_pivots: list = []
        self.c_pivots: list = []
        self.d_pivots: list = []
        self.matched_pivot_ones: list = []
        self.openTrades: dict = {}
        self.chartData: list = []
        self.ab_pivotPairs: list = []
        self.abc_pivotTrios: list = []
        self.abcd_pivotQuads: list = []
        self.open_ABCDs: list = []
        self.stockName: str  = self.params.stockName
        self.c = 0
        self.settings: dict = {
            'settingsName': self.params.settingsName,
            'market': self.params.market,
            'pivotLength': int(self.params.pivotLength),
            'rrr': 1,
            's&r': 'average',
            'maxAtoBLength': '60',
            'maxBtoCLength': 'Off',
            'maxCtoDLength': 'Off',
            'entryRSI': 30,
            'abnormalPriceJump': 'Off',
            'pivotSteepness':  [False,1],
            'aBelowB':'true',
            'inRestrictionArea': True,
            'barsFromBack': True,
        }

    def next(self) -> None:

        def printEachBarDate():
            one = 0
            if(one == 0):
                one+=1
                print(self.datas[0].datetime.date(ago=0))

        def get_bars_from_previous_pivot(previous_pivot_date, date, pivot_length):
   

            i = pivot_length

            while str(previous_pivot_date) <= str(date(ago=-i)):

                if str(previous_pivot_date) == '2022-09-14':
                    if(str(date(ago=-1)) == '2022-09-26'):

                        print('a_date',previous_pivot_date, 'current_candle',date(ago=-i), 'candle_number: ', i)
              
                i+=1
            
            return i - 1
        
        def check_for_pivot_A():
              
            pivotType = findPivot(self.data_close, self.data_open, self.settings['pivotLength'], self.settings['market'])

            if pivotType:
              
                isAbnormalPriceJump = abnormalPriceJump(self.settings['abnormalPriceJump'],self.settings['pivotLength'], self.data_open, self.data_close)
                
                if isAbnormalPriceJump:

                    result, leftSideAverage, rightSideAverage = checkPivotSideSteepness(self.settings['pivotSteepness'][0],self.data_open, self.data_close, self.settings['pivotLength'],  self.settings['pivotSteepness'][1])
                    if result: 

                        pivotID = len(self.a_pivots)
                        pivotLetter = 'A'
                        pivotColor = 'Red'
                        # paired = False
                        pivotDate = self.datas[0].datetime.date(ago=-self.settings['pivotLength'])
                        open = self.data_open[-self.settings['pivotLength']]
                        high = self.data_high[-self.settings['pivotLength']]
                        low = self.data_low[-self.settings['pivotLength']]
                        close = self.data_close[-self.settings['pivotLength']]
                        startDate = self.datas[0].datetime.date(ago=-(self.settings['pivotLength'] * 2))
                        endDate = self.datas[0].datetime.date(ago=0)
                        barsSincePreviousPivot = 0
                        daysSincePreviousPivot = 0
                        retracementPct = None
                        retracementPrice = None

                        pivot = A_PivotSingle(
                            pivotID,
                            pivotLetter,
                            pivotColor,
                            # paired,
                            pivotDate,
                            open,
                            high,
                            low,
                            close,
                            startDate,
                            endDate,
                            barsSincePreviousPivot,
                            daysSincePreviousPivot,
                            retracementPct,
                            retracementPrice,
                            self.settings['pivotLength']
              
                    
                            
                        )
                     
                        self.a_pivots.append(pivot)

        def check_for_pivot_B():

            for pivot_A in self.a_pivots:

                pivot_A.basicInfo['full_length'] += 1
                
                pivot_A.duration['bars_passed'] += 1

                is_B_found = find_B(self.settings['market'], self.data_close, self.data_open, self.settings['pivotLength'])
                
                if is_B_found:
                    
                    pivot_B = create_B(
                        self.b_pivots, 
                        self.datas[0].datetime.date, 
                        self.settings['pivotLength'], 
                        self.data_high, 
                        self.data_open, 
                        self.data_close, 
                        self.data_low,
                        self.settings['pivotLength']
                    )

                    is_ab_correct = check_ab_is_start_of_abcd(self.settings['market'], pivot_A, pivot_B)
                            
                    if is_ab_correct:

                        add_b_with_group_of_b(self.b_pivots, pivot_B)

                        # days_between_A_and_B = get_days_between_A_and_B(self.datas[0].datetime.date,self.settings['pivotLength'], pivot_A)

                        # bars_between_A_and_B = get_bars_from_previous_pivot(pivot_A.pivotInfo['pivotDate'], self.datas[0].datetime.date, self.settings['pivotLength'])
                                        
                        is_A_the_lowest = check_if_A_is_the_lowest(pivot_A.duration['bars_passed'], self.data_high, self.data_low, pivot_A)

                        is_A_the_highest = check_if_A_is_the_highest(pivot_A.duration['bars_passed'], self.data_high, self.data_low, pivot_A)

                        is_B_the_lowest = check_if_B_is_the_lowest(pivot_A.duration['bars_passed'], self.data_open, self.data_close, pivot_B)

                        is_B_the_highest = check_if_B_is_the_highest(pivot_A.duration['bars_passed'], self.data_high, self.data_low, pivot_B)

                        is_correct_shape = check_if_A_to_B_is_correct_shape(self.settings['market'], is_A_the_highest, is_B_the_lowest, is_A_the_lowest,is_B_the_highest)

                        if is_correct_shape:
                            
                            pivotPairID = len(self.ab_pivotPairs)

                            pivot_B.duration['barsSincePreviousPivot'] = pivot_A.duration['bars_passed']

                            # pivot_B.duration['daysSincePreviousPivot'] = days_between_A_and_B

                            ab_pivotPair = AB_PivotPair(pivot_A, pivot_B, pivotPairID , pivot_A.basicInfo['full_length'])

                            self.matched_pivot_ones.append(pivot_A.pivotInfo['pivotDate'])

                            self.ab_pivotPairs.append(ab_pivotPair)
                
        def check_for_pivot_C():
          
            for pivotPairID, pivotPair in enumerate(self.ab_pivotPairs):

                open = pivotPair.pivot_A.pivotInfo['open']
                close  = pivotPair.pivot_A.pivotInfo['close']
                high = get_high_of_candle(open, close)

                b_open = pivotPair.pivot_B.pivotInfo['open']
                b_close  = pivotPair.pivot_B.pivotInfo['close']
                b_low = getLowOfCandle(b_open, b_close)
                

                current_open = self.data_open[0]
                current_close = self.data_close[0]
                current_high = get_high_of_candle(current_open, current_close)
                current_low = getLowOfCandle(current_open, current_close)
                self.data_close[0]
                if current_high > high:
                    self.ab_pivotPairs.remove(pivotPair)

                elif current_low < b_low:
                    self.ab_pivotPairs.remove(pivotPair)
                
                
                pivotPair.full_length += 1

                pivotPair.bars_passed += 1 

                is_C_found = findPivot(self.data_close, self.data_open, int(self.settings['pivotLength']), self.settings['market'])

                if is_C_found:

                    pivot_C = create_pivot_c(
                        len(self.c_pivots), 
                        pivotPair.bars_passed, 
                        self.datas[0].datetime.date, 
                        int(self.settings['pivotLength']), 
                        self.data_high, 
                        self.data_open, 
                        self.data_close, 
                        self.data_low, 
                        pivotPair,
                        1
                        )

                    if pivotPair.pivot_A.duration['bars_passed'] > pivotPair.bars_passed:

                        c_position = None
                        b_position = None

                        if self.settings['market'] == 'Bull':
                            c_position, b_position = is_B_and_C_Low_and_High(pivot_C, pivotPair, pivotPair.bars_passed, self.data_open, self.data_close )

                        if self.settings['market'] == 'Bear':
                            c_position, b_position = is_b_high_and_c_low(pivot_C, pivotPair, pivotPair.bars_passed, self.data_open, self.data_close)
                        
                        if c_position and b_position:       
                            
                            retracement_ = None

                            if self.settings['market'] == 'Bull':

                                retracement_ = get_bull_retracement(pivot_C, pivotPair)

                            elif self.settings['market'] == 'Bear':

                                retracement_ = get_bear_retracement(pivot_C, pivotPair)
                                #  38.2% to 78.6% 

                            # if float(retracement_) > 30 and float(retracement_) < 90:
                            if float(retracement_) >= 1 and float(retracement_) <= 100:

                                c_shape = None
                                b_shape = None

                                if self.settings['market'] == 'Bear':

                                    c_shape, b_shape = check_bear_shape(pivot_C, pivotPair)

                                if self.settings['market'] == 'Bull':

                                    c_shape, b_shape = check_bull_shape(pivot_C, pivotPair)

                                if c_shape and b_shape:
            
                                    pivotTrio_ID = len(self.abc_pivotTrios)

                                    bToC_pctInBars = (pivotPair.bars_passed  / pivotPair.pivot_A.duration['bars_passed']) * 100

                                    pivotTrio = ABC_PivotTrio(
                                        pivotTrio_ID, 
                                        pivotPair.pivot_A, 
                                        pivotPair.pivot_B, 
                                        pivot_C, 
                                        pivotPair.bars_passed , 
                                        pivotPair,
                                        # retracement_, 
                                        bToC_pctInBars,
                                        pivotPair.full_length,
                                        
                                    )

                                    self.abc_pivotTrios.append(pivotTrio)
                                    self.c_pivots.append(pivot_C)

        def check_for_pivot_D():

            for pivotTrioID, pivotTrio in enumerate(self.abc_pivotTrios):

                open = pivotTrio.pivot_C.pivotInfo['open']
                close  = pivotTrio.pivot_C.pivotInfo['close']
                high = get_high_of_candle(open, close)

                # b_open = pivotTrio.pivot_B.pivotInfo['open']
                # b_close  = pivotTrio.pivot_B.pivotInfo['close']
                # b_low = getLowOfCandle(b_open, b_close)
                

                current_open = self.data_open[0]
                current_close = self.data_close[0]
                current_high = get_high_of_candle(current_open, current_close)
                # current_low = getLowOfCandle(current_open, current_close)

                if current_high > high:
                    self.abc_pivotTrios.remove(pivotTrio)

                # elif current_low < b_low:
                #     self.ab_pivotPairs.remove(pivotTrio)
                

                pivotTrio.full_length += 1      

                pivotTrio.bars_passed += 1

                bars_between_C_and_D = pivotTrio.bars_passed 
         
                d_to_b_retracement = get_d_to_b_retracement(self.settings['market'], pivotTrio, self.data_low[0], self.data_high[0])

                d_to_a_retracement = get_d_to_a_retracement(self.settings['market'], pivotTrio, self.data_low[0], self.data_high[0])

                # bars_between_C_and_D = get_bars_from_previous_pivot(pivotTrio.pivot_C.pivotInfo['pivotDate'],  self.datas[0].datetime.date, self.settings['pivotLength'])

                a_to_b_bar_length = pivotTrio.pivot_B.duration['barsSincePreviousPivot']

                
                c_to_d_retracment = (bars_between_C_and_D / a_to_b_bar_length) * 100


                # Retracement: ab bar-length, bc bar-length, cd bar-length
                # Retracement: ab price-length, bc price-length, cd price-length

                # measuring cd bar-length.
                if c_to_d_retracment >= 60 and c_to_d_retracment <= 140:
                    
                    # measuring cd prince-length compared to ab price-length
                    # if(float(d_to_a_retracement) > 110) and float(d_to_a_retracement) < 180:
                    if(float(d_to_a_retracement) >= 101) and float(d_to_a_retracement) <= 500:
                
                        c_position = get_c_position(self.settings['market'], bars_between_C_and_D, pivotTrio, self.data_open, self.data_close)

                        d_position = get_d_position(self.settings['market'], bars_between_C_and_D, pivotTrio, self.data_open, self.data_close)

                        if c_position and d_position:

                            if not pivotTrio.found_D:
                          

                                closes = getCloses(self.data_close, self.index)

                                dates = getDates(self.datas[0].datetime, self.index)

                                close_prices = []

                                for each in closes:
                                    close_prices.append(each['Close'])
                            
                                df = getPandasRSI(closes, dates)
                                
                                last_rsi = df.iloc[-1]['rsi']

                                pivotTrio.found_D = True  
                            
                                pivot_D = create_d(
                                    len(self.d_pivots), 
                                    self.datas[0].datetime.date, 
                                    self.data_high, 
                                    self.data_open, 
                                    self.data_close, 
                                    self.data_low, 
                                    bars_between_C_and_D, 
                                    pivotTrio,
                                    pivotTrio.full_length

                                )

                                self.d_pivots.append(pivot_D)

                                

                                abcd = create_ABCD(
                                    len(self.abcd_pivotQuads), 
                                    pivotTrio, 
                                    pivot_D, 
                                    d_to_a_retracement, 
                                    last_rsi,
                                    pivotTrio.full_length - 1,
                                    )
                                
                                self.abcd_pivotQuads.append(abcd)

        def check_for_abcd_entry(market):
            
            for abcdID, abcd in enumerate(self.abcd_pivotQuads):

                enterDate = self.datas[0].datetime.date(ago=0)

                entry_price = get_entry_price(market, self.data_low, self.data_high)

                risk, reward = get_risk_and_reward(market, abcd, entry_price, self.settings['rrr'])

                takeProfit = entry_price + reward

                stopLoss = entry_price - risk
        
                a = get_high_of_candle(float(abcd.pivot_A.pivotInfo['open']), float(abcd.pivot_A.pivotInfo['close']))
                b = get_low_of_candle(float(abcd.pivot_B.pivotInfo['open']), float(abcd.pivot_B.pivotInfo['close']))
                c = get_high_of_candle(float(abcd.pivot_C.pivotInfo['open']), float(abcd.pivot_C.pivotInfo['close']))
                d = get_high_of_candle(float(abcd.pivot_D.pivotInfo['open']), float(abcd.pivot_D.pivotInfo['close']))

                ab = a - b
                cb = c - b
                cd = c - d

                bc_retracement ='%.2f'%((cb / ab ) * 100)
                cd_retracement ='%.2f'%((cd / cb ) * 100)

                
                full_length = int(abcd.full_length) 

                prev_bars_volume = []

                for each in range(full_length):
                    prev_bars_volume.append(self.datas[0].volume[-each])

                
                d_volume =  prev_bars_volume[0]

                prev_bars_volume = prev_bars_volume[1:]

                prev_bars_volume.reverse()

                average_volume = sum(prev_bars_volume) / len(prev_bars_volume)

                percentage_change = ((d_volume - average_volume) / average_volume) * 100

                

                openTradeABCD = ABCD_Open(
                    abcdID,
                    self.stockName,
                    self.data_close[0],
                    abcd.pivot_A,
                    abcd.pivot_B,
                    abcd.pivot_C,
                    abcd.pivot_D,
                    self.settings,
                    abcd.barsBetweenBandC,
                    abcd.abc_pivotTrio.ab_pivotPair,
                    0,
                    abcd.pivot_D.duration['barsSincePreviousPivot'],
                    abcd.pivot_B.duration['barsSincePreviousPivot'],
                    self.datas[0].datetime.date(0),
                    abcdID,
                    entry_price,
                    reward,
                    risk,
                    takeProfit,
                    stopLoss,
                    enterDate,
                    'Live',
                    abcd.d_to_a_retracement,
                    bc_retracement, 
                    abcd.rsi,
                    self.datas[0].volume[0],
                    (abcd.pivot_B.duration['barsSincePreviousPivot'] + 2),
                    abcd.full_length,
                    prev_bars_volume,
                    average_volume,
                    percentage_change,
                    
                    )

                is_this_abcd_already_in_trade = checkIfQuadIsAlreadyInATrade(self.open_ABCDs, abcdID)
                
                if not is_this_abcd_already_in_trade:

                    todaysDate = self.datas[0].datetime

                    chartData = openTradeABCD.getOHLCChartData(
                        todaysDate,
                        self.data_open, 
                        self.data_high, 
                        self.data_low, 
                        self.data_close
                    )
                    
                    openTradeABCD.chartData = chartData   

                    self.open_ABCDs.append(openTradeABCD)

                    allTrades.append(openTradeABCD)      

        def check_for_abcd_exit():

            for each in allTrades:

                if each.tradeInfo['tradeOpen'] == True:

                    each.tradeInfo['tradeDuration'] += 1
                    
                    low = get_low_of_candle(self.data_open[0], self.data_close[0])
                    
                    if low < float(each.tradeInfo['lowest_price_dropped']):
                        each.tradeInfo['lowest_price_dropped'] = str(low)

                    
                    todaysOpen = self.data_open[0]
                    todaysClose = self.data_close[0]

                    takeProfilt = round(float(each.pnl['takeProfit']),2)
                    stopLoss = round(float((each.pnl['stopLoss'])),2)

                    openPassedTakeProfit = todaysOpen > takeProfilt
                    closePassedTakeProfit = todaysClose > takeProfilt

                    openPassedStopLoss = todaysOpen < stopLoss
                    closePassedStopLoss = todaysClose < stopLoss

                    openOrClosedPassedTakeProfit = openPassedTakeProfit or closePassedTakeProfit
                    openOrClosedPassedStopLoss = openPassedStopLoss or closePassedStopLoss

                    if openOrClosedPassedTakeProfit or openOrClosedPassedStopLoss:

                        each.tradeInfo['tradeOpen'] = False
                        each.tradeInfo['tradeClosed'] = True
                        each.tradeInfo['tradeCloseDate'] = str(self.datas[0].datetime.date(ago=0))
                        each.enterExitInfo['exitDate'] = str(self.datas[0].datetime.date(ago=0))
                        todaysDate = datetime.strptime(str(self.datas[0].datetime.date(ago=0)), "%Y-%m-%d")
                        enteredDate = datetime.strptime(each.enterExitInfo['enterDate'], "%Y-%m-%d")
                        # duration = str(todaysDate - enteredDate)
                        # sep = ' '
                        # duration = duration.split(sep, 1)[0]
                        
                        # each.tradeInfo['tradeDuration'] = str(duration)
                        
                        if openOrClosedPassedTakeProfit:
                            each.pnl['pnl'] = each.pnl['reward']
                            each.tradeInfo['tradeResult'] = 'Win'
                            each.enterExitInfo['exitPrice'] = str(each.pnl['takeProfit'])
                            each.pnl['returnPercentage'] = '%.2f'%((float(each.pnl['reward']) / float(each.enterExitInfo['enterPrice'])) * 100)
                        
                        if openOrClosedPassedStopLoss:
                            each.pnl['pnl'] =each.pnl['risk']
                            each.tradeInfo['tradeResult'] = 'Loss'
                            each.enterExitInfo['exitPrice'] = str(each.pnl['stopLoss'])
                            each.pnl['returnPercentage'] = '-' + '%.2f'%((float(each.pnl['risk']) / float(each.enterExitInfo['enterPrice'])) * 100)

                    # Get chart data.
                    chartData = each.getOHLCChartData(
                        self.datas[0].datetime, 
                        self.data_open, 
                        self.data_high, 
                        self.data_low, 
                        self.data_close
                    )
                    
                    each.chartData = chartData     





        printEachBarDate()

        self.counter, self.dateCanStart = setDateTestingCanStart(self.counter, self.dateCanStart, self.settings['pivotLength'], self.datas[0].datetime)

        self.index += 1

        if preventPullingBarsFromBack(self.settings['barsFromBack'], str(self.datas[0].datetime.date(0)), self.dateCanStart):
            
            check_for_pivot_A()

            check_for_pivot_B()    

            check_for_pivot_C()  

            check_for_pivot_D()

            check_for_abcd_entry(self.settings['market'])
            
            check_for_abcd_exit()

    def stop(self):
        
        # for i in reversed(range(len(allTrades))):
        #     if allTrades[i].tradeInfo['tradeClosed']:
        #         del allTrades[i]

        new_list = []

        for each in allTrades:
            new_list.append(
            {
                'id': each.tradeInfo['id'],
                'number': None,
                'list': [
                    each.pivotInfo['pivotA']['date'],
                    each.pivotInfo['pivotB']['date'],
                    each.pivotInfo['pivotC']['date'],
                    each.pivotInfo['pivotD']['date']
                    ]
            })

        class UnionFind:
            def __init__(self):
                self.parent = {}
                self.rank = {}

            def find(self, x):
                if x != self.parent[x]:
                    self.parent[x] = self.find(self.parent[x])
                return self.parent[x]

            def union(self, x, y):
                x_root = self.find(x)
                y_root = self.find(y)

                if x_root != y_root:
                    if self.rank[x_root] < self.rank[y_root]:
                        self.parent[x_root] = y_root
                    elif self.rank[x_root] > self.rank[y_root]:
                        self.parent[y_root] = x_root
                    else:
                        self.parent[y_root] = x_root
                        self.rank[x_root] += 1

        def assign_numbers(original_lists):
            uf = UnionFind()

            for i, lst in enumerate(original_lists):
                uf.parent[i] = i
                uf.rank[i] = 0

            for i in range(len(original_lists)):
                for j in range(i + 1, len(original_lists)):
                    if any(string in original_lists[j]['list'] for string in original_lists[i]['list']):
                        uf.union(i, j)

            groups = {}
            for i in range(len(original_lists)):
                root = uf.find(i)
                if root not in groups:
                    groups[root] = len(groups) + 1

            result = []
            for i, lst in enumerate(original_lists):
                root = uf.find(i)
                result.append({'id': lst['id'], 'number': groups[root], 'list': lst['list']})

            return result
       
        result = assign_numbers(new_list)

        for trade in allTrades:
            for each in result:
                if trade.tradeInfo['id'] == each['id']:
                    trade.tradeInfo['pivot_number'] = each['number']

        chartData.append(self.chartData)

        gatherAllTrades(self.openTrades, allTrades)    

        results = get_strategy_results(allTrades, self.stockName)

        allResults.append(results)

        print('a ',len(self.a_pivots))
        print('b ',len(self.ab_pivotPairs))
        print('c ',len(self.abc_pivotTrios))
        print('d ',len(self.abcd_pivotQuads))
        print('trades: ', len((allTrades)))

