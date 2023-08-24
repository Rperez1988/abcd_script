
class ABCD_PivotQuad():

    def __init__(self,
            
            pivotQuad_ID,
            pivot_A,
            pivot_B,
            pivot_C,
            pivot_D,
            barsBetweenBandC,
            abc_pivotTrio,
            d_to_a_retracement,
            rsi,
            full_length,
  

            # cd_pctInBars
        ) -> None:
        
        self.pivotQuad_ID = pivotQuad_ID
        self.pivot_A = pivot_A
        self.pivot_B = pivot_B
        self.pivot_C = pivot_C
        self.pivot_D = pivot_D
        self.barsBetweenBandC = barsBetweenBandC
        self.abc_pivotTrio =  abc_pivotTrio
        self.ab_pivotPair = abc_pivotTrio.ab_pivotPair
        self.tradeDuration = 0
        self.barsBetweenCandD = 1
        self.cd_pctInPrice = 1
        self.d_to_a_retracement = d_to_a_retracement
        self.rsi = rsi
        self.full_length = full_length
