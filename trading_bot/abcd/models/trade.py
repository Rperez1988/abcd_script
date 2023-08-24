class Trade():

    def __init__(self) -> None:

        # Basic Info
        self.settingsName=None
        self.tradeID = None
        self.exchange = 'Nasdaq'
        self.stockNameFull = None
        self.stockNameSymbol = None

        self.openingTradeType = None
        self.closingTradeType = None
        self.completeTradeType = None

        self.tradeResult = None
        self.tradeOpen = None
        self.tradeClosed = None
        self.pivotPair = None
        self.riskRewardRatio = None
        self.snr = None

        # Chart
        self.chartData = None
        
        # RSI
        self.rsi = None
        self.rsiOnEnter = None
        
        # Cash
        self.pnl = None
        self.risk = None
        self.reward = None
        self.stopLoss = None
        self.takeProfit = None
        self.returnPercentage = 0
        
        # Dates
        self.dateOfA = None
        self.dateOfB = None
        self.dateOfC = None
        self.dateOfD = 0
        self.tradeStartDate = None
        self.tradeCloseDate = None
        self.currentDate = None

        # Prices
        self.priceOfA = None
        self.priceOfB = None
        self.priceOfC = None
        self.priceOfD = 0
        self.currentPrice = None

        # Size
        self.length_AtoB = 0
        self.length_BtoC = 0
        self.length_CtoD = 0
        self.length_AtoD = 0
        self.daysSinceStartDate = None
        self.tradeDuration = None
    
        # Retracement
        self.bcRetracement = 0
        self.cdRetracement = 0
        self.furthestOfA = None


        self.settings = None
        
    def getRetracement(self, A, B, priceOfC):

        aToBDistance = B - A
        aToCDistance = B - priceOfC



        retracement = '%.2f'%((aToCDistance/aToBDistance) * 100)

        x = float(retracement) / 100
        x1 = x * float(aToBDistance)
   




        return retracement

    def getTradeType(self, trade, initialType, filter, rsiNumber):

        if filter:
            if trade.rsiOnEnter < rsiNumber:
                return 'Bull'
            elif trade.rsiOnEnter >= rsiNumber:
                return 'Bear'
        if not filter:
            return initialType

    def getRiskReward(self, trade, riskRewardRatio, pivotPair):
                        
        if(trade.closingTradeType == 'Bear'):

            if(trade.openingTradeType == 'Bull'):

                reward = '%.2f'%(trade.priceOfC - pivotPair.pivot_one.close)
                risk = '%.2f'%(float(reward) / riskRewardRatio)

            if(trade.openingTradeType == 'Bear'):

                reward = '%.2f'%(trade.priceOfC - pivotPair.pivot_two.close)
                risk = '%.2f'%(float(reward) / riskRewardRatio)

            return risk, reward

        elif(trade.closingTradeType == 'Bull'):
            
            if(trade.openingTradeType == 'Bull'):
            
                reward = '%.2f'%(pivotPair.pivot_two.close - trade.priceOfC)
                risk = '%.2f'%(float(reward) / self.riskRewardRatio)

            if(trade.openingTradeType == 'Bear'):
            
                reward = '%.2f'%(trade.priceOfC - pivotPair.pivot_one.close)
                risk = '%.2f'%(float(reward) / self.riskRewardRatio)
        
            return risk, reward

    def getStopLossAndTakeProfit(self, trade):

        if(trade.closingTradeType == 'Bear'):
            
            if(trade.openingTradeType == 'Bear'):
         
                takeProfit = '%.2f'%(trade.pivotPair.pivot_two.open)
                stopLoss = '%.2f'%(trade.priceOfC + abs(float(trade.risk)))

            if(trade.openingTradeType == 'Bull'):
                                
     
                takeProfit = '%.2f'%(trade.pivotPair.pivot_one.close)
                stopLoss = '%.2f'%(trade.priceOfC + abs(float(trade.risk)))
          
            return stopLoss, takeProfit
    
        elif(trade.closingTradeType == 'Bull'):
            
            if(trade.openingTradeType == 'Bear'):

                takeProfit = '%.2f'%(trade.pivotPair.pivot_open.open)
                stopLoss = '%.2f'%(trade.priceOfC - abs(float(trade.risk)))

            if(trade.openingTradeType == 'Bull'):
                takeProfit = '%.2f'%(trade.pivotPair.pivot_two.close)
                stopLoss = '%.2f'%(trade.priceOfC - abs(float(trade.risk)))
          
       
            
            return stopLoss, takeProfit

    def getPNL(self, trade, close):

        if trade.closingTradeType == 'Bull':

            pnl = close - trade.priceOfC
            
            return '%.2f'%pnl
        
        if trade.closingTradeType == 'Bear':

            pnl = trade.priceOfC - close
            
            return '%.2f'%pnl

    def getOHLCChartData(self, trade, date,open,high, low, close):
        
        chartData = []
        i = 0
    
        while date.date(ago=-i) >= trade.tradeStartDate:

            i+=1

        for each in range(i):

            chartData.append(
                {
                    'Date': str(date.date(-each)), 
                    'Open': open[-each],
                    'High': high[-each],
                    'Low': low[-each],
                    'Close': close[-each]
                }
            )

            
        chartData.reverse()


        return chartData

    def updateTradeInfo(self, trade, date, open, high, low, close):

        trade.currentPrice = str(close)
        trade.currentDate = str(date.date(0))
        trade.tradeDuration += 1
        trade.chartData.append({'Date': str(date.date(0)),'Open': open,'High': high,'Low': low,'Close': close})
        
        return

    def printAll(self, trade):
        
        print('=============================================')
        print('=============================================')
        print('=============================================')
        print('=============================================')
        print('=============================================')
        print('=============================================')

        print('settingsName', trade.settingsName)
        print('completeTradeType', trade.completeTradeType)
        print('tradeID: ',trade.tradeID)
        print('stockNameFull: ',trade.stockNameFull)
        print('stockNameSymbol: ',trade.stockNameSymbol)
        print('currentPrice: ',trade.currentPrice)
        print('currentDate: ',trade.currentDate)
        print('tradeDuration: ',trade.tradeDuration)
        print('tradeOpen: ',trade.tradeOpen)
        print('tradeClosed: ',trade.tradeClosed)
        # print('tradeType: ',trade.tradeType)
        # print('initialTradeType: ',trade.initialTradeType)
        # print('type', trade.type)
        print('tradeResult: ',trade.tradeResult)
        print('pnl: ',trade.pnl)
        print('riskRewardRatio: ',trade.riskRewardRatio)
        print('rsi: ',trade.rsi)
        print('rsiOnEnter: ',trade.rsiOnEnter)
        print('risk: ',trade.risk)
        print('reward: ',trade.reward)
        print('pivotPair: ',trade.pivotPair)
        print('dateOfA: ',trade.dateOfA)
        print('furthestOfA: ',trade.furthestOfA)
        print('dateOfB: ',trade.dateOfB)
        print('dateOfC: ',trade.dateOfC)
        print('dateOfD:', trade.dateOfD)
        print('priceOfA: ',trade.priceOfA)
        print('priceOfB: ',trade.priceOfB)
        print('priceOfC: ',trade.priceOfC)
        print('priceOfD: ',trade.priceOfD)
        print('length A to B:', trade.length_AtoB)
        print('tradeStartDate: ',trade.tradeStartDate)
        print('A:          ', trade.priceOfA , 'on',trade.pivotPair.pivot_one.date)
        print('B:          ', trade.priceOfB , 'on', trade.pivotPair.pivot_two.date)
        print('SNR:        ', trade.pivotPair.pivot_one.snr)
        print('C:          ', trade.priceOfC , 'on',trade.dateOfC)
        print('D:          ', trade.currentPrice , 'on',trade.tradeCloseDate)
        print('Exit Prices:',trade.stopLoss,'/',trade.takeProfit)
        print('Take Profit:',trade.takeProfit)
        print('Stop Loss:', trade.stopLoss)
        print('Return Percentage:',trade.returnPercentage)
        print("Settings: ", trade.settings)
        # print('Chart Data: ', trade.chartData)
        print('Retracement: ', trade.bcRetracement)

        print('A to B Bars:', trade.pivotPair.barsBetweenAandB)
        print('A to B Days', trade.pivotPair.daysBetweenAandB)
        print('################################################')

        print('################################################')
  
    def __str__ (self):
    
            return ('Name: ' +  self.stockNameSymbol  + ' ID: ' + self.tradeID)