def get_high_of_candle(open, close):
            
    high = None

    if close >= open:
        high = close
        
    if open >= close:
        high = open

    return high


def get_low_of_candle(open, close):
    
    low = None

    if close >= open:
        low = open
        
    if close <= open:
        low = close

    return low

def getBarsInBetweenPivots(A_date, date):
    
    i = 0
    while str(A_date) <= str(date(ago=i)):
        i-=1
        
    return i

from datetime import datetime
def check_bar_length(date, start_date):

    try: 
        duration = 0
        while date(ago=-duration) >= start_date:
            duration +=1
        return duration
    
    except Exception as e:
        print(f'check_bar_length {e}')