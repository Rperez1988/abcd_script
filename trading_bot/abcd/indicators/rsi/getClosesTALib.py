def getClosesTALib(close):

    closes = []

    for each in reversed(range(1,30)):
        close = close[-each]
        x = {'price':float(close)}
        closes.append(x)

    return closes
