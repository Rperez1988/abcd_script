class ABCD_Open():

    def __init__(self,
            id, 
            symbol, 
            currentClose, 
            pivot_A,
            pivot_B,
            pivot_C,
            pivot_D,
            settings,
            barsBetweenBandC,
            ab_pivotPair, 
            tradeDuration, 
            barsBetweenCandD,
            barsBetweenAandB, 
            currentDate,
            abc_ID,
            entryPrice,
            reward,
            risk,
            takeProfit,
            stopLoss,
            enterDate,
            tradeResult,
            c,
            r1,
            rsi, 
            volume,
            ab_full_length,
            abcd_full_length,
            prev_bars_volume,
            average_volume,
            percentage_change,


        ) -> None:
        
        self.rsi = 30
        self.rsiOnEnter = 30
        self.pivotPair = ab_pivotPair
        self.chartData = None

        
        from datetime import datetime, timedelta
        self.tradeInfo = {
            'id': id,
            'abc_ID': abc_ID,
            'symbol': symbol,
            'exchange': 'Nasdaq',
            'endDate': str(pivot_D.pivotInfo['pivotEndDate']),
            'startDate':  str(pivot_A.pivotInfo['pivotStartDate']),
            'tradeDuration': tradeDuration,
            'tradeOpen': True,
            'tradeClosed': False,
            'closingTradeType':'Bull',
            'openingTradeType':'Bull',
            'completeTradeType':'Bull',
            'tradeResult':tradeResult,
            'tradeStartDate': str(enterDate),
            'tradeCloseDate':str(pivot_D.pivotInfo['pivotDate']),
            'currentPrice': currentClose,
            'currentDate': str(currentDate),
            'pivot_number' : None,
            'lowest_price_dropped': str(entryPrice),



            'rsi': '%.2f'%(rsi), 
            'volume': volume,
            'abcd_volumes': str(prev_bars_volume),
            'average_volume':  average_volume,
            'percentage_change': '%.2f'%(percentage_change)

        }
        
        self.pivotInfo = {
            'pivotA': {
                'pivot':str(pivot_A),
                'date': str(pivot_A.pivotInfo['pivotDate']),
                'high': str(pivot_A.pivotInfo['high']),
                'open': str(pivot_A.pivotInfo['open']),
                'low': str(pivot_A.pivotInfo['low']),
                'close': str(pivot_A.pivotInfo['close']),
            },
            'pivotB': {
                'pivot': str(pivot_B),
                'date': str(pivot_B.pivotInfo['pivotDate']),
                'high': str(pivot_B.pivotInfo['high']),
                'open':str(pivot_B.pivotInfo['open']),
                'low': str(pivot_B.pivotInfo['low']),
                'close': str(pivot_B.pivotInfo['close']),
            },
            'pivotC': {
                'pivot':str(pivot_C),
                'date': str(pivot_C.pivotInfo['pivotDate']),
                'high': str(pivot_C.pivotInfo['high']),
                'open':str(pivot_C.pivotInfo['open']),
                'low': str(pivot_C.pivotInfo['low']),
                'close': str(pivot_C.pivotInfo['close']),
            },
            'pivotD': {
                'pivot':str(pivot_D),
                'date': str(pivot_D.pivotInfo['pivotDate']),
                'high': str(pivot_D.pivotInfo['high']),
                'open':str(pivot_D.pivotInfo['open']),
                'low': str(pivot_D.pivotInfo['low']),
                'close': str(pivot_D.pivotInfo['close']),
            }
        }
      
        self.settings = settings
              
        self.pnl = {
            # 'risk': '%.2f'%(risk),
            # 'reward': '%.2f'%(reward),
            # 'stopLoss': '%.2f'%(stopLoss),
            # 'takeProfit': '%.2f'%(takeProfit),
            # 'pnl': self.getPNL(self.tradeInfo['closingTradeType'], self.tradeInfo['currentPrice'], pivot_C.pivotInfo['open']),
            # 'returnPercentage':'',
            'riskRewardRatio': 5,
        }
        
        self.retracement = {
            'bcRetracement': float(r1),
            'cdRetracement': float(c)
        }
        
        self.enterExitInfo = {
            # 'enterPrice': str(entryPrice),
            # 'enterDate': str(enterDate),
            # 'exitPrice': '%.2f'%(pivot_D.pivotInfo['close']),
            # 'exitDate': str(currentDate),
        }
        
        self.duration = {
    
            'bars':{
				# 'A_to_B': barsBetweenAandB,
				# 'B_to_C': barsBetweenBandC,
				# 'C_to_D': barsBetweenCandD,
                'ab_pct': '%.2f'%((barsBetweenAandB/barsBetweenAandB) * 100),
                'bc_pct': '%.2f'%((barsBetweenBandC/barsBetweenAandB) * 100),
                'cd_pct': '%.2f'%((barsBetweenCandD/barsBetweenAandB) * 100),
			},
			'days':{
	     		'A_to_B': '',
				'B_to_C': '',
				'C_to_D': '',
			}
        }
  
        self.movement = {
            'atoBMovement': '%.2f'%(float(self.pivotInfo['pivotA']['high']) - float(self.pivotInfo['pivotB']['low'])),
            'btoCMovement': '%.2f'%(float(self.pivotInfo['pivotC']['high']) - float(self.pivotInfo['pivotB']['low'])),
            'ctoDMovement': '%.2f'%(float(self.pivotInfo['pivotC']['high']) - float(self.pivotInfo['pivotD']['low'])),
            'aToBPct': 100,
            'bToCPct': '%.2f'%(((float(self.pivotInfo['pivotC']['high']) - float(self.pivotInfo['pivotB']['low'])) / (float(self.pivotInfo['pivotA']['high']) - float(self.pivotInfo['pivotB']['low']))) * 100),
            'cToDPct': '%.2f'%(((float(self.pivotInfo['pivotC']['high']) - float(self.pivotInfo['pivotD']['low'])) / (float(self.pivotInfo['pivotA']['high']) - float(self.pivotInfo['pivotB']['low']))) * 100),
            'aToB_pctInBars': 0,
            'bToC_pctInBars': 0,
            'cToD_pctInBars': 0,

        }
        
        # self.length = {
        #     'a_length': 0,
        #     'b_length': 0,
        #     'a_b_length': ab_full_length,
        #     'a_b_c_length': 0,
        #     'b_c_length': 0,
        #     'abcd_length': abcd_full_length,


        # }
    
    def getOHLCChartData(self, date ,open, high, low, close):

        chartData = []
        i = 0
    
        while str(date.date(ago=-i)) >= self.tradeInfo['startDate']:


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
    
    def getPNL(self, type, currentPrice, priceOfC):

        if type == 'Bull':

            pnl = priceOfC - currentPrice
            
            return '%.2f'%pnl
        
        if type == 'Bear':

            pnl = priceOfC - currentPrice
            
            return '%.2f'%pnl

    def getRiskReward(self, riskRewardRatio, pivotPair, priceOfC):
                        
        if(self.closingTradeType == 'Bear'):

            if(self.openingTradeType == 'Bull'):

                reward = '%.2f'%(priceOfC - pivotPair.pivot_one.close)
                risk = '%.2f'%(float(reward) / riskRewardRatio)

            if(self.openingTradeType == 'Bear'):

                reward = '%.2f'%(priceOfC - pivotPair.pivot_two.close)
                risk = '%.2f'%(float(reward) / riskRewardRatio)

            return risk, reward

        elif(self.closingTradeType == 'Bull'):
            
            if(self.openingTradeType == 'Bull'):
            
                reward = '%.2f'%(pivotPair.pivot_two.close - priceOfC)
                risk = '%.2f'%(float(reward) / self.riskRewardRatio)

            if(self.openingTradeType == 'Bear'):
            
                reward = '%.2f'%(priceOfC - pivotPair.pivot_one.close)
                risk = '%.2f'%(float(reward) / self.riskRewardRatio)
        
            return risk, reward

    def getStopLossAndTakeProfit(self, trade):

        if(self.closingTradeType == 'Bear'):
            
            if(self.openingTradeType == 'Bear'):
         
                takeProfit = '%.2f'%(self.pivotPair.pivot_two.open)
                stopLoss = '%.2f'%(self.priceOfC + abs(float(self.risk)))

            if(self.openingTradeType == 'Bull'):
                                
     
                takeProfit = '%.2f'%(self.pivotPair.pivot_one.close)
                stopLoss = '%.2f'%(self.priceOfC + abs(float(self.risk)))
          
            return stopLoss, takeProfit
    
        elif(self.closingTradeType == 'Bull'):
            
            if(self.openingTradeType == 'Bear'):

                takeProfit = '%.2f'%(self.pivotPair.pivot_open.open)
                stopLoss = '%.2f'%(self.priceOfC - abs(float(self.risk)))

            if(self.openingTradeType == 'Bull'):
                takeProfit = '%.2f'%(self.pivotPair.pivot_two.close)
                stopLoss = '%.2f'%(self.priceOfC - abs(float(self.risk)))
          
       
            
            return stopLoss, takeProfit

    def printData(self):
        ''
        print('C-High:',self.pivotC.high)
        print('C-Open:',self.pivotC.open)
        print('C-Close:',self.pivotC.close)
        print('C-Low:',self.pivotC.low)
        # print('pivotA:',self.pivotstr(A.date)
        # print('pivotB:',self.pivotB.date)
        # print('pivotC:',self.pivotC.date)
        # print('pivotD:',self.pivotD.date)
        # print('AB_size:', '%.2f'%(self.pivotstr(A.high - self.pivotB.low)) 
        # print('BC_size:', '%.2f'%(self.pivotC.high - self.pivotB.low), 'pct:','%.2f'%(((self.pivotC.high - self.pivotB.low) / (self.pivotstr(A.high - self.pivotB.low)) * 100)) 
        # print('CD_size:', '%.2f'%(self.pivotC.high - self.pivotD.low)) 
        # print('CD_size:', '%.2f'%(self.pivotC.high - self.pivotD.low)) 
        # print('Target:', '%.2f'%(self.pivotC.high - (self.pivotstr(A.high - self.pivotB.low)) )
        # print('', '%.2f'%((self.pivotB.low) - (self.pivotC.high - (self.pivotstr(A.high - self.pivotB.low))) )

        # print('%.2f'%(self.pivotB.low - self.pivotD.low))
        # print('%.2f'%(self.pivotC.high - self.pivotB.low))
        # print('bcRetracement',self.cdRetracement)
        # print('btoc', self.length_BtoC)
