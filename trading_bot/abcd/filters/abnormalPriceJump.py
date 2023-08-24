


from statistics import mean

def get_average_size_of_bars_in_pivot(pivot_length, data_open, data_close):
        
        candles_in_pivot = pivot_length * 2
        
        # Create an empty list to store the size of each bar in the pivot
        average_of_all_bars = []

        # Loop through the data in reverse order up to the specified length
        for x in range(0, candles_in_pivot):

            # Get the open and close price for the current bar
            open_price = data_open[-x]
            close_price = data_close[-x]

            # Calculate the size of the bar (the absolute difference between the open and close prices)
            candle_size = float("%.2f" % abs(open_price - close_price))

            # Add the size of the bar to the list of all bar sizes
            average_of_all_bars.append(candle_size)

        # Calculate the average size of all bars in the pivot
        average_size = "%.2f" % mean(average_of_all_bars)

        # Return the average size of all bars in the pivot
        return average_size

def isPivotAbnormalPriceJumpEngine(price_change_limit, pivot_length, current_candle_open, current_candle_close):
    
    # Call the get_average_size_of_bars_in_pivot function to calculate the average size of all bars in the pivot
    averageSizeOFBarsInPivot = get_average_size_of_bars_in_pivot(pivot_length, current_candle_open, current_candle_close)

    # Get the open and close prices for the current pivot
    open_price = current_candle_open[-pivot_length]
    close_price = current_candle_close[-pivot_length]

    # Calculate the size of the pivot (the absolute difference between the open and close prices)
    pivot_size = "%.2f" % abs(open_price - close_price)

    # Calculate the percentage change in size of the pivot compared to the average size of all bars in the pivot
    percentChange = ((float(pivot_size) / float(averageSizeOFBarsInPivot)) / float(averageSizeOFBarsInPivot)) * 100

    # Check if the percentage change is less than or equal to the specified price change cap
    if percentChange <= float(price_change_limit):
        # If so, return False (not an abnormal price jump) and the percentage change
        return False
    else:
        # If not, return True (an abnormal price jump) and False (there is no percentage change to return)
        return True
    



def abnormalPriceJump(price_change_limit, pivot_length, current_candle_open, current_candle_close):

    # Check if the value of price_change_limit is "Off" or a numeric string
    if price_change_limit == "Off":
        # If it is "Off", return False
        return True
    elif price_change_limit.isdigit():
        # If it is a numeric string, call the isPivotAbnormalPriceJumpEngine function to check if the current pivot is due to an abnormal price jump.
        # The results are returned as a tuple of two values: abnormalPriceJump and priceChange
        abnormalPriceJump = isPivotAbnormalPriceJumpEngine(price_change_limit, pivot_length, current_candle_open, current_candle_close)
        # If the pivot is not due to an abnormal price jump, return True, else return False
        if not abnormalPriceJump:
            return True
        else:
            return False

            
