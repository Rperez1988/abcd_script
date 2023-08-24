
def get_low_of_candle(dOpen,dClose) -> float:
    low = dOpen if dOpen < dClose else dClose
    return low
