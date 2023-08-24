def getOpenAndCloseOfCandle(open,close, length, side):

    # Grab the open of the 'x' bar back.
    openOfPivot = open[length]

    # Grab the close of the 'x' bar back.
    closeOfPivot = close[length]

    return openOfPivot, closeOfPivot
