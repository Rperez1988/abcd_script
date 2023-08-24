import pandas as pd
def getLiveRSI(Pivots, date, close):
        
    pd.set_option('display.width', 100)

    date    = str(date.date(ago=0))
  
    diff    = close[0] - close[-1]  

    bar     = {'Close': close[0], 'Dates': date, 'diff': "%.2f"%diff}

    ups     = 0

    downs   = 0

    if diff >= 0:

        bar.update({'gain': float("%.2f"%diff), 'loss': downs})

    elif diff <= 0:
        
        bar.update({'gain': ups, 'loss': float("%.2f"%abs(diff))})

    df2     = pd.DataFrame(bar,index=[0])

    Pivots.pandasDF = pd.concat([Pivots.pandasDF, df2], ignore_index = True, axis = 0)

    Pivots.pandasDF['avg_gain'].iloc[-1] = (Pivots.pandasDF['avg_gain'].iloc[-2] * (14 - 1) + Pivots.pandasDF['gain'].iloc[-2]) / 14

    Pivots.pandasDF['avg_loss'].iloc[-1] = (Pivots.pandasDF['avg_loss'].iloc[-2] * (14 - 1) + Pivots.pandasDF['loss'].iloc[-2]) / 14      

    Pivots.pandasDF['rs'] = Pivots.pandasDF['avg_gain'] / Pivots.pandasDF['avg_loss']

    Pivots.pandasDF['rsi'] = 100 - (100 / (1.0 + Pivots.pandasDF['rs']))

    return Pivots.pandasDF
