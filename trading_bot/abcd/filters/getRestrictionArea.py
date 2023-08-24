

def filter_RestrictionArea(setting,pivotOnedate, date_time):
    
    match setting:

        case True:

            inRestrictionArea = setRestrictionArea(0, pivotOnedate, date_time)
            if not inRestrictionArea:
                return True
            else: 
                return False
        case False:
            return True

def setRestrictionArea(restrictionLength, pivotDate, currentDate) -> bool:

        currentBar = 0
        
        while currentBar <= restrictionLength + restrictionLength:
    
            if currentDate(ago=-currentBar) == pivotDate:
                
                return True
                
            currentBar +=1
