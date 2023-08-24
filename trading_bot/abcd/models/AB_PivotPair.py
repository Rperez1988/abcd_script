class AB_PivotPair():
    
    def __init__(self, 
            pivot_A, 
            pivot_B, 
            pivotPair_ID, 
            full_length

        ) -> None:

        self.pivotPairID = pivotPair_ID
        self.pivot_A = pivot_A
        self.pivot_B = pivot_B
        self.bars_passed = 0
        self.full_length = full_length
