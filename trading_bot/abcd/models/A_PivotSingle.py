from datetime import datetime, timedelta
class A_PivotSingle():

    def __init__(self,
                    
            pivotID,
            pivotLetter,
            pivotColor,
            # paired,
            pivotDate,
            open,
            high,
            low,
            close,
            startDate,
            endDate,
            barsSincePreviousPivot,
            daysSincePreviousPivot,
            retracementPct,
            retracementPrice,
            full_length
            
        ):

        self.basicInfo = {
            'pivotID': pivotID,
            'pivotLetter': pivotLetter,
            'pivotColor': pivotColor,
            # 'paired': paired,
            'full_length': float(full_length)
        }
        
        self.pivotInfo = {
            'pivotStartDate': startDate,
            'pivotDate': pivotDate,
            'pivotEndDate': startDate,
            'open': open,
            'high': high,
            'close': close,
            'low': low,
            'startDate': startDate,
            'endDate': endDate,
        }
        
        self.duration = {
            'barsSincePreviousPivot':barsSincePreviousPivot,
            'daysSincePreviousPivot':daysSincePreviousPivot,
            'bars_passed': 0
        }
        
        self.bars = {
            '0':{
                    'high':None,
                    'close':None,
                    'open':None,
                    'low':None
                }
        }
        
        self.rectracement = {
            'pct': retracementPct,
            'price': retracementPrice,
        }
        self.currentLength = {
            'pct': 0
        }
        

        


