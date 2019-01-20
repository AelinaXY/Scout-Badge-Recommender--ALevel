import math

badgeDict = {
    'potatoat': (1, 0, 0, 1, 1, 0, 0),
    'badge2': (1, 1, 0, 0, 0, 0, 1),
    'badge3': (1, 0, 0, 0, 0, 0, 1),
    'badge4': (0, 1, 1, 1, 0, 1, 0)
             }

sqrtd = {}
DF = []
IDF = []


def sqrtList(a):
    s = sum(a)
    return [x/(s**0.5) for x in a]

def listCount(a):
    count = 0
    for i in range(0,len(a)):
        if a[i] >0:
            count += 1
    return(count)

def listCount2(list):
    attributeList = []
    for i in range(0, len(list[0])):
        attributeList.append(0)
    for i in range(0, len(list)):
        tempList = list[i]
        for j in range(0, len(attributeList)):
            attributeList[j] += tempList[j]
    return attributeList

def userBadgesetup(badgeList):
    userBadges = {}
    userInput = 0
    print('Please enter the number value for the badges you have, one at a time')
    for i in range(0,len(badgeList)):
        print(f'Type {i} for: {badgeList[i]}')
        userBadges[badgeList[i]] = 0

    while userInput != 'exit':
        userInput = input()
        try:
            userBadges[badgeList[int(userInput)]] = 1
            print("SUCCESS")
        except:
            print("Please enter a valid input, if you want to leave type exit")

    return userBadges

def userBadgeProfile(badgeDict, userBadges):
    bdv = list(badgeDict.values())
    ubv = list(userBadges.values())
    userProfile = []
    for i in range(0, len(bdv[0])):
        userProfile.append(0)
    for i in range(0, len(bdv)):
        bdvi = bdv[i]
        ubvi = ubv[i]
        if ubvi == 1 :
            for j in range(0,len(bdvi)):
                userProfile[j] += bdvi[j]
    return(userProfile)

def finalRecommendations(sqrtd, userProfile, IDF):
    recs = {}
    sqrtdv = list(sqrtd.values())
    sqrtdk = list(sqrtd.keys())
    for i in range(0, len(sqrtd)):
        tempValue = 0
        tempList = sqrtdv[i]
        for j in range(0, len(tempList)):
            tempValue += (userProfile[j] * IDF[j] * tempList[j])
        recs[sqrtdk[i]] = tempValue
    return(recs)



bd1 = list(badgeDict.keys())
bd2 = list(badgeDict.values())

for i in range(0,len(badgeDict)):
    sqrtd[bd1[i]] = sqrtList(bd2[i])

DF = listCount2(bd2)

for i in range(0, len(DF)):
    IDF.append(math.log10(len(bd1)/DF[i]))
print(DF)
print(IDF)


userBadges = userBadgesetup(bd1)
userProfile = userBadgeProfile(sqrtd,userBadges)
print(finalRecommendations(sqrtd, userProfile, IDF))