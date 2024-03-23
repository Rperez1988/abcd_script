
class Pattern_A():

    def __init__(self,
            pattern_A_start_date,
            pattern_A_pivot_date,
            pattern_A_end_date,
            pattern_A_high,
            pattern_A_close,
            pattern_A_open,
            pattern_A_low,
            trade_symbol
        ):

        self.pattern_A_start_date = pattern_A_start_date
        self.pattern_A_pivot_date = pattern_A_pivot_date
        self.pattern_A_end_date = pattern_A_end_date
        self.pattern_A_open = pattern_A_open
        self.pattern_A_high = pattern_A_high
        self.pattern_A_close = pattern_A_close
        self.pattern_A_low = pattern_A_low
        self.trade_symbol = trade_symbol

        self.pattern_AB_bar_duration = 0
        

    def print_data(self):

        print('Pivot Date', self.pattern_A_pivot_date)

class Pattern_AB():
    
    def __init__(self, 
            
            # PATTERN A
            pattern_A_start_date,
            pattern_A_pivot_date, 
            pattern_A_end_date,
            pattern_A_high,
            pattern_A_close,
            pattern_A_open,
            pattern_A_low,

            # Pattern B
            pattern_B_start_date,
            pattern_B_pivot_date,
            pattern_B_end_date, 
            pattern_B_high,
            pattern_B_close,
            pattern_B_open,
            pattern_B_low,
            trade_symbol,

            # PATTERN AB
            pattern_AB_bar_duration, 


        ) -> None:
        
        self.trade_symbol = trade_symbol
        self.pattern_BC_bar_duration = 3

        # PATTERN A 
        self.pattern_A_start_date = pattern_A_start_date
        self.pattern_A_pivot_date = pattern_A_pivot_date
        self.pattern_A_end_date = pattern_A_end_date
        self.pattern_A_open = pattern_A_open
        self.pattern_A_high = pattern_A_high
        self.pattern_A_close = pattern_A_close
        self.pattern_A_low = pattern_A_low

        # PATTERN B
        self.pattern_B_start_date = pattern_B_start_date
        self.pattern_B_pivot_date = pattern_B_pivot_date
        self.pattern_B_end_date = pattern_B_end_date
        self.pattern_B_open = pattern_B_open
        self.pattern_B_high = pattern_B_high
        self.pattern_B_close = pattern_B_close
        self.pattern_B_low = pattern_B_low
    
        # PATTERN AB
        # self.pattern_AB_id = pattern_AB_id
        self.pattern_AB_start_date = pattern_A_start_date
        self.pattern_AB_end_date = pattern_B_end_date
        self.pattern_AB_bar_duration = pattern_AB_bar_duration
        

        self.failed_point = None

class Pattern_ABC():

    try:
        def __init__(self, 

                # Pattern A
                pattern_A_start_date,
                pattern_A_pivot_date, 
                pattern_A_end_date,
                pattern_A_high,
                pattern_A_close,
                pattern_A_open,
                pattern_A_low,

                # Pattern B
                pattern_B_start_date,
                pattern_B_pivot_date, 
                pattern_B_end_date,
                pattern_B_high,
                pattern_B_close,
                pattern_B_open,
                pattern_B_low,

                # Pattern C
                pattern_C_start_date,
                pattern_C_pivot_date, 
                pattern_C_end_date,
                pattern_C_high,
                pattern_C_close,
                pattern_C_open,
                pattern_C_low,
                
                # PATTERN AB
                pattern_AB_start_date,
                pattern_AB_end_date,
                pattern_AB_bar_length,

                # PATTERN ABC
                pattern_ABC_bar_length,
                pattern_ABC_start_date,
                pattern_ABC_end_date,
                pattern_C_bar_retracment,
                pattern_C_price_retracement,
                pattern_BC_bar_length,
                trade_symbol

            ) -> None:

            self.trade_symbol = trade_symbol
            # PATTERN A 
            # self.pattern_A_id = pattern_A_id
            # # self.pattern_A_pivot_color = pattern_A_pivot_color
            self.pattern_A_start_date = pattern_A_start_date
            self.pattern_A_pivot_date = pattern_A_pivot_date
            self.pattern_A_end_date = pattern_A_end_date
            self.pattern_A_open = pattern_A_open
            self.pattern_A_high = pattern_A_high
            self.pattern_A_close = pattern_A_close
            self.pattern_A_low = pattern_A_low

            # PATTERN B
            # # self.pattern_B_pivot_color = pattern_B_pivot_color
            self.pattern_B_start_date = pattern_B_start_date
            self.pattern_B_pivot_date = pattern_B_pivot_date
            self.pattern_B_end_date = pattern_B_end_date
            self.pattern_B_open = pattern_B_open
            self.pattern_B_high = pattern_B_high
            self.pattern_B_close = pattern_B_close
            self.pattern_B_low = pattern_B_low

            # Pattern C
            # # self.pattern_C_pivot_color = pattern_C_pivot_color
            self.pattern_C_start_date = pattern_C_start_date
            self.pattern_C_pivot_date = pattern_C_pivot_date
            self.pattern_C_end_date = pattern_C_end_date
            self.pattern_C_open = pattern_C_open
            self.pattern_C_high = pattern_C_high
            self.pattern_C_close = pattern_C_close
            self.pattern_C_low = pattern_C_low
        
            # PATTERN AB
            self.pattern_AB_start_date = pattern_AB_start_date
            self.pattern_AB_end_date = pattern_AB_end_date
            self.pattern_AB_bar_length = pattern_AB_bar_length

            # PATTERN ABC
            # self.pattern_ABC_id = pattern_ABC_id
            self.pattern_ABC_start_date = pattern_ABC_start_date
            self.pattern_ABC_end_date = pattern_ABC_end_date
            self.pattern_ABC_bar_length = pattern_ABC_bar_length
            self.pattern_C_bar_retracement = pattern_C_bar_retracment
            self.pattern_C_price_retracement = pattern_C_price_retracement
            self.pattern_BC_bar_length = pattern_BC_bar_length
            self.pattern_ABC_found_D = False
    except Exception as e:
        print(e)

class Pattern_ABCD():

    def __init__(self, 

            # Pattern A
            pattern_A_start_date,
            pattern_A_pivot_date, 
            pattern_A_end_date,
            pattern_A_high,
            pattern_A_close,
            pattern_A_open,
            pattern_A_low,

            # Pattern B
            pattern_B_start_date,
            pattern_B_pivot_date, 
            pattern_B_end_date,
            pattern_B_high,
            pattern_B_close,
            pattern_B_open,
            pattern_B_low,

            # Pattern C
            pattern_C_start_date,
            pattern_C_pivot_date, 
            pattern_C_end_date,
            pattern_C_high,
            pattern_C_close,
            pattern_C_open,
            pattern_C_low,
            
            # PATTERN AB
            pattern_AB_start_date,
            pattern_AB_end_date,
            pattern_AB_bar_length,

            # PATTERN ABC
            pattern_ABC_bar_length,
            pattern_ABC_start_date,
            pattern_ABC_end_date,
            pattern_C_bar_retracment,
            pattern_C_price_retracement,
            pattern_BC_bar_length,

            # PATTERN ABCD
            pattern_ABCD_id,
            pattern_ABCD_bar_length,
            pattern_ABCD_start_date,
            pattern_ABCD_end_date,
            pattern_D_bar_retracement,
            pattern_D_price_retracement,
            pattern_CD_bar_length,
            trade_symbol,

            # PIVOT PRICES
            pivot_A_price,
            pivot_B_price,
            pivot_C_price,
            pivot_D_price,

            # PATTERN PRICE LENGTHS
            ab_price_length,
            bc_price_length,
            cd_price_length,

            pivot_D_watchmark
    

        ) -> None:

        self.trade_symbol = trade_symbol

        # PATTERN A 
        self.pattern_A_start_date = pattern_A_start_date
        self.pattern_A_pivot_date = pattern_A_pivot_date
        self.pattern_A_end_date = pattern_A_end_date
        self.pattern_A_open = pattern_A_open
        self.pattern_A_high = pattern_A_high
        self.pattern_A_close = pattern_A_close
        self.pattern_A_low = pattern_A_low

        # PATTERN B
        self.pattern_B_start_date = pattern_B_start_date
        self.pattern_B_pivot_date = pattern_B_pivot_date
        self.pattern_B_end_date = pattern_B_end_date
        self.pattern_B_open = pattern_B_open
        self.pattern_B_high = pattern_B_high
        self.pattern_B_close = pattern_B_close
        self.pattern_B_low = pattern_B_low

        # Pattern C
        self.pattern_C_start_date = pattern_C_start_date
        self.pattern_C_pivot_date = pattern_C_pivot_date
        self.pattern_C_end_date = pattern_C_end_date
        self.pattern_C_open = pattern_C_open
        self.pattern_C_high = pattern_C_high
        self.pattern_C_close = pattern_C_close
        self.pattern_C_low = pattern_C_low
    
        # PATTERN AB
        self.pattern_AB_start_date = pattern_AB_start_date
        self.pattern_AB_end_date = pattern_AB_end_date
        self.pattern_AB_bar_length = pattern_AB_bar_length

        # PATTERN ABC
        self.pattern_ABC_start_date = pattern_ABC_start_date
        self.pattern_ABC_end_date = pattern_ABC_end_date
        self.pattern_ABC_bar_length = pattern_ABC_bar_length
        self.pattern_C_bar_retracement = pattern_C_bar_retracment
        self.pattern_C_price_retracement = pattern_C_price_retracement
        self.pattern_BC_bar_length = pattern_BC_bar_length

        # PATTERN ABCD
        self.pattern_ABCD_id = pattern_ABCD_id
        self.pattern_ABCD_bar_length = pattern_ABCD_bar_length
        self.pattern_ABCD_start_date = pattern_ABCD_start_date
        self.pattern_ABCD_end_date = pattern_ABCD_end_date
        self.pattern_D_bar_retracement = pattern_D_bar_retracement
        self.pattern_D_price_retracement = pattern_D_price_retracement
        self.pattern_CD_bar_length = pattern_CD_bar_length
        self.candle_ids = []
        self.pattern_d_created_date = None

        # PIVOT PRICES
        self.pivot_A_price = round(pivot_A_price,2)
        self.pivot_B_price = round(pivot_B_price,2)
        self.pivot_C_price = round(pivot_C_price,2)
        self.pivot_D_price = round(pivot_D_price,2)

        # PATTERN PRICE LENGTHS
        self.ab_price_length = round(ab_price_length,2)
        self.bc_price_length = round(bc_price_length,2)
        self.cd_price_length = round(cd_price_length,2)

        self.pivot_D_watchmark = pivot_D_watchmark

        

        # Trade
        self.trade_is_open = False
        self.trade_is_closed = None
        self.trade_entered_date = None
        self.trade_entered_price = None
        self.trade_exited_date = None
        self.trade_exited_price = None
        self.trade_risk = None
        self.trade_reward = None
        self.trade_take_profit = None
        self.trade_stop_loss = None
        self.trade_duration_bars = 0
        self.trade_duration_days = 0
        self.trade_pnl = None
        self.trade_result = None
        self.trade_return_percentage = None
        self.trade_rrr = 1
        self.trade_created = False
        self.trade_candle_ids = []
        self.current_date = None

        self.d_dropped_below_b = None