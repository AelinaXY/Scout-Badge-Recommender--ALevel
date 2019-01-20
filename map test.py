import math

badgedict = {
    'badge1': (1, 0, 0, 1, 1, 0),
    'badge2': (1, 1, 0, 0, 0, 0),
    'badge3': (1, 0, 0, 0, 0, 0),
    'badge4': (1, 1, 1, 1, 0, 1)
             }
sqrtd = {}
DF = {}
IDF =  {}


def sqrtList(a):
    s = sum(a)
    return [x/(s**0.5) for x in a]

def listCount(a):
    count = 0
    for i in range(0,len(a)):
        if a[i] >0:
            count += 1
    return(count)


bd1 = list(badgedict.keys())
bd2 = list(badgedict.values())

for i in range(0,len(badgedict)):
    sqrtd[bd1[i]] = sqrtList(bd2[i])
    DF[bd1[i]] = listCount(bd2[i])
    IDF[bd1[i]] = math.log10(len(bd1)/listCount(bd2[i]))

