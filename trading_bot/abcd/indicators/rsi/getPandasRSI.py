
import pandas as pd
from abcd_script.trading_bot.abcd.indicators.rsi.getAverageGains import getAverageGains 
from abcd_script.trading_bot.abcd.indicators.rsi.getAverageLosses import getAverageLosses

def getPandasRSI(closes, dates, pivot):
    
    df = pd.DataFrame(closes)

    df['diff'] = df.diff(1)

    df['Dates'] = dates

    df['gain'] = df['diff'].clip(lower=0).round(2)

    df['loss'] = df['diff'].clip(upper=0).abs().round(2)

    df['avg_gain'] = df['gain'].rolling(window=15, min_periods=14).mean()[:14+1]

    df['avg_loss'] = df['loss'].rolling(window=15, min_periods=14).mean()[:14+1]

    df = getAverageGains(df)

    df = getAverageLosses(df)

    df['rs'] = df['avg_gain'] / df['avg_loss']

    df['rsi'] = 100 - (100 / (1.0 + df['rs']))

    # df = df.drop(columns=['diff', 'gain','loss','avg_gain','avg_loss','rs'])
    pivot.pandasDF = df
