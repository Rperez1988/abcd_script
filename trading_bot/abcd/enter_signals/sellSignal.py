def sell_signal_one(pivotPair) -> bool:
            
            """SELL SIGNAL ONE
            1. TWO PIVOTS ARE FORMED.
            2. FIRST PIVOT IS HIGHER THAN THE SECOND PIVOT.
            3. FIRST PIVOT IS A PIVOT HIGH.
            4. SECOND PIVOT IS A PIVOT LOW.
            """

            # Check if there are two pivots in     
            if len(pivotPair) == 2:

                """GRAB THE FIRST PIVOT PRICE"""
                firstPivot = pivotPair[0].close

                """GRAB THE SECOND PIVOT PRICE"""
                secondPivot = pivotPair[1].close

                """CHECK IF THE FIRST PIVOT PRICE IS HIGHER THAN THE SECOND PRICE"""         
                if firstPivot > secondPivot:
                    
                    """CHECK IF THE FIRST PIVOT IS A PIVOT HIGH"""
                    if pivotPair[0].type == "High":

                        """CHECK IF THE SECOND PIVOT IS A PIVOT LOW"""
                        if pivotPair[1].type == "Low":

                            return True

def isSupportAndResistanceHit(pivotPair: list, dataH, dataL) -> bool:

    # Get high of current bar.
    high = dataH

    # Get low of current bar.
    low  = dataL

    # Get pivot high snr.
    pivotOneSnR = pivotPair.pivot_one.snr
    
    # Check if current bar is touching pivot ones snr
    if high > float(pivotOneSnR) and low < float(pivotOneSnR):
        return True





            