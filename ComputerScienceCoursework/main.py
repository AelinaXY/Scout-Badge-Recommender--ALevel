import math

badgeDict = {
    'badge1': (1, 0, 0, 1, 1, 0),
    'badge2': (1, 1, 0, 0, 0, 0),
    'badge3': (1, 0, 0, 0, 0, 0),
    'badge4': (1, 1, 1, 1, 0, 1)
             }

sqrtd = {}
DF = {}
IDF = {}


def sqrtList(a):
    s = sum(a)
    return [x/(s**0.5) for x in a]

def listCount(a):
    count = 0
    for i in range(0,len(a)):
        if a[i] >0:
            count += 1
    return(count)

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




bd1 = list(badgeDict.keys())
bd2 = list(badgeDict.values())

for i in range(0,len(badgeDict)):
    sqrtd[bd1[i]] = sqrtList(bd2[i])
    DF[bd1[i]] = listCount(bd2[i])
    IDF[bd1[i]] = math.log10(len(bd1)/listCount(bd2[i]))

userBadges = userBadgesetup(bd1)
print(userBadgeProfile(sqrtd,userBadges))