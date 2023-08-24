def get_high_of_candle(open, close):
            
    high = None

    if close >= open:
        high = close
        
    if open >= close:
        high = open

    return high


def getLowOfCandle(open, close):
    
    low = None

    if close >= open:
        low = open
        
    if close <= open:
        low = close

    return low

