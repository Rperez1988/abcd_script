def getAverageGains(df):

    for i, row in enumerate(df['avg_gain'].iloc[14+1:]):
        df['avg_gain'].iloc[i + 14 + 1] = (df['avg_gain'].iloc[i + 14] * (14 - 1) + df['gain'].iloc[i + 14 + 1]) / 14

    return df