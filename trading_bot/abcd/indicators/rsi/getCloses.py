def getCloses(x):

    allCloses = []

    for each in reversed(range(1,30)):
     
        close = x[-each]
        xy = {'Close':float(close)}
        allCloses.append(xy)

    return allCloses