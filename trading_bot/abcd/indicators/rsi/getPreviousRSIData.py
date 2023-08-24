import pandas as pd

def getPreviousRSIData(Pivots, close, dates):

    if Pivots.rsiStart < 1:
    
        dates = getDates(dates)
        closes = getCloses(close)
        getPandasRSI(closes, dates, Pivots)

        Pivots.rsiStart += 1

def getCloses(x, current_index):

    allCloses = []
    
    for each in reversed(range(0,current_index)):
     
        close = x[-each]
        xy = {'Close':float(close)}
        allCloses.append(xy)
    return allCloses


def getDates(dates, current_index):

    alldates = []


    for each in reversed(range(0,current_index)):
        date = str(dates.date(-each))
        alldates.append(date)

    return alldates


def getPandasRSI(closes, dates):
    
    df = pd.DataFrame(closes)

    df['diff'] = df.diff(1)

    df['Dates'] = dates

    df['gain'] = df['diff'].clip(lower=0).round(2)

    df['loss'] = df['diff'].clip(upper=0).abs().round(2)

    df['avg_gain'] = df['gain'].rolling(window=14, min_periods=14).mean()
    df['avg_loss'] = df['loss'].rolling(window=14, min_periods=14).mean()

    df = getAverageGains(df)

    df = getAverageLosses(df)

    df['rs'] = df['avg_gain'] / df['avg_loss']

    df['rsi'] = 100 - (100 / (1.0 + df['rs']))

    # df = df.drop(columns=['diff', 'gain','loss','avg_gain','avg_loss','rs'])
    return df

import pandas as pd
import ta

def getPandasRSI_(closes, dates):
    df = pd.DataFrame({'Close': closes, 'Date': dates})
    rsi = ta.momentum.RSIIndicator(close=df['Close'], window=14)
    df['rsi'] = rsi.rsi()
    return df

def getAverageGains(df):

    for i, row in enumerate(df['avg_gain'].iloc[14+1:]):
        df['avg_gain'].iloc[i + 14 + 1] = (df['avg_gain'].iloc[i + 14] * (14 - 1) + df['gain'].iloc[i + 14 + 1]) / 14

    return df

def getAverageLosses(df):

    for i, row in enumerate(df['avg_loss'].iloc[14+1:]):
        df['avg_loss'].iloc[i + 14 + 1] =\
            (df['avg_loss'].iloc[i + 14] *
            (14 - 1) +
            df['loss'].iloc[i + 14 + 1])\
            / 14

    return df


import numpy as np


def calculate_rsi(source, rsi_length):
    deltas = np.diff(source)
    up = np.mean(np.maximum(deltas, 0)[-rsi_length:])
    down = np.mean(np.abs(np.minimum(deltas, 0))[-rsi_length:])
    
    if down == 0:
        rsi_value = 100
    elif up == 0:
        rsi_value = 0
    else:
        rsi_value = 100 - (100 / (1 + up / down))
    
    return rsi_value