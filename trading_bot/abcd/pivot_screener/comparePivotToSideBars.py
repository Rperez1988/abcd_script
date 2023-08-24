from abcd_script.trading_bot.abcd.pivot_screener.getOpenAndCloseOfCandle import getOpenAndCloseOfCandle
from abcd_script.trading_bot.abcd.pivot_screener.getLowOfCandle import get_low_of_candle
from abcd_script.trading_bot.abcd.pivot_screener.getHighOfCandle import get_high_of_candle

# def comparePivotLowToSideCandles(dataOpen, dataClose, pivotLength, lowOfPivot, side):
    
#     sideBars = []

#     if side == 'left':

#         i = 1
#         while i <= pivotLength:
            
#             length = -abs(pivotLength + i)
    
#             openOfCandle,closeOfCandle = getOpenAndCloseOfCandle(dataOpen,dataClose,length, side)

#             lowOfSideBar = get_low_of_candle(openOfCandle,closeOfCandle)

#             # print(side, lowOfSideBar)
            
#             isPivotLower = lowOfPivot <= lowOfSideBar

#             sideBars.append(isPivotLower)

#             i += 1

#     if side == 'right':

#         i = 0
#         while i < pivotLength:
            
#             length = i - (pivotLength - 1)

    
#             openOfCandle,closeOfCandle = getOpenAndCloseOfCandle(dataOpen,dataClose,length, side)

#             lowOfSideBar = get_low_of_candle(openOfCandle,closeOfCandle)

#             # print(side, lowOfSideBar)
            
#             isPivotLower = lowOfPivot <= lowOfSideBar

#             sideBars.append(isPivotLower)

#             i += 1

#     return sideBars


        


# def comparePivotHighToSideCandles(dataOpen, dataClose, pivotLength, highOfPivot, side):
#     sideBars = []

#     if side == 'left':

#         i = 1
#         while i <= pivotLength:
            
#             length = -abs(pivotLength + i)
    
#             openOfCandle,closeOfCandle = getOpenAndCloseOfCandle(dataOpen,dataClose,length, side)

#             highOfSideBar = get_high_of_candle(openOfCandle,closeOfCandle)

#             # print(side, highOfSideBar)
                
#             isPivotHigher = highOfPivot >= highOfSideBar
            
#             sideBars.append(isPivotHigher)

#             i += 1



      
#     if side == 'right':

#         i = 0
#         while i < pivotLength:
            
#             length = i - (pivotLength - 1)

#             openOfCandle,closeOfCandle = getOpenAndCloseOfCandle(dataOpen,dataClose,length, side)

#             highOfSideBar = get_high_of_candle(openOfCandle,closeOfCandle)

#             # print(side, highOfSideBar)
                
#             isPivotHigher = highOfPivot >= highOfSideBar
            
#             sideBars.append(isPivotHigher)

#             i += 1

#     return sideBars


import numpy as np

def comparePivotLowToSideCandles(dataOpen, dataClose, pivotLength, lowOfPivot):


    data_opens_r = []
    data_closes_r = []

    for each in range(0,3):
        data_opens_r.append(dataOpen[-each])
        data_closes_r.append(dataClose[-each])

    x = (pivotLength * 2) + 1

    highest_prices = np.minimum(data_opens_r, data_closes_r)

    pivot_index = len(highest_prices) // 2

    left_list = np.array(highest_prices[2])

    right_list = np.array(highest_prices[0])
    
    if lowOfPivot < left_list and lowOfPivot < right_list:
        return True

def comparePivotHighToSideCandles(dataOpen, dataClose, pivotLength, highOfPivot):

    data_opens_r = []
    data_closes_r = []

    for each in range(0,3):
        data_opens_r.append(dataOpen[-each])
        data_closes_r.append(dataClose[-each])

    x = (pivotLength * 2) + 1

    highest_prices = np.maximum(data_opens_r, data_closes_r)



    pivot_index = len(highest_prices) // 2

    left_list = np.array(highest_prices[2])

    right_list = np.array(highest_prices[0])

    
    # if(highOfPivot == 171.78 or highOfPivot == "171.78"):
    #     print('--------------------------------------------')
    #     print(highest_prices)
    #     print(left_list)
    #     print(right_list)
    
    if highOfPivot > left_list and highOfPivot > right_list:
        return True



# Script Run Time: 13.090648412704468



# Script Run Time: 13.146716117858887