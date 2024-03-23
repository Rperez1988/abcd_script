
import uuid


class ABCD_PivotQuad():

    def __init__(self,
            
            # 
            abcd_pattern_id,


            
            d_price_retracement,
       

            symbol,
            start_date,
            end_date,
     
            market_type,
            trade_result,
            trade_start_date,
            trade_end_date,
            current_price,
            current_date,
            lowest_price_dropped,
            pattern_A_date,
            pattern_A_high,
            pattern_A_close,
            pattern_A_open,
            pattern_A_low,
            pattern_B_date,
            pattern_B_high,
            pattern_B_close,
            pattern_B_open,
            pattern_B_low,
            pattern_C_date,
            pattern_C_high,
            pattern_C_close,
            pattern_C_open,
            pattern_C_low,
            pattern_D_date,
            pattern_D_high,
            pattern_D_close,
            pattern_D_open,
            pattern_D_low,
            risk,
            reward,
            stop_loss,
            take_profit,
            pnl,
            enter_price,
            exit_price,
            entered_date,
            exited_date,
            return_percentage,
            pattern_AB_length,
            pattern_BC_length,
            pattern_CD_length,
            pattern_ABC_length,
            pattern_ABCD_length



  

            # cd_pctInBars
        ) -> None:
        
        self.abcd_pattern_id = abcd_pattern_id
        self.symbol = symbol
        self.d_price_retracement = d_price_retracement
        self.tradeDuration = 0
        self.rsi = None
        self.abcd_length_in_bars = None
        
        


        self.abcd_start_date = start_date
        self.abcd_end_date = end_date
        self.market_type = market_type
        self.current_price = current_price
        self.current_date = current_date

        # 'rsi': '%.2f'%(rsi), 
        #     'volume': volume,
        #     'abcd_volumes': str(prev_bars_volume),
        #     'average_volume':  average_volume,
        #     'percentage_change': '%.2f'%(percentage_change)

        # TRADE INFO
        self.is_trade_open = False
        self.is_trade_closed = None
        self.trade_duration = None
        self.trade_result = trade_result
        self.trade_start_date = trade_start_date
        self.trade_end_date = trade_end_date
        self.lowest_price_dropped = lowest_price_dropped

        # PATTERN A
        self.pattern_A_date = pattern_A_date
        self.pattern_A_high = pattern_A_high
        self.pattern_A_close = pattern_A_close
        self.pattern_A_open = pattern_A_open
        self.pattern_A_low = pattern_A_low

        # PATTERN B
        self.pattern_B_date = pattern_B_date
        self.pattern_B_high = pattern_B_high
        self.pattern_B_close = pattern_B_close
        self.pattern_B_open = pattern_B_open
        self.pattern_B_low = pattern_B_low

        # PATTERN C
        self.pattern_C_date = pattern_C_date
        self.pattern_C_high = pattern_C_high
        self.pattern_C_close = pattern_C_close
        self.pattern_C_open = pattern_C_open
        self.pattern_C_low = pattern_C_low

        # PATTERN D
        self.pattern_D_date = pattern_D_date
        self.pattern_D_high = pattern_D_high
        self.pattern_D_close = pattern_D_close
        self.pattern_D_open = pattern_D_open
        self.pattern_D_low = pattern_D_low

        # PNL
        self.risk = risk
        self.reward = reward
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.pnl = pnl 
        self.entered_price = enter_price
        self.exited_price = exit_price
        self.entered_date = entered_date
        self.exited_date = exited_date
        self.return_percentage = return_percentage

        # LENGTH BARS
        self.pattern_AB_length_bars = pattern_AB_length
        self.pattern_BC_length_bars = pattern_BC_length
        self.pattern_CD_length_bars = pattern_CD_length
        self.pattern_ABC_length_bars = pattern_ABC_length
        self.pattern_ABCD_length_bars = pattern_ABCD_length

        # LENGTH DAYS
        self.pattern_AB_length_days = pattern_AB_length
        self.pattern_BC_length_days = pattern_BC_length
        self.pattern_CD_length_days = pattern_CD_length
        self.pattern_ABC_length_days = pattern_ABC_length
        self.pattern_ABCD_length_days = pattern_ABCD_length

        # PRICE LENGTH PCT
        self.A_to_B_price_length_pct = None
        self.B_to_C_price_length_pct = None
        self.C_to_D_price_length_pct = None

        # BAR LENGTH PCT
        self.A_to_B_bar_length_pct = None
        self.B_to_C_bar_length_pct = None
        self.C_to_D_bar_length_pct = None

        # RETRACEMENT
        self.C_retracement = None
        self.D_retracement = None