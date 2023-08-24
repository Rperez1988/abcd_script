from .data_manipulation.first_and_last_date_of_DF import get_first_and_last_data_of_DF
from .data_manipulation.csv_into_backtraderfeeds import csv_into_btfeeds

def prepareDataForStrategy(df,datapath):

    startYear,startMonth,startDays,endingYear,endingMonth,endingDays = get_first_and_last_data_of_DF(df)
    btFeed = csv_into_btfeeds(datapath,startYear,startMonth,startDays,endingYear,endingMonth,endingDays)

    return btFeed
