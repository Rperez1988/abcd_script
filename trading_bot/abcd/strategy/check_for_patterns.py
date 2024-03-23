from abcd_script.trading_bot.abcd.strategy.abcd_entry import *
from abcd_script.trading_bot.abcd.filters.abnormalPriceJump import abnormalPriceJump
from abcd_script.trading_bot.abcd.filters.pivotSteepness import checkPivotSideSteepness
from abcd_script.trading_bot.abcd.pivot_screener.findPivot import findPivot
from abcd_script.trading_bot.abcd.strategy.check_for_pivot_B import *
from abcd_script.trading_bot.abcd.strategy.check_for_pivot_C import *
from abcd_script.trading_bot.abcd.strategy.check_for_pivot_D import *
import uuid

def check_for_pivot_A(
        
    date,
    data_close,
    data_open,
    pivot_length,
    market,
    abnormal_price_jump,
    pivot_steepness,
    a_pivots,
    data_high,
    data_low,
    symbol
    ):
            
    try:
        
        pivotType = findPivot('A',None, str(date(ago=-1)),data_close, data_open, pivot_length, market)

        if pivotType:
        
            isAbnormalPriceJump = abnormalPriceJump(abnormal_price_jump,pivot_length, data_open, data_close)
            
            if isAbnormalPriceJump:

                result, leftSideAverage, rightSideAverage = checkPivotSideSteepness(
                    pivot_steepness[0],
                    data_open, 
                    data_close, 
                    pivot_length,  
                    pivot_steepness[1])
                if result: 

                    pattern_A = Pattern_A(
                
                        date(ago=-2), # Pattern A start date
                        date(ago=-1), # Pattern A pivot date
                        date(ago=0), # Pattern A end date
                        data_high[-pivot_length],  # Pattern A pivot high
                        data_close[-pivot_length], # Pattern A pivot close
                        data_open[-pivot_length], # Pattern A pivot open
                        data_low[-pivot_length], # Pattern A pivot low
                        symbol
                    )
                
                    a_pivots.append(pattern_A)

    except Exception as e:
        print(f'check_for_pivot_A {e}')

def check_for_pivot_B(
        
    a_pivots,
    date,
    market,
    data_close,
    data_open,
    pivot_length,
    data_low,
    data_high,
    matched_pivot_ones,
    ab_pivotPairs,
    failed_AB_patterns,
    symbol
    ):

    try:
        for pivot_A in reversed(a_pivots):

                def remove_a():
                    pivot_A_top = get_high_of_candle(pivot_A.pattern_A_open, pivot_A.pattern_A_close)
                    current_candle_top = get_high_of_candle(data_open[0],data_close[0])

                    if current_candle_top > pivot_A_top:

                        a_pivots.remove(pivot_A)
                    
                remove_a()

                pivot_A.pattern_AB_bar_duration += 1

                is_B_found = find_B(
                    'B',
                    pivot_A, 
                    str(date(ago=-1)), 
                    market, 
                    data_close, 
                    data_open, 
                    pivot_length)

                if is_B_found:
                    
                    pattern_B_low = data_low[-1]
                    pattern_B_high = data_high[-1]
                    pattern_B_open = data_open[-1]
                    pattern_B_close = data_close[-1]
                    pattern_A_pivot_to_pattern_B_pivot_bar_length = check_bar_length(date, pivot_A.pattern_A_pivot_date)
                    is_ab_correct = check_ab_is_start_of_abcd(market, pivot_A.pattern_A_low, data_low)

                    candle_A_low = get_low_of_candle(pivot_A.pattern_A_open, pivot_A.pattern_A_close)
                    candle_A_high = get_high_of_candle(pivot_A.pattern_A_open, pivot_A.pattern_A_close)
                    candle_B_low = get_low_of_candle(pattern_B_open, pattern_B_close)
                    candle_B_high = get_high_of_candle(pattern_B_open, pattern_B_close)

                    
                    """
                    =========================================
                    is_ab_correct:

                        - Bull: Check if B low is lower than A high
                        - Bear: Check if B low is higher than an A high
                    =========================================

                    """
                    if is_ab_correct:
                        
                        is_A_the_lowest = check_if_A_is_the_lowest(
                            pivot_A.pattern_AB_bar_duration, 
                            data_open, 
                            data_close, 
                            candle_A_low, 
                        )
                        
                        is_A_the_highest = check_if_A_is_the_highest(
                            pattern_A_pivot_to_pattern_B_pivot_bar_length - 1, 
                            data_open, 
                            data_close,  
                            candle_A_high,
                        )
                        
                        is_B_the_lowest = check_if_B_is_the_lowest(
                            pivot_A.pattern_AB_bar_duration, 
                            data_open, 
                            data_close, 
                            candle_B_low
                        )
                        
                        is_B_the_highest = check_if_B_is_the_highest(
                            pivot_A.pattern_AB_bar_duration, 
                            data_open, 
                            data_close, 
                            candle_B_high
                        )
                                
                        is_correct_shape = check_if_A_to_B_is_correct_shape(
                            market, 
                            is_A_the_highest, 
                            is_B_the_lowest, 
                            is_A_the_lowest,
                            is_B_the_highest)

                        """
                        =========================================
                        is_correct_shape:

                            - Bull: Check if A is the high, and B is the low
                            - Bear: Check if A is the low, and B is the high
                        =========================================

                        """ 
                        if is_correct_shape:
                            
                            pattern_AB = Pattern_AB(
                            
                                # Pattern A
                                pivot_A.pattern_A_start_date,
                                pivot_A.pattern_A_pivot_date, 
                                pivot_A.pattern_A_end_date,
                                pivot_A.pattern_A_high,
                                pivot_A.pattern_A_close,
                                pivot_A.pattern_A_open,
                                pivot_A.pattern_A_low,

                                # Pattern B
                                date(ago=-(pivot_length * 2)), # Pattern B start date
                                date(ago=-pivot_length), # Pattern B pivot date
                                date(ago=0), # Pattern B end date
                                data_high[-pivot_length], # Pattern B pivot high
                                data_close[-pivot_length], # Pattern B pivot close
                                data_open[-pivot_length], # Pattern B pivot open
                                data_low[-pivot_length],  # Pattern B pivot low
                                symbol,
                                
                                pivot_A.pattern_AB_bar_duration, 

                                )

                            matched_pivot_ones.append(pivot_A.pattern_A_pivot_date)
                            ab_pivotPairs.append(pattern_AB)
                        
                        elif not is_correct_shape:
                        
                            pattern_AB = Pattern_AB(
                                    
                               # Pattern A
                                pivot_A.pattern_A_start_date,
                                pivot_A.pattern_A_pivot_date, 
                                pivot_A.pattern_A_end_date,
                                pivot_A.pattern_A_high,
                                pivot_A.pattern_A_close,
                                pivot_A.pattern_A_open,
                                pivot_A.pattern_A_low,

                                # Pattern B
                                date(ago=-(pivot_length * 2)), # Pattern B start date
                                date(ago=-pivot_length), # Pattern B pivot date
                                date(ago=0), # Pattern B end date
                                data_high[-pivot_length], # Pattern B pivot high
                                data_close[-pivot_length], # Pattern B pivot close
                                data_open[-pivot_length], # Pattern B pivot open
                                data_low[-pivot_length],  # Pattern B pivot low
                                symbol,
                                
                                pivot_A.pattern_AB_bar_duration, 
                                
                                    )

                            pattern_AB.failed_point = 'is_correct_shape'

                            failed_AB_patterns.append(pattern_AB)

                    elif not is_ab_correct:
                        
                        pattern_AB = Pattern_AB(
                            
                                # Pattern A
                                pivot_A.pattern_A_start_date,
                                pivot_A.pattern_A_pivot_date, 
                                pivot_A.pattern_A_end_date,
                                pivot_A.pattern_A_high,
                                pivot_A.pattern_A_close,
                                pivot_A.pattern_A_open,
                                pivot_A.pattern_A_low,

                                # Pattern B
                                date(ago=-(pivot_length * 2)), # Pattern B start date
                                date(ago=-pivot_length), # Pattern B pivot date
                                date(ago=0), # Pattern B end date
                                data_high[-pivot_length], # Pattern B pivot high
                                data_close[-pivot_length], # Pattern B pivot close
                                data_open[-pivot_length], # Pattern B pivot open
                                data_low[-pivot_length],  # Pattern B pivot low
                                symbol,
                                
                                pivot_A.pattern_AB_bar_duration, 
                                )

                        pattern_AB.failed_point = 'is_ab_correct'

                        failed_AB_patterns.append(pattern_AB)
    
    except Exception as e:
        print(f'check_for_pivot_B {e}')

def check_for_pivot_C(
    
    ab_pivotPairs,
    date,
    data_close,
    data_open,
    pivot_length,
    settings,
    data_high,
    data_low,
    market,
    abc_pivot_trios,
    symbol,

    ):

        for pivotPairID, pivotPair in enumerate(reversed(ab_pivotPairs)):

            def remove_b():

                pivot_B_low = get_low_of_candle(pivotPair.pattern_B_open, pivotPair.pattern_B_close)
                current_candle_low = get_low_of_candle(data_open[0],data_close[0])

                if current_candle_low < pivot_B_low:
                    ab_pivotPairs.remove(pivotPair)
                

            remove_b()



            pivotPair.pattern_BC_bar_duration += 1

            is_C_found = findPivot(
                'C',
                pivotPair, 
                str(date(ago=-1)), 
                data_close, 
                data_open, 
                int(pivot_length), 
                market)
            
            if is_C_found:

              
                
                    pattern_C_bar_retracement = ((pivotPair.pattern_BC_bar_duration)  / (pivotPair.pattern_AB_bar_duration)) * 100
                    pattern_C_price_retracement = get_pattern_c_price_retracement(
                        settings,
                        data_high[-pivot_length],
                        data_low[-pivot_length],
                        pivotPair.pattern_B_high,
                        pivotPair.pattern_B_low,
                        pivotPair.pattern_A_high,
                        pivotPair.pattern_A_low)
                    
                    pattern_ABC = Pattern_ABC(

                        # Pattern A
                        pivotPair.pattern_A_start_date,
                        pivotPair.pattern_A_pivot_date, 
                        pivotPair.pattern_A_end_date,
                        pivotPair.pattern_A_high,
                        pivotPair.pattern_A_close,
                        pivotPair.pattern_A_open,
                        pivotPair.pattern_A_low,

                        # Pattern B
                        pivotPair.pattern_B_start_date,
                        pivotPair.pattern_B_pivot_date, 
                        pivotPair.pattern_B_end_date,
                        pivotPair.pattern_B_high,
                        pivotPair.pattern_B_close,
                        pivotPair.pattern_B_open,
                        pivotPair.pattern_B_low,

                        date(ago=-(pivot_length * 2)),   # Pattern C start date
                        date(ago=-pivot_length),   # Pattern C start dat
                        date(ago=0),   # Pattern C start date
                        data_high[-pivot_length],   # Pattern C start date        
                        data_close[-pivot_length],   # Pattern C start date
                        data_open[-pivot_length],  # Pattern C start date      
                        data_low[-pivot_length],  # Pattern C start date

                        # PATTERN AB
                        pivotPair.pattern_AB_start_date,
                        pivotPair.pattern_AB_end_date,
                        pivotPair.pattern_AB_bar_duration,

                        # PATTERN ABC
                        pivotPair.pattern_BC_bar_duration + pivotPair.pattern_AB_bar_duration,
                        pivotPair.pattern_A_start_date,
                        date(0),
                        pattern_C_bar_retracement,
                        pattern_C_price_retracement,
                        pivotPair.pattern_BC_bar_duration,
                        symbol,

                    )                               
                    
                    # CHECK IF PATTERN IS THE HIGH & IF PATTERN B IS THE LOW              
                    if check_if_c_is_the_high_and_if_b_is_the_low(
                        settings,
                        data_open[-pivot_length],
                        data_close[-pivot_length], 
                        pivotPair.pattern_B_open,
                        pivotPair.pattern_B_close,
                        pivotPair.pattern_BC_bar_duration, 
                        data_open, 
                        data_close 
                    ):
                        

                        if pattern_C_price_retracement != None:
                        
                        
                            # CHECK PATTERN C PRICE RETRACEMENT    
                            if float(pattern_C_price_retracement) >= 1 and float(pattern_C_price_retracement) <= 100:
                                
                                # CHECK IF PATTERN C IS ABOVE PATTERN B & IF PATTERN C AND B ARE BELOW A
                                if check_pattern_ABC_shape(
                                    settings,
                                    data_high,
                                    data_low,
                                    pivotPair,
                                ):
                        
                                    abc_pivot_trios.append(pattern_ABC)

def check_for_pivot_D(
    abc_pivotTrios, 
    market,
    data_low,
    data_high,
    date,
    data_open,
    data_close,
    pattern_abcd,
    symbol,

    ):

    try:

        for pivotTrioID, pattern_ABC in enumerate(reversed(abc_pivotTrios)):
                
                def remove_c():
                    pivot_C_top = get_high_of_candle(pattern_ABC.pattern_C_open, pattern_ABC.pattern_C_close)

                    current_candle_top = get_high_of_candle(data_open[0],data_close[0])

                    if current_candle_top > pivot_C_top:
                        abc_pivotTrios.remove(pattern_ABC)
                
                remove_c()

                # GET D PRICE RETRACEMENT
                d_price_retracement = get_d_to_a_retracement(market,pattern_ABC,data_low,data_high)

                # PIVOT PRICES
                candle_C_top = pattern_ABC.pattern_C_open if pattern_ABC.pattern_C_open > pattern_ABC.pattern_C_close else pattern_ABC.pattern_C_close
                candle_A_top = pattern_ABC.pattern_A_open if pattern_ABC.pattern_A_open > pattern_ABC.pattern_A_close else pattern_ABC.pattern_A_close
                candle_B_bot = pattern_ABC.pattern_B_open if pattern_ABC.pattern_B_open < pattern_ABC.pattern_B_close else pattern_ABC.pattern_B_close
                candle_D_bot = data_open[0] if data_open[0] < data_close[0] else data_close[0]

                # PIVOT TO PIVOT PRICE LENGTH
                ab_length = candle_A_top - candle_B_bot
                bc_length = candle_C_top - candle_B_bot
                cd_length = candle_C_top - candle_D_bot

                # PIVOT D MARKER
                pivot_D_watchmark = candle_B_bot - 1

                # PIVOT TO PIVOT BAR LENGTH
                c_to_d_bar_length = check_bar_length(date, pattern_ABC.pattern_C_pivot_date)
                abcd_bar_length = check_bar_length(date, pattern_ABC.pattern_A_start_date)

                # CHECK IF PATTERNS SHAPE. (If C is the high, and D is the low)
                c_position = get_c_position(market, c_to_d_bar_length, pattern_ABC, data_open, data_close)
                d_position = get_d_position(market, c_to_d_bar_length, pattern_ABC, data_open, data_close)

                max_d_length_filter = pattern_ABC.pattern_AB_bar_length * 2

                # CD PRICE LENGTH VS BC PRICE LENGTH
                if cd_length > bc_length:
                    
                    # C THE HIGH & D THE LOW
                    if c_position and d_position:
                        
                        # FILTER D BAR LENGTH
                        if c_to_d_bar_length <= max_d_length_filter:

                            # CREATE PATTERN ABCD
                            abcd = Pattern_ABCD(
                                
                                # PATTERN A
                                pattern_ABC.pattern_A_start_date,
                                pattern_ABC.pattern_A_pivot_date, 
                                pattern_ABC.pattern_A_end_date,
                                pattern_ABC.pattern_A_high,
                                pattern_ABC.pattern_A_close,
                                pattern_ABC.pattern_A_open,
                                pattern_ABC.pattern_A_low,

                                # Pattern B
                                pattern_ABC.pattern_B_start_date,
                                pattern_ABC.pattern_B_pivot_date, 
                                pattern_ABC.pattern_B_end_date,
                                pattern_ABC.pattern_B_high,
                                pattern_ABC.pattern_B_close,
                                pattern_ABC.pattern_B_open,
                                pattern_ABC.pattern_B_low,

                                # Pattern C
                                pattern_ABC.pattern_C_start_date,
                                pattern_ABC.pattern_C_pivot_date, 
                                pattern_ABC.pattern_C_end_date,
                                pattern_ABC.pattern_C_high,
                                pattern_ABC.pattern_C_close,
                                pattern_ABC.pattern_C_open,
                                pattern_ABC.pattern_C_low,

                                # PATTERN AB
                                pattern_ABC.pattern_AB_start_date,
                                pattern_ABC.pattern_AB_end_date,
                                pattern_ABC.pattern_AB_bar_length,

                                # PATTERN ABC
                                pattern_ABC.pattern_ABC_bar_length,
                                pattern_ABC.pattern_ABC_start_date,
                                pattern_ABC.pattern_ABC_end_date,
                                pattern_ABC.pattern_C_bar_retracement,
                                pattern_ABC.pattern_C_price_retracement,
                                pattern_ABC.pattern_BC_bar_length,


                                # PATTERN ABCD
                                uuid.uuid4(),
                                abcd_bar_length,
                                pattern_ABC.pattern_A_start_date,
                                date(ago=0),
                                d_price_retracement,
                                d_price_retracement, 
                                c_to_d_bar_length,
                                symbol,

                                # PIVOT PRICES
                                candle_A_top,
                                candle_B_bot,
                                candle_C_top,
                                candle_D_bot,

                                # PATTERN PRICE LENGTHS
                                ab_length,
                                bc_length,
                                cd_length,

                                pivot_D_watchmark



                                # pattern_ABC.pattern_A_open if pattern_ABC.pattern_A_open > pattern_ABC.pattern_A_close else pattern_ABC.pattern_A_close,

                            )

                            pattern_ABC.pattern_ABC_found_D = True
                            pattern_abcd.append(abcd)
    
    except Exception as e:
        print(f'check_for_pivot_D {e}')

def enter_trade(pattern_abcd, date, volume, market,data_low, data_high, rrr):
    
    try:
            
        for abcdID, abcd in enumerate(pattern_abcd):
        

            if abcd.trade_created == False:

                abcd.trade_created = True

                abcd.trade_is_open = True
                # Enter Trade
                abcd.trade_is_open = True
                abcd.trade_is_closed = False
                abcd.trade_entered_date = date(ago=0)
                abcd.trade_entered_price = get_entry_price(market, data_low, data_high)
                # abcd.risk, abcd.reward = get_risk_and_reward(market, abcd, abcd.trade_entered_price, abcd.rrr)
                abcd.trade_reward = round(abcd.pattern_C_high - abcd.trade_entered_price,2)
                abcd.trade_risk = round(abcd.trade_reward,2)
                abcd.trade_take_profit = round(abcd.trade_entered_price + abcd.trade_reward,2)
                abcd.trade_stop_loss = round(abcd.trade_entered_price - abcd.trade_reward,)
                abcd.current_date = date(ago=0)
                abcd.d_dropped_below_b = date(ago=0)
                
             
    
    except Exception as e:
        print(f'enter trade {e}')
            
def exit_trade(pattern_abcd, data_open, data_close, date, data, ids):

    try:

        for each in pattern_abcd:
            

            if each.trade_is_open == True and each.trade_is_closed == False:
                
                # TRACK TRADE DURATION
                each.trade_duration_bars += 1
                each.current_date = date(ago=0)

                # TRACK IF CURRENT PRICE IS HIGHER OR LOWER THAN ENTRY PRICE
                z = each.trade_entered_price - data_close[0]
                y = data_close[0] - each.trade_entered_price

                # ASSIGN DIFFERENCE TO PNL
                each.trade_pnl = round(y if data_close[0] > each.trade_entered_price else z,2)
                
                # TRACK LOWEST PRICE DROPPED
                # low = get_low_of_candle(data_open[0], data_close[0])
                
                # if low < float(each.tradeInfo['lowest_price_dropped']):
                #     each.tradeInfo['lowest_price_dropped'] = str(low)


                is_open_higher_than_take_profit = data_open[0] > each.trade_take_profit
                is_close_higher_then_take_profit = data_close[0] > each.trade_take_profit

                is_open_lower_than_stop_loss = data_open[0] < each.trade_stop_loss
                is_close_lower_than_stop_loss = data_close[0] < each.trade_stop_loss

                take_profit_market_hit = is_open_higher_than_take_profit or is_close_higher_then_take_profit
                stop_loss_market_hit = is_open_lower_than_stop_loss or is_close_lower_than_stop_loss

                each.trade_candle_ids = []
                # GATHER CANDLE IDS OF ABCD PATTERN
                current_index = len(data) - 1
                length = (each.pattern_ABCD_bar_length + each.trade_duration_bars) - 1
                for _ in range(length):    
                    each.trade_candle_ids.append(ids[current_index])
                    current_index-=1
                # each.trade_candle_ids.reverse()

                if take_profit_market_hit or stop_loss_market_hit:

                    each.trade_is_open = False
                    each.trade_is_closed = True  
                    each.trade_exited_date = date(ago=0)

                    if take_profit_market_hit:

                        
                        each.trade_pnl = round(each.trade_reward,2)
                        each.trade_result = 'Win'
                        each.trade_exited_price = each.trade_take_profit
                        each.trade_return_percentage = round((each.trade_reward / each.trade_entered_price) * 100,2)
                    
                    if stop_loss_market_hit:

                        each.trade_pnl = round(each.trade_risk,2)
                        each.trade_result = 'Lost'
                        each.trade_exited_price = each.trade_stop_loss
                        each.trade_return_percentage = round((each.trade_risk / each.trade_entered_price) * 100,2)

                    
                    # GATHER CANDLE IDS OF ABCD PATTERN
                    current_index = len(data) - 1
                    length = (each.pattern_ABCD_bar_length + each.trade_duration_bars) - 1
                    for _ in range(length):    
                        each.trade_candle_ids.append(ids[current_index])
                        current_index-=1
                    
                    each.trade_candle_ids.reverse()

          
    except Exception as e:
        print(f'check for exit {e}')
        