import math
from csvimporting import csvImporting
from operator import itemgetter

badgeDict = {
    'badge1': (1, 0, 0, 1, 1, 0, 1),
    'badge2': (1, 1, 0, 0, 0, 0, 1),
    'badge3': (1, 0, 0, 0, 0, 0, 1),
    'badge4': (0, 1, 1, 1, 0, 1, 0)
             }


def recommendation(userBadges):
    sqrtd = {}


    def sqrtList(a):
        s = sum(a)
        return [x/(s**0.5) for x in a]

    def listCount(list):
        attributeList = []
        for i in range(0, len(list[0])):
            attributeList.append(0)
        for i in range(0, len(list)):
            tempList = list[i]
            for j in range(0, len(attributeList)):
                attributeList[j] += tempList[j]
        return attributeList

    def logList(DF):
        IDF = []
        for i in range(0, len(DF)):
            IDF.append(math.log10(len(bd1) / DF[i]))
        return(IDF)

    def userBadgesetup(badgeList):
        userBadges = {}
        userInput = 0
        increment = 0
        userHistory = []
        print('Please enter the number value for the badges you have, one at a time')
        for i in range(0,len(badgeList)):
            print(f'Type {i} for: {badgeList[i]}')
            userBadges[badgeList[i]] = 0

        while userInput != 'exit':
            userInput = input()
            try:
                userBadges[badgeList[int(userInput)]] = 1
                if increment == 0:
                    increment += 1
                    print("Do you have any other badges, if so input them in the same way. If not type 'exit' ")
                elif userInput in userHistory:
                    print("You already have that badge")
                    print("If you are done type 'exit'")
                else:
                    print("Badge Noted")

                userHistory.append(userInput)
            except:
                if userInput == 'exit':
                    print(userBadges)
                    return userBadges
                else:
                    print("Please enter a valid input, if you want to leave type 'exit'")


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

    badgeDict = csvImporting()


    bd1 = list(badgeDict.keys())
    bd2 = list(badgeDict.values())

    for i in range(0,len(badgeDict)):
        sqrtd[bd1[i]] = sqrtList(bd2[i])

    DF = listCount(bd2)
    IDF = logList(DF)

    #userBadges = userBadgesetup(bd1)
    userProfile = userBadgeProfile(sqrtd,userBadges)
    userRecommendations = finalRecommendations(sqrtd, userProfile, IDF)

                                    #print(userRecommendations)
    s = sorted(userRecommendations.items(), key=lambda x:(x[0],x[1]))
                                    #print(s)
    sortedUserRecs = sorted((dict(s)).items(), key=lambda x:(x[1]), reverse=True)
    #sortedUserRecs = sorted(userRecommendations.items(), key=lambda x: (x[1],x[0]), reverse=True)

    print(sortedUserRecs)

    return(sortedUserRecs)

