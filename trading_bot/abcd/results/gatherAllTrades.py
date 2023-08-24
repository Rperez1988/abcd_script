def gatherAllTrades(openTrades, allTrades):
    
    
    for id, trade in openTrades.items():
        allTrades.append(trade)
    return allTrades