from abcd_script.trading_bot.abcd.strategy.utilties import *
from abcd_script.trading_bot.abcd.models.A_PivotSingle import A_PivotSingle
from abcd_script.trading_bot.abcd.models.ABCD_PivotQuad import ABCD_PivotQuad

def get_bull_d_to_b_retracement(pivot_trio, d_low):

    c_High = float(pivot_trio.pivot_C.pivotInfo['high'])

    d_Low = float(d_low)

    b_Low = float(pivot_trio.pivot_B.pivotInfo['low'])

    cd_retracement = '%.2f'%(((c_High - d_Low) / (c_High - b_Low)) * 100)

    return cd_retracement

def get_bear_d_to_b_retracement(pivot_trio, d_high):

    c_low = float(pivot_trio.pivot_C.pivotInfo['low'])

    d_high = float(d_high)

    b_high = float(pivot_trio.pivot_B.pivotInfo['high'])

    bear_cd_retracement = '%.2f'%((d_high - c_low) / (b_high - c_low) * 100)

    return bear_cd_retracement

def check_bull_c_position(c_to_d_bar_length, open, close, pivot_trio):
            
    isPivotC_Hightest = True

    for each in range(c_to_d_bar_length):

        open_ = open[-each]

        close_ = close[-each]

        pivotC_open = pivot_trio.pivot_C.pivotInfo['open']

        pivotC_close = pivot_trio.pivot_C.pivotInfo['close']

        pivotC_High = get_high_of_candle(pivotC_open, pivotC_close)

        candle_High = get_high_of_candle(open_, close_)

        candleClosesAboveC = pivotC_High < candle_High

        if candleClosesAboveC:

            isPivotC_Hightest = False

    return isPivotC_Hightest

def check_bear_c_position(c_to_d_bar_length, open, close, pivot_trio):

    is_c_lowest = True

    for each in range(c_to_d_bar_length):

        open_ = open[-each]

        close_ = close[-each]

        pivotC_open = pivot_trio.pivot_C.pivotInfo['open']

        pivotC_close = pivot_trio.pivot_C.pivotInfo['close']

        c_low = get_low_of_candle(pivotC_open, pivotC_close)

        current_candle_low = get_low_of_candle(open_, close_)
        
        candle_is_lower_then_c = current_candle_low < c_low

        if candle_is_lower_then_c:

            is_c_lowest = False

    return is_c_lowest

def check_bull_d_position(c_to_d_bar_length, open, close):

    isPivotD_Lowest = True

    for each in range(c_to_d_bar_length):

        open_ = open[-each]

        close_ = close[-each]

        pivotD_open = open[0]

        pivotD_close = close[0]

        pivotD_Low = get_low_of_candle(pivotD_open, pivotD_close)

        candle_Low = get_low_of_candle(open_, close_)

        candleClosesBelowD = pivotD_Low > candle_Low

        if candleClosesBelowD:

            isPivotD_Lowest = False
            
    return isPivotD_Lowest

def check_bear_d_position(c_to_d_bar_length, open, close):

    is_d_the_highest = True

    for each in range(c_to_d_bar_length):

        open_ = open[-each]

        close_ = close[-each]

        pivotD_open = open[0]

        pivotD_close = close[0]

        d_high = get_high_of_candle(pivotD_open, pivotD_close)

        current_candle_high = get_high_of_candle(open_, close_)

        candle_is_higher_then_d = current_candle_high > d_high

        if candle_is_higher_then_d:

            is_d_the_highest = False

    return is_d_the_highest
                
def create_d(d_pivots, date, high, open, close, low, c_to_d_bar_length, pivot_trio, d_length):

    # Prepare pivot D data.
    pivotID = d_pivots
    pivotLetter = 'D'
    pivotColor = 'Red'
    paired = False
    pivotDate =  date(ago=0)
    open = open[0]
    high = high[0]
    low = low[0]
    close = close[0]
    startDate = date(ago=0)
    endDate = date(ago=0)
    barsSincePreviousPivot = c_to_d_bar_length
    daysSincePreviousPivot = pivotDate - pivot_trio.pivot_C.pivotInfo['pivotDate']
    retracementPct = None
    retracementPrice = None

    # Create pivot D.
    pivot_D = A_PivotSingle(
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
        d_length
        
    )

    return pivot_D

def get_bull_d_to_a_retracement(pivot_trio, d_low):

    c_High = float(pivot_trio.pivot_C.pivotInfo['high'])

    d_Low = float(d_low)

    a_High = float(pivot_trio.pivot_A.pivotInfo['high'])

    b_Low = float(pivot_trio.pivot_B.pivotInfo['low'])

    cd_retracement = '%.2f'%((c_High - d_Low) / (a_High - b_Low) * 100)

    return cd_retracement

def get_bear_d_to_a_retracement(pivot_trio, d_high):

    # Get c to d price length pct.
    c_low = float(pivot_trio.pivot_C.pivotInfo['low'])
    d_high = float(d_high)
    a_low = float(pivot_trio.pivot_A.pivotInfo['low'])
    b_high = float(pivot_trio.pivot_B.pivotInfo['high'])

    cd_retracement = '%.2f'%((d_high - c_low) / (b_high - a_low) * 100)

    return cd_retracement

def get_d_to_b_retracement(market, pivot_trio, low, high):

    d_to_b_retracement = None

    if market == 'Bull':
        d_to_b_retracement = get_bull_d_to_b_retracement(pivot_trio, low)

    elif market == 'Bear':
        d_to_b_retracement = get_bear_d_to_b_retracement(pivot_trio, high)


    return d_to_b_retracement

def get_d_to_a_retracement(market, pivot_trio, low, high):

    d_to_a_retracement = None

    if market == 'Bull':
        d_to_a_retracement = get_bull_d_to_a_retracement(pivot_trio, low)

    elif market == 'Bear':
        d_to_a_retracement = get_bull_d_to_a_retracement(pivot_trio, high)



    return d_to_a_retracement

def get_c_position(market, c_to_d_bar_length, pivotTrio, open, close):

    match market:

        case 'Bull':
            c_position = check_bull_c_position(c_to_d_bar_length, open, close, pivotTrio)

        case 'Bear':
            c_position = check_bear_c_position(c_to_d_bar_length, open, close, pivotTrio)

    return c_position

def get_d_position(market, c_to_d_bar_length, pivotTrio, open, close):

    c_position = None

    match market:

        case 'Bull':
            c_position = check_bull_d_position(c_to_d_bar_length, open, close)

        case 'Bear':
            c_position = check_bear_d_position(c_to_d_bar_length, open, close)

    return c_position

def create_ABCD(pivot_qaud_length, pivotTrio, pivot_D, d_to_a_retracement, rsi, full_length):

    abcd = ABCD_PivotQuad(
        pivot_qaud_length,
        pivotTrio.pivot_A, 
        pivotTrio.pivot_B, 
        pivotTrio.pivot_C, 
        pivot_D, 
        pivotTrio.pivot_C.duration['barsSincePreviousPivot'], 
        pivotTrio, 
        d_to_a_retracement,
        rsi,
        full_length

    )

    return abcd