def getLeftAndRightOpenAndClosesOfPivot(close, open, length):
    
    leftSideClose   = []
    leftSideOpen    = []
    rightSideClose  = []
    rightSideOpen   = []
    
    for each in range(length):
        leftSideClose.append(close[-(each + (length+1))])
        leftSideOpen.append(open[-(each + (length+1))])

    for each in range(length):
        rightSideClose.append(close[-each])
        rightSideOpen.append(open[-each])


    return rightSideOpen, rightSideClose, leftSideOpen, leftSideClose