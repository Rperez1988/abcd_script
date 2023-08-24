def pivotTwotoTradeLength(setting, pivotPair,pivotTwotoShortLength, length):

    match setting:

        case True: 


            if pivotPair.days_passed + length <= pivotTwotoShortLength:
         

                return True
        case False:

            return True
