import backtrader as bt
from backtrader.feeds.yahoo import YahooFinanceCSV
import datetime

def csv_into_btfeeds(datapath,startYear,startMonth,startDays,endingYear,endingMonth,endingDays) -> YahooFinanceCSV:

    data = bt.feeds.YahooFinanceCSVData(
        dataname=datapath,
        fromdate=datetime.datetime(int(startYear),int(startMonth), int(startDays)),
        todate=datetime.datetime(int(endingYear), int(endingMonth), int(endingDays)),
        adjclose=False)
    

    return data
