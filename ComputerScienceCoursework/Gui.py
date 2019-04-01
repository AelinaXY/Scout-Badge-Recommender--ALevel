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


def recommendedBadges():
    with open('recommendations.json') as json_file:
        recommendations = list(json.load(json_file))

        if len(recommendations) <= 5:
            msgbox(msg="This application cannot help you as you know what you need to do. \n Go and do it, We believe in you!", title="Yay!")
            mainFunc()

        print(recommendations[0])
        image = "badges\{0}.png".format(recommendations[0])
        choice = buttonbox("We believe that you would like {0}, {1}, {2}, {3}, {4} \n Click the badge you want to find out more about, or click back".format(recommendations[0], recommendations[1], recommendations[2], recommendations[3], recommendations[4]), title="Recommendations", choices=(["Back", recommendations[0], recommendations[1], recommendations[2], recommendations[3], recommendations[4]]), image=image)
        if choice == "Back":
            mainFunc()

        if choice == image:
            badgeFunc(recommendations[0])

        for i in range(5):
            if choice == recommendations[i]:
                badgeFunc(recommendations[i])



def newRecommendations():
    badges = picker()
    recommendations = recommendation(badges)
    rec1 = []
    for i in range(len(recommendations)):
        tempRec = recommendations[i]
        rec1.append(tempRec[0])

    for i in range(len(list(badges.keys()))):
        if (list(badges.values()))[i] == 1:
            rec1.remove((list(badges.keys()))[i])

    with open('recommendations.json', 'w') as f:
        json.dump(rec1, f)

    return

def removeBadges():

    with open('recommendations.json') as json_file:
        recommendations = list(json.load(json_file))

    choice = multchoicebox(msg="Please enter the badges you wish to remove", title="Remove Badges", choices=recommendations)

    recommendations = [x for x in recommendations if x not in list(choice)]

    with open("recommendations.json", "w") as json_file:
        json.dump(recommendations, json_file)


def mainFunc():
    image = "logo.png"
    choice = buttonbox("Welcome to the Scout Badge Recommendation Engine", "Main", choices=["Quit", "Enter new recommendations", "Add New Badges", "Remove Badges", "Badges", "Your Recommended Badges"], image=image)

    if choice == "Enter new recommendations":
        newRecommendations()
        recommendedBadges()

    if choice == "Your Recommended Badges":
        recommendedBadges()

    if choice == "Remove Badges":
        removeBadges()

mainFunc()