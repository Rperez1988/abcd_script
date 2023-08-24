
from abcd_script.trading_bot.abcd.pivot_screener.getPivotLow import get_pivot_low
from abcd_script.trading_bot.abcd.pivot_screener.getPivotHigh import get_pivot_high
from abcd_script.trading_bot.abcd.pivot_screener.getOpenAndCloseOfCandle import getOpenAndCloseOfCandle
from abcd_script.trading_bot.abcd.pivot_screener.getLowOfCandle import get_low_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import get_high_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.comparePivotToSideBars import comparePivotLowToSideCandles
from abcd_script.trading_bot.abcd.pivot_screener.comparePivotToSideBars import comparePivotHighToSideCandles
from typing import List, Dict

# def findPivot(candle_close: list[dict[float]], candle_open: list[dict[float]], pivot_length: int, pivot_type: str) -> str:
    
#     # Grab the open of the candle being checked for a pivot
#     openOfPivot = candle_open[-pivot_length]

#     # Grab the close of the candle being checked for a pivot
#     closeOfPivot = candle_close[-pivot_length]

#     highOfPivot = openOfPivot if openOfPivot > closeOfPivot else closeOfPivot
#     lowOfPivot  = openOfPivot if openOfPivot <= closeOfPivot else closeOfPivot

#     pivot_found = None
#     left_bars_pivot_comparison = None
#     right_bars_pivot_comparison = None

#     # print('pivot_open: ',openOfPivot, 'pivot_close:',  closeOfPivot)

#     match pivot_type:
#         case 'Bear':

#             pivot_type_str = 'Low'

#             left_bars_pivot_comparison = comparePivotLowToSideCandles(candle_open, candle_close, pivot_length, lowOfPivot, 'left')   
#             right_bars_pivot_comparison = comparePivotLowToSideCandles(candle_open, candle_close, pivot_length, lowOfPivot, 'right')  

#         case 'Bull':
#             # Set pivot type to 'High'
#             pivot_type_str = 'High'

#             # Compare pivot high to side candles
#             left_bars_pivot_comparison = comparePivotHighToSideCandles(candle_open, candle_close, pivot_length, highOfPivot, 'left')   
#             right_bars_pivot_comparison = comparePivotHighToSideCandles(candle_open, candle_close, pivot_length, highOfPivot, 'right')  

#     # Check if pivot found or not
#     if False in left_bars_pivot_comparison or False in right_bars_pivot_comparison:
#         pivot_found = False
#     else:
#         pivot_found = True

#     # Return pivot type if found, otherwise False
#     if pivot_found:
#         return pivot_type_str
#     else:
#         return False
            


def findPivot(candle_close: list[dict[float]], candle_open: list[dict[float]], pivot_length: int, pivot_type: str) -> str:
    
    openOfPivot = candle_open[-pivot_length]
    closeOfPivot = candle_close[-pivot_length]

    highOfPivot = openOfPivot if openOfPivot > closeOfPivot else closeOfPivot
    lowOfPivot  = openOfPivot if openOfPivot <= closeOfPivot else closeOfPivot

    match pivot_type:

        case 'Bear':

            is_pivot_the_lower = comparePivotLowToSideCandles(candle_open, candle_close, pivot_length, lowOfPivot)

            return is_pivot_the_lower

        case 'Bull':

            is_pivot_the_higher = comparePivotHighToSideCandles(candle_open, candle_close, pivot_length, highOfPivot)

            return is_pivot_the_higher
   





