def getAverageLosses(df):
    for i, row in enumerate(df['avg_loss'].iloc[14+1:]):
        df['avg_loss'].iloc[i + 14 + 1] =\
            (df['avg_loss'].iloc[i + 14] *
            (14 - 1) +
            df['loss'].iloc[i + 14 + 1])\
            / 14

    return df