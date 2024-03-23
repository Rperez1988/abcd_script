from abcd_script.trading_bot.abcd.strategy.utilties import *
from abcd_script.trading_bot.abcd.strategy.Pattern_Models import *
import numpy as np
def create_pivot_c(c_pivots, b_to_c_bars, date, pivot_length, high, open, close, low, pivot_pair, c_length, candle_ids, candle_dates):


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
    pivot_C = Pattern_A(
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
        c_length,
        candle_ids,
        candle_dates
        
    )

    return pivot_C

def is_b_low_and_c_high(
        pivot_C_open, 
        pivot_C_close, 
        pivot_B_open,
        pivot_B_close,
        b_to_c_bars, 
        data_open, 
        data_close):
    
    try:
        pivotC_HighEnd = get_high_of_candle(pivot_C_open, pivot_C_close)
        pivot_b_bottom = get_low_of_candle(pivot_B_open ,pivot_B_close)


        isPivotC_Highest = True
        is_pivot_b_the_lowest = True

        try: 

            for each in range(int(b_to_c_bars)):

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
        except Exception as e:
            print(f'for each in range(b_to_c_bars): {e}')

        return isPivotC_Highest, is_pivot_b_the_lowest



    except Exception as e:
        print(f'get_high_of_candle get_low_of_candle {e}')
    

def is_b_high_and_c_low(
        pivot_C_open, 
        pivot_C_close, 
        pivot_B_open,
        pivot_B_close,
        b_to_c_bars, 
        data_open, 
        data_close):
    pivot_c_low = get_low_of_candle(pivot_C_open, pivot_C_close)
    pivot_b_high = get_high_of_candle(pivot_B_open ,pivot_B_close)

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

def get_bull_retracement(
        pattern_C_high,
        pattern_B_low,
        pattern_A_high):

    c_High = float(pattern_C_high)

    b_Low = float(pattern_B_low)

    a_High = float(pattern_A_high)
    
    b_c_retracement = ((c_High - b_Low) / (a_High - b_Low)) * 100

    return b_c_retracement

def get_bear_retracement(
        pattern_C_low,
        pattern_B_high,
        pattern_A_low
):

    c_low = float(pattern_C_low)
    b_high = float(pattern_B_high)
    a_low = float(pattern_A_low)
    b_c_retracement = '%.2f'%((b_high - c_low) / (b_high - a_low) * 100)

    return b_c_retracement

def check_bull_shape(pivot_C_low, pivot_C_high, pivot_pair):

    c_low_above_b_high = pivot_C_low > pivot_pair.pattern_B_high

    c_high_below_a_low = pivot_C_high < pivot_pair.pattern_A_low

    return c_low_above_b_high, c_high_below_a_low

def check_bear_shape(pivot_C_low, pivot_C_high, pivot_pair):
    
    c_low = pivot_C_low
    c_high = pivot_C_high

    b_low = pivot_pair.pattern_B_low
    a_high = pivot_pair.pattern_A_high

    c_high_below_b_low = c_high < b_low
    c_low_above_a_high = c_low > a_high

    return c_high_below_b_low, c_low_above_a_high

def check_if_c_is_the_high_and_if_b_is_the_low(
        settings,
        pattern_C_pivot_open,
        pattern_C_pivot_close,
        pattern_B_pivot_open,
        pattern_B_pivot_close,
        bars_passed,
        data_open,
        data_close
        ):
    c_position = None
    b_position = None


    try:
    
        if settings['market'] == 'Bull':
            c_position, b_position = is_b_low_and_c_high(
                pattern_C_pivot_open,
                pattern_C_pivot_close,
                pattern_B_pivot_open,
                pattern_B_pivot_close,
                bars_passed, 
                data_open, 
                data_close,
                )
            
    except Exception as e:
        print(f'check_if_c_is_the_high_and_if_b_is_the_low {e}')
    

    if settings['market'] == 'Bear':
        c_position, b_position = is_b_high_and_c_low(
            pattern_C_pivot_open,
            pattern_C_pivot_close,
            pattern_B_pivot_open,
            pattern_B_pivot_close,
            bars_passed, 
            data_open, 
            data_close,)
        
    if c_position and b_position: 
        return True
    else:
        return False
                


def get_pattern_c_price_retracement(
    settings,
    pattern_C_high,
    pattern_C_low,
    pattern_B_high,
    pattern_B_low,
    pattern_A_high,
    pattern_A_low,

):
    try:
        c_retracement_price_retracement_ = None

        if settings['market'] == 'Bull':
            c_retracement_price_retracement_ = get_bull_retracement(
                pattern_C_high,
                pattern_B_low,
                pattern_A_high)

        elif settings['market'] == 'Bear':
            c_retracement_price_retracement_ = get_bear_retracement(
                pattern_C_low,
                pattern_B_high,
                pattern_A_low)

        return c_retracement_price_retracement_
    except Exception as e:
        print(e)

def check_pattern_c_price_retracement(
        settings,
        data_high,
        data_low,
        pivot_pair,

):
     
    c_retracement_price_retracement_ = None

    if settings['market'] == 'Bull':
        c_retracement_price_retracement_ = get_bull_retracement(
        data_high[-settings['pivotLength']], 
        pivot_pair)

    elif settings['market'] == 'Bear':
        c_retracement_price_retracement_ = get_bear_retracement(
        data_low[-settings['pivotLength']],
        pivot_pair)

    if float(c_retracement_price_retracement_) >= 1 and float(c_retracement_price_retracement_) <= 100:
        return True
    else:
        return False
    


def check_pattern_ABC_shape(
    settings,
    data_high,
    data_low,
    pivot_pair,

    
    ):
    c_shape = None
    b_shape = None

    if  settings['market'] == 'Bear':

        c_shape, b_shape = check_bear_shape(
            data_low[-settings['pivotLength']],
            data_high[-settings['pivotLength']], 
            pivot_pair)

    if settings['market'] == 'Bull':

        c_shape, b_shape = check_bull_shape(
            data_low[-settings['pivotLength']],
            data_high[-settings['pivotLength']], 
            pivot_pair)

    if c_shape and b_shape:

        return True
    else:

        return False