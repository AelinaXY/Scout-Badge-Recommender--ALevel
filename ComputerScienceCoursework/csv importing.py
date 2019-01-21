import csv
badgeDict ={}

with open('badges.csv', newline ='') as badges:
    badgereader = csv.reader(badges, delimiter=',', quotechar=')')
    badge = list(badgereader)

for i in range(0, len(badge)):
    tempList = badge[i]
    attList = []
    for j in range(1, len(tempList)):
        attList.append(tempList[j])
    badgeDict[tempList[0]] = attList
print(badgeDict['Snowsports'])
