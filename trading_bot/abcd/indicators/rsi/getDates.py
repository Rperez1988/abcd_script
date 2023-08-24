
def getDates(dates):

    alldates = []

    for each in reversed(range(1,30)):
        date = str(dates.date(-each))
        alldates.append(date)

    return alldates

