import backtrader as bt

def createCerebro(btFeed, strat, stockName, settings):

 
    cerebro = bt.Cerebro(writer=False)
    cerebro.adddata(btFeed)
    cerebro.addstrategy(strat, 
            settingsName=settings['settingsName'],
            stockName=stockName, 
            market = settings['market'],
            pivotLength= settings['pivotLength'],
            rrr=settings['rrr'],
            sAndR=settings['s&r'],
            maxAtoBLength=settings['maxAtoBLength'],
            maxBtoCLength=settings['maxBtoCLength'],
            maxCtoDLength=settings['maxCtoDLength'],
            entryRSI=settings['entryRSI'],
            abnormalPriceJump=settings['abnormalPriceJump'],
            pivotSteepness=settings['pivotSteepness'],
            aBelowB=settings['aBelowB'],
        )
    cerebro.addanalyzer(bt.analyzers.TradeAnalyzer, _name="ta")
    cerebro.addanalyzer(bt.analyzers.SQN, _name="sqn")

    cerebro.run()
 