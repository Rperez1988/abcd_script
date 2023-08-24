from abcd_script.trading_bot.abcd.strategy.utilties import *
from abcd_script.trading_bot.abcd.models.A_PivotSingle import A_PivotSingle
import numpy as np
def create_pivot_c(c_pivots, b_to_c_bars, date, pivot_length, high, open, close, low, pivot_pair, c_length):


    # Prepare data.
    pivotID = c_pivots
    pivotLetter = 'C'
    pivotColor = 'Red'
    # paired = False
    pivotDate = date(ago=-pivot_length)
    open = open[-int(pivot_length)]
    high = high[-int(pivot_length)]
    low = low[-int(pivot_length)]
    close = close[-int(pivot_length)]
    startDate = date(ago=-(int(pivot_length) * 2))
    endDate = date(ago=0)
    barsSincePreviousPivot = b_to_c_bars

    daysSincePreviousPivot = pivotDate - pivot_pair.pivot_B.pivotInfo['pivotDate']
    retracementPct = None
    retracementPrice = None

    # Create pivot.
    pivot_C = A_PivotSingle(
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
        c_length
        
    )

    return pivot_C

def is_B_and_C_Low_and_High(pivot_C, pivot_pair, b_to_c_bars, data_open, data_close):
            
    pivotC_HighEnd = get_high_of_candle(pivot_C.pivotInfo['open'], pivot_C.pivotInfo['close'])
    pivot_b_bottom = get_low_of_candle(pivot_pair.pivot_B.pivotInfo['open'] ,pivot_pair.pivot_B.pivotInfo['close'])

    isPivotC_Highest = True
    is_pivot_b_the_lowest = True

    for each in range(b_to_c_bars):

        currentCandleOpen = data_open[-each]
        currentCandleClose = data_close[-each]

        isOpenAboveThenPivotCHigh = currentCandleOpen > pivotC_HighEnd
        isCloseAboveThenPivotCHigh = currentCandleClose > pivotC_HighEnd

        is_open_below_pivot_b_bottom = currentCandleOpen < pivot_b_bottom
        is_close_below_pivot_b_bottom = currentCandleClose < pivot_b_bottom

        if isOpenAboveThenPivotCHigh or isCloseAboveThenPivotCHigh:
            isPivotC_Highest = False
        
        if is_open_below_pivot_b_bottom or is_close_below_pivot_b_bottom:
            is_pivot_b_the_lowest = False

    return isPivotC_Highest, is_pivot_b_the_lowest

# def is_B_and_C_Low_and_High(pivot_C, pivot_pair, b_to_c_bars, data_open, data_close):
    
    
        
#     pivot_c_top = get_high_of_candle(pivot_C.pivotInfo['open'], pivot_C.pivotInfo['close'])
#     pivot_b_bot = get_low_of_candle(pivot_pair.pivot_B.pivotInfo['open'] ,pivot_pair.pivot_B.pivotInfo['close'])

#     data_opens_r = []
#     data_closes_r = []

#     for each in range(1,b_to_c_bars + 1):
#         data_opens_r.append(data_open[-each])
#         data_closes_r.append(data_close[-each])
    
#     highest_prices = np.maximum(data_opens_r, data_closes_r)

#     lowest_prices = np.minimum(data_opens_r, data_closes_r)

#     pivot_c_is_the_high = pivot_c_top >= np.array(highest_prices)
#     pivot_b_is_the_low = pivot_b_bot <= np.array(lowest_prices)

    

#     if str(pivot_C.pivotInfo['pivotDate']) == "2022-06-02":
#         print('highest prices: ',highest_prices)
#         print(pivot_c_is_the_high, pivot_b_is_the_low)

#     if np.all(pivot_c_is_the_high) and np.all(pivot_b_is_the_low):
#         return True, True
    
#     else:
#         return False, False

def is_b_high_and_c_low(pivot_C, pivot_pair, b_to_c_bars, data_open, data_close):

    pivot_c_low = get_low_of_candle(pivot_C.pivotInfo['open'], pivot_C.pivotInfo['close'])
    pivot_b_high = get_high_of_candle(pivot_pair.pivot_B.pivotInfo['open'] ,pivot_pair.pivot_B.pivotInfo['close'])

    is_pivot_c_lowest = True
    is_pivot_b_highest = True

    for each in range(b_to_c_bars):

        currentCandleOpen = data_open[-each]
        currentCandleClose = data_close[-each]

        is_candle_open_lower_then_c_low = currentCandleOpen < pivot_c_low
        is_candle_close_lower_then_c_low = currentCandleClose < pivot_c_low

        is_candle_open_higher_then_b_high = currentCandleOpen > pivot_b_high
        is_candle_close_higher_then_b_high = currentCandleClose > pivot_b_high

        if is_candle_open_lower_then_c_low or is_candle_close_lower_then_c_low:
            is_pivot_c_lowest = False
        
        if is_candle_open_higher_then_b_high or is_candle_close_higher_then_b_high:
            is_pivot_b_highest = False

    return is_pivot_c_lowest, is_pivot_b_highest

def get_bull_retracement(pivot_C, pivot_pair):

    c_High = float(pivot_C.pivotInfo['high'])

    b_Low = float(pivot_pair.pivot_B.pivotInfo['low'])

    a_High = float(pivot_pair.pivot_A.pivotInfo['high'])
    
    b_c_retracement = '%.2f'%((c_High - b_Low) / (a_High - b_Low) * 100)

    return b_c_retracement

def get_bear_retracement(pivot_C, pivot_pair):

    c_low = float(pivot_C.pivotInfo['low'])
    b_high = float(pivot_pair.pivot_B.pivotInfo['high'])
    a_low = float(pivot_pair.pivot_A.pivotInfo['low'])
    b_c_retracement = '%.2f'%((b_high - c_low) / (b_high - a_low) * 100)

    return b_c_retracement

def check_bull_shape(pivot_C, pivot_pair):
    pivotC_Low = pivot_C.pivotInfo['low']
    pivotC_High = pivot_C.pivotInfo['high']
    pivotB_High = pivot_pair.pivot_B.pivotInfo['high']
    pivotA_Low = pivot_pair.pivot_A.pivotInfo['low']
    c_low_above_b_high = pivotC_Low > pivotB_High
    c_high_below_a_low = pivotC_High < pivotA_Low

    return c_low_above_b_high, c_high_below_a_low

def check_bear_shape(pivot_C, pivot_pair):
    
    c_low = pivot_C.pivotInfo['low']
    c_high = pivot_C.pivotInfo['high']
    b_low = pivot_pair.pivot_B.pivotInfo['low']
    a_high = pivot_pair.pivot_A.pivotInfo['high']

    c_high_below_b_low = c_high < b_low
    c_low_above_a_high = c_low > a_high

    return c_high_below_b_low, c_low_above_a_high
