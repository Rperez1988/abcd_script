def createTrade(settingsName, openTrade, pivotPairID, stockName, pivotPair, filter, riskRewardRatio, marketType, date, open, high, low, close, initialType, settings, rsiNumber):



    stockName = stockName.replace('COINBASE:', '')
    
    # Basic Info
    openTrade.settingsName = settingsName
    openTrade.tradeID = pivotPairID
    openTrade.stockNameFull = None
    openTrade.stockNameSymbol = stockName
    openTrade.tradeResult = 'Live'
    openTrade.tradeOpen = True
    openTrade.tradeClosed = False   
    openTrade.pivotPair = pivotPair
    openTrade.riskRewardRatio = riskRewardRatio
    openTrade.snr = float(pivotPair.pivot_one.snr)

    # RSI
    openTrade.rsiOnEnter = float("%.2f"%pivotPair.pandasDF.iloc[-1]['rsi']) if filter == True else 0
    openTrade.tradeDuration = 0
                             
    # Dates
    openTrade.dateOfA = pivotPair.pivot_one.date
    openTrade.dateOfB = pivotPair.pivot_two.date
    openTrade.dateOfC = date.date(0)
    openTrade.tradeStartDate = pivotPair.pivot_one.tradeStartDate
    openTrade.tradeCloseDate = None
    
    # Prices
    openTrade.priceOfA = pivotPair.pivot_one.close
    openTrade.priceOfB = pivotPair.pivot_two.close
    openTrade.priceOfC = float(pivotPair.pivot_one.snr)
    openTrade.furthestOfA = pivotPair.pivot_one.high if marketType == 'Bear' else pivotPair.pivot_one.low

    # Market
    openTrade.openingTradeType = initialType
    openTrade.closingTradeType = openTrade.getTradeType(openTrade, initialType, filter, rsiNumber)
    openTrade.completeTradeType = openTrade.openingTradeType + '-' + openTrade.closingTradeType
    
    # Chart
    openTrade.chartData = openTrade.getOHLCChartData(openTrade, date, open, high, low, close)

     # Cash
    openTrade.pnl = openTrade.getPNL(openTrade, close[0])
    risk, reward = openTrade.getRiskReward(openTrade, riskRewardRatio, pivotPair)

    openTrade.risk = -abs(float(risk))
    openTrade.reward = abs(float(reward))
    stopLoss, takeProfit = openTrade.getStopLossAndTakeProfit(openTrade)
    openTrade.stopLoss = stopLoss
    openTrade.takeProfit = takeProfit

    openTrade.settings = settings

    return openTrade