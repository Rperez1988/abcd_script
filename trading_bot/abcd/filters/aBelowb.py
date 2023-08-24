def check_pivot_b_position(pivotOne, pivotTwo, type):
        
    if type == 'Bear':
        if pivotOne.pivotInfo['high'] < pivotTwo.pivotInfo['low']:
            return True
        
    elif type == 'Bull':
        if pivotOne.pivotInfo['low'] > pivotTwo.pivotInfo['high']:
            return True

