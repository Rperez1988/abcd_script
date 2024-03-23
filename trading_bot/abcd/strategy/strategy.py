import backtrader as bt
import sys
sys.path.append('../')
from abcd_script.trading_bot.abcd.filters.preventBarsFromBack import preventPullingBarsFromBack
from abcd_script.trading_bot.abcd.tools.setBeginTrading import setDateTestingCanStart
from abcd_script.trading_bot.abcd.strategy.abcd_entry import *
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import *
from abcd_script.trading_bot.abcd.indicators.rsi .getPreviousRSIData import *
from abcd_script.trading_bot.abcd.strategy.check_for_patterns import *
from abcd_script.trading_bot.abcd.strategy.Pattern_Models import *
from abcd_script.trading_bot.abcd.strategy.end_tasks import *

allResults      = []
chartData       = []
allTrades       = []
a_pivots = []

# PATTERNS
pattern_a = []
pattern_ab = []
pattern_abc = []
pattern_abcd = []

class Three_Wave_Down_Trend(bt.Strategy):

    # DELCARE INCOMING PARAMS
    params = dict(
        data_length = None, 
        full_scan = None,
        pattern_A = None,
        pattern_AB = None,
        pattern_ABC = None,
        pattern_ABCD = None,
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
        candle_ids=None,
    )
    
    def __init__(self) -> None:      

        # CLEAR PREVIOUS DATA SET
        del chartData[:]
        del allTrades[:]
        del allResults[:]
        del a_pivots[:]
        del pattern_a[:]
        del pattern_ab[:]
        del pattern_abc[:]
        del pattern_abcd[:]

        # INITIALIZE STRATEGY VARIABLES
        self.candle_ids = self.params.candle_ids
        self.counter: int = 0   
        self.dateCanStart: str = None

        self.total_bars = self.params.data_length


        
        self.b_pivots: list = []
        self.c_pivots: list = []
        self.d_pivots: list = []
        self.matched_pivot_ones: list = []
        self.openTrades: dict = {}
        self.chartData: list = []

        # Full Scan
        self.full_scan = self.params.full_scan

        # PATTERNS
        # self.a_pivots: list = []
        # self.ab_pivotPairs: list = []
        # self.abc_pivotTrios: list = []
        # self.pattern_abcd = list = []

        self.a_pivots: list = self.params.pattern_A
        self.ab_pivotPairs: list = self.params.pattern_AB
        self.abc_pivotTrios: list = self.params.pattern_ABC
        self.pattern_abcd = list = self.params.pattern_ABCD


        self.trade_symbol: str  = self.params.stockName
        self.settings: dict = {
            'candle_ids': self.params.candle_ids,
            'settingsName': self.params.settingsName,
            'market': 'Bull',
            'pivotLength': int(1),
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
        self.failed_pivot_trio = []
        self.failed_AB_patterns = []
    
    def next(self) -> None:

        def printEachBarDate():
                one = 0
                if(one == 0):
                    print(self.datas[0].datetime.date(ago=0),self.data_close[0])

                    one+=1
            
        if self.full_scan:

            printEachBarDate()
            

            # PREVENT FROM PULLING CANDLES FROM BACK OF DATA SET
            self.counter, self.dateCanStart = setDateTestingCanStart(self.counter, self.dateCanStart, self.settings['pivotLength'], self.datas[0].datetime)
            if preventPullingBarsFromBack(self.settings['barsFromBack'], str(self.datas[0].datetime.date(0)), self.dateCanStart):
                    
                check_for_pivot_A(
                    self.datas[0].datetime.date,
                    self.data_close,
                    self.data_open,
                    1,
                    self.settings['market'],
                    self.settings['abnormalPriceJump'],
                    self.settings['pivotSteepness'],
                    self.a_pivots,
                    self.data_high,
                    self.data_low,
                    self.trade_symbol 
                )

                check_for_pivot_B(
                    self.a_pivots,
                    self.datas[0].datetime.date,
                    self.settings['market'],
                    self.data_close,
                    self.data_open,
                    1,
                    self.data_low,
                    self.data_high,
                    self.matched_pivot_ones,
                    self.ab_pivotPairs,
                    self.failed_AB_patterns,
                    self.trade_symbol
                )
                    
                check_for_pivot_C(
                    self.ab_pivotPairs,
                    self.datas[0].datetime.date,
                    self.data_close,
                    self.data_open,
                    1,
                    self.settings,
                    self.data_high,
                    self.data_low,
                    self.settings['market'],
                    self.abc_pivotTrios,
                    self.trade_symbol
                
                )
                    
                check_for_pivot_D(
                    self.abc_pivotTrios,
                    self.settings['market'],
                    self.data_low[0],
                    self.data_high[0],
                    self.datas[0].datetime.date,
                    self.data_open,
                    self.data_close,
                    self.pattern_abcd,
                    self.trade_symbol    
                )
                    
                enter_trade(
                    self.pattern_abcd,
                    self.datas[0].datetime.date,
                    self.datas[0].volume,
                    self.settings['market'],
                    self.data_low,
                    self.data_high,
                    self.settings['rrr'],
                
                    )
        
                exit_trade(
                    self.pattern_abcd,
                    self.data_open,
                    self.data_close,
                    self.datas[0].datetime.date,
                    self.data,
                    self.settings['settingsName'],


                    )

        elif not self.full_scan:   

            if len(self.data) == self.total_bars - 1:

                printEachBarDate()

                # print(len(self.data),self.total_bars,  str(self.datas[0].datetime.date(ago=0)))
                
                check_for_pivot_A(
                    self.datas[0].datetime.date,
                    self.data_close,
                    self.data_open,
                    1,
                    self.settings['market'],
                    self.settings['abnormalPriceJump'],
                    self.settings['pivotSteepness'],
                    self.a_pivots,
                    self.data_high,
                    self.data_low,
                    self.trade_symbol 
                )

                check_for_pivot_B(
                    self.a_pivots,
                    self.datas[0].datetime.date,
                    self.settings['market'],
                    self.data_close,
                    self.data_open,
                    1,
                    self.data_low,
                    self.data_high,
                    self.matched_pivot_ones,
                    self.ab_pivotPairs,
                    self.failed_AB_patterns,
                    self.trade_symbol
                )
                    
                check_for_pivot_C(
                    self.ab_pivotPairs,
                    self.datas[0].datetime.date,
                    self.data_close,
                    self.data_open,
                    1,
                    self.settings,
                    self.data_high,
                    self.data_low,
                    self.settings['market'],
                    self.abc_pivotTrios,
                    self.trade_symbol
                
                )
                    
                check_for_pivot_D(
                    self.abc_pivotTrios,
                    self.settings['market'],
                    self.data_low[0],
                    self.data_high[0],
                    self.datas[0].datetime.date,
                    self.data_open,
                    self.data_close,
                    self.pattern_abcd,
                    self.trade_symbol    
                )
                    
                enter_trade(
                    self.pattern_abcd,
                    self.datas[0].datetime.date,
                    self.datas[0].volume,
                    self.settings['market'],
                    self.data_low,
                    self.data_high,
                    self.settings['rrr'],
                
                    )
        
                exit_trade(
                    self.pattern_abcd,
                    self.data_open,
                    self.data_close,
                    self.datas[0].datetime.date,
                    self.data,
                    self.settings['settingsName'],


                    )


    def stop(self):

        try:

            merged_patterns = merge_patterns(self.pattern_abcd)
                   
            sorted_objects = sorted(merged_patterns, key=lambda x: x.pattern_A_pivot_date)

            for each in sorted_objects:
                # print('==============')
                # print(each.pattern_A_pivot_date, each.pattern_B_pivot_date, each.pattern_C_pivot_date, each.pattern_ABCD_end_date)
                # print(len(each.trade_candle_ids))
                # print(each.trade_candle_ids[0], each.trade_candle_ids[-1])
                # print('a price:', each.pivot_A_price)
                # print('b price:', each.pivot_B_price)
                # print('c price:', each.pivot_C_price)
                # print('d price:', each.pivot_D_price)
                # print('ab:', each.ab_price_length)
                # print('bc:', each.bc_price_length)
                # print('cd:', each.cd_price_length)
                # print('d date:', each.pattern_d_created_date)
                # print('d retracement:', each.pattern_D_price_retracement)
                # print('open:', each.trade_is_open)
                # print('closed:', each.trade_is_closed)
                # print(each.trade_candle_ids)
              
                pattern_abcd.append(each)
               
            for each in self.abc_pivotTrios:
                pattern_abc.append(each)
            for each in self.ab_pivotPairs:
                pattern_ab.append(each)
            for each in self.a_pivots:
                pattern_a.append(each)

        except Exception as e:

            print('end task ',{e})

"""

- Make sure to fix all the 'get high and low' methods bc it was passing in the candle high and low and not the open and close.

- A to B bar length needs to be the exact number of bars including the pivot bar themselves.

- Find a better filter for D max length rather than just a to b length * 2

- remove patterns that arent being used for time being to make faster if going to loop

- how does d work exactly as far as running every new bar.



"""