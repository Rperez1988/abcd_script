
def get_first_and_last_data_of_DF(df):

    earliestDate  = df.iloc[0]['Date'].split('-')
    startYear     = earliestDate[0]
    startMonth    = earliestDate[1]
    startDays     = earliestDate[2]
    
    latestDate      = df.iloc[-1]['Date'].split('-')
    endingYear    = latestDate[0]
    endingMonth   = latestDate[1]
    endingDays    = latestDate[2]

    return startYear, startMonth, startDays, endingYear, endingMonth, endingDays
