from abcd_script.trading_bot.abcd.strategy.utilties import *

def get_entry_price(market, low, high):

    entry_price = None

    match market:

        case 'Bull':

            entry_price = low[0]

        case 'Bear':
        
            entry_price = high[0]


    return entry_price

def get_risk_and_reward(market, abcd, entry_price, rrr):


    match market:

        case 'Bull':

            pivotC_High = get_high_of_candle(
                abcd.pattern_C_open, 
                abcd.pattern_C_close
            )

            reward = pivotC_High - entry_price

            risk = reward / rrr

            return risk, reward
        
        case 'Bear':

            pivotC_Low = get_low_of_candle(abcd.pivot_C.pivotInfo['open'], abcd.pivot_C.pivotInfo['close'])

            reward = pivotC_Low - entry_price

            risk = reward / rrr

            return risk, reward

def checkIfQuadIsAlreadyInATrade(all_abcds, abcd_id):
    
    
    inTrade = False
    for each in all_abcds:
        if each.tradeInfo['id'] == abcd_id:
            inTrade = True
            break
    return inTrade 