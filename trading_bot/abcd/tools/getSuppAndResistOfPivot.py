from statistics import mean

def get_support_and_resistance( length, dataClose) -> None:

        closes = []        
    
        for x in range(length):
            closes.append(dataClose[-x])


        average = mean(closes)

        return '%.2f' % average

