from abcd_script.trading_bot.abcd.strategy.Pattern_Models import *
from abcd_script.trading_bot.abcd.pivot_screener.findPivot import findPivot

def create_B(b_pivot, date, pivot_length, high, open, close, low, full_length,candle_ids, candle_dates):

    pivotID = len(b_pivot)
    pivotLetter = 'B'
    pivotColor = 'Red'
    paired = False
    pivotDate = date(ago=-pivot_length)
    open = open[-pivot_length]
    high = high[-pivot_length]
    low = low[-pivot_length]
    close = close[-pivot_length]
    startDate = date(ago=-(pivot_length * 2))
    endDate = date(ago=0)
    barsSincePreviousPivot = 0
    daysSincePreviousPivot = 0
    retracementPct = None
    retracementPrice = None,
   

    pivot_B = Pattern_A(
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
        full_length,
        candle_ids,
        candle_dates
        
    )
    
    return pivot_B

def add_b_with_group_of_b(b_pivots, b_pivot):
                                        
    def is_object_in_list(new_object):
        for obj in b_pivots:
            if obj.pivotInfo['pivotDate'] == new_object.pivotInfo['pivotDate']:
                return True
        return False

    if not is_object_in_list(b_pivot):

        b_pivots.append(b_pivot)

def get_days_between_A_and_B(date, pivot_length, pivot_A):

    daysBetweenAandB = date(ago=-pivot_length) - pivot_A.pivotInfo['pivotDate']
    daysBetweenAandB = str(daysBetweenAandB).split(' ', 1)[0]

    return daysBetweenAandB

def check_A_position_to_B_position(market, pivot_A, pivot_B):

    b_position = False
                    

    if market == 'Bull':
        if pivot_A.pivotInfo['low'] > pivot_B.pivotInfo['high']:
            b_position =  True

        
    if market == 'Bear':
        if pivot_A.pivotInfo['high'] < pivot_B.pivotInfo['low']:
            b_position =  True


    return b_position

def check_if_A_is_the_lowest(bars_between_A_and_B, candle_high, candle_low, pivot_A_low):

    try:
        is_pivot_A_the_lowest = True

        for each in range(bars_between_A_and_B):

                if candle_high[-each] < pivot_A_low:
            
                    is_pivot_A_the_lowest = False
                
                if candle_low[-each] < pivot_A_low:
                    is_pivot_A_the_lowest = False
            
        return is_pivot_A_the_lowest

    except Exception as e:
        print(f'check_if_A_is_the_lowest {e}')
                            
def check_if_A_is_the_highest(
    bars_between_A_and_B, 
    candle_high, 
    candle_low, 
    pivot_A_high,

    ):

    try:    
        isPivotA_Highest = True
        
        for each in range(bars_between_A_and_B):
          
            # print(bars_between_A_and_B ,date(ago=-each),'candle high:',candle_high[-each], candle_low[-each], pivot_A_high)
        
            if candle_high[-each] > pivot_A_high:
                
                isPivotA_Highest = False  
                

            if candle_low[-each] > pivot_A_high:
             
                isPivotA_Highest = False        
        
        return isPivotA_Highest
    except Exception as e:
        print(f'check_if_A_is_the_highest {e}')

def check_if_B_is_the_lowest(bars_between_A_and_B, candle_open, candle_close, pattern_B_low):

    try:     
        isPivotB_Lowest = True

        for each in range(bars_between_A_and_B):

            if candle_open[-each] < pattern_B_low:
                isPivotB_Lowest =  False
            
            if candle_close[-each] < pattern_B_low: 
                isPivotB_Lowest = False
        return isPivotB_Lowest

    except Exception as e:
        print(f'check_if_B_is_the_lowest {e}')

def check_if_B_is_the_highest(bars_between_A_and_B, candle_high, candle_low, pattern_B_high):

    try:

        isPivotB_Highest = True
        for each in range(bars_between_A_and_B):
            if candle_high[-each] > pattern_B_high:
                isPivotB_Highest = False

            if candle_low[-each] > pattern_B_high: 
                isPivotB_Highest = False
    
        return isPivotB_Highest
    except Exception as e:
        print(f'check_if_B_is_the_highest {e}')

def find_B(pivot, pivotOjbect, date, market, close, open, pivot_length):

    pivotType = None

    match market:

        case 'Bull':
            
            pivotType = findPivot(pivot, pivotOjbect, date, close, open, pivot_length, 'Bear')

        case 'Bear':

            pivotType = findPivot(date, close, open, pivot_length, 'Bull')

    return pivotType

def check_if_A_to_B_is_correct_shape(market, is_A_the_highest, is_B_the_lowest, is_A_the_lowest,is_B_the_highest):

    match market:

        case 'Bull':
            
            if is_A_the_highest and is_B_the_lowest:

                return True
            
            elif not is_A_the_highest  or not is_B_the_lowest:
                
                return False

        case 'Bear':

            if is_A_the_lowest and is_B_the_highest:

                return True
            
            elif not is_A_the_lowest  or not is_B_the_highest:

                return False

def check_ab_is_start_of_abcd(market, pivot_A_high, pivot_B_low):


    try:

        match market:

            case 'Bull':
                
                return pivot_A_high > pivot_B_low
            
            case 'Bear':

                return pivot_A_high < pivot_B_low
    except Exception as e:
        print(f'check_ab_is_start_of_abcd {e}')