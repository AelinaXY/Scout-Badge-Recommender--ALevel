from easygui import *
import sys
from main import recommendation
import json
from csvimporting import csvImporting


def picker():

    try:
        msg = "Pick your badges"
        title = "Badge picker"
        badgeList = list(csvImporting().keys())
        badgeChoice = multchoicebox(msg, title, badgeList)
        choiceDict = {}
        for i in range(len(badgeList)):
            choiceDict[badgeList[i]] = 0
        for i in range(len(badgeChoice)):
            choiceDict[badgeList[badgeList.index(badgeChoice[i])]] = 1

    except TypeError:
        sys.exit(0)

    return choiceDict


def output(recs):
    msg = ("The program believes you would like these badges: \n" + str(recs[0]) + "\n" + str(recs[1]) + "\n" + str(recs[2]) + "\n" + str(recs[3]) + "\n" + str(recs[4]))
    title = "Recommendations"

    if ccbox(msg, title):
        mainStartup()
        pass
    else:
        sys.exit(0)


def newRecommendations():
    badges = picker()
    recommendations = recommendation(badges)
    rec1 = []
    for i in range(len(recommendations)):
        tempRec = recommendations[i]
        rec1.append(tempRec[0])

    print(rec1)
    for i in range(len(list(badges.keys()))):
        if (list(badges.values()))[i] == 1:
            print ((list(badges.keys()))[i])
            rec1.remove((list(badges.keys()))[i])

    with open('recommendations.json', 'w') as f:
        json.dump(rec1, f)


    print("help", rec1)

    return rec1

def mainFunc():
    image = "logo.png"
    choice = buttonbox("Welcome to the Scout Badge Recommendation Engine", "Main", choices=["Quit", "Enter new recommendations", "Add New Badges", "Remove Badges", "Badges", "Your Recommended Badges"], image=image)

    if choice == "Enter new recommendations":
        newRecommendations()


mainFunc()