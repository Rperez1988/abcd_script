
class ABC_PivotTrio():

    def __init__(self, 

            pivotTrio_ID,
            pivotA, 
            pivotB, 
            pivotC, 
            barsBetweenBandC, 
            ab_pivotPair,
            bToC_pctInBars,
            full_length

        ) -> None:
        
        self.pivotTrio_ID = pivotTrio_ID
        self.pivot_A = pivotA
        self.pivot_B = pivotB
        self.pivot_C = pivotC
        self.barsBetweenBandC = barsBetweenBandC
        self.ab_pivotPair = ab_pivotPair
        self.found_D = False
        self.bToC_pctInBars = bToC_pctInBars
        self.bars_passed = 0
        self.full_length = full_length