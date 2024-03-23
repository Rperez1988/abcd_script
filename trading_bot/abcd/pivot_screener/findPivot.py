import numpy as np

def findPivot(pivot, pivotObject, date, candle_close: list[dict[float]], candle_open: list[dict[float]], pivot_length: int, pivot_type: str) -> str:
    
    
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





