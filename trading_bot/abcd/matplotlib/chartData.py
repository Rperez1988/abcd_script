# def getInfoForBarChart():
#     # Bar Chart Data
#     matData = {'tickerSymbol': self.stockName,'tradeid': None, 'dates': [], 'open': [],'high': [],'low': [],'close': [], 'topclose' : None, 'sr': None, 'botclose': None}  

#     i = 0
#     k = 1
#     while closed_trade.date_of_pivot_one <= self.datas[0].datetime.date(-i):
        
#         matData['tradeid']                  = closed_trade.trade_id
#         matData['topclose']                 = closed_trade.pivotOneCloseMark
#         matData['date_of_pivot_high']       = closed_trade.date_of_pivot_one
#         matData['date_of_pivot_low']        = closed_trade.date_of_pivot_two
#         matData['price_of_pivot_high']      = closed_trade.price_of_pivot_one
#         matData['price_of_pivot_low']       = closed_trade.price_of_pivot_two
    
#         matData['sr']                       = closed_trade.price_pivot_one_snr_tested
#         matData['botclose']                 = closed_trade.pivotTwoCloseMark

#         matData['dates'].append(self.datas[0].datetime.date(-i))
#         matData['open'].append(self.data_open[-i])
#         matData['high'].append(self.data_high[-i])
#         matData['low'].append(self.data_low[-i])
#         matData['close'].append(self.data_close[-i])

#         if closed_trade.date_of_pivot_one == self.datas[0].datetime.date(-i):
#             while k <= self.length:
#                 matData['dates'].append(self.datas[0].datetime.date(-i - k))
#                 matData['open'].append(self.data_open[-i - k])
#                 matData['high'].append(self.data_high[-i - k])
#                 matData['low'].append(self.data_low[-i - k])
#                 matData['close'].append(self.data_close[-i - k])
#                 k = k + 1
#         i = i + 1
        
#     self.chartData.append(matData)