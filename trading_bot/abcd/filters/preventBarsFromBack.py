def preventPullingBarsFromBack(setting, currentDate, filterDate):

    match setting:

        case True: 
            if currentDate > filterDate:
                return True
        case False:
            return True

