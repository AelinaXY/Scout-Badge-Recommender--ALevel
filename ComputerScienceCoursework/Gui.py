from easygui import *
import sys
from main import recommendation
import json
from csvimporting import csvImporting

# lets to user pick badges using the csv list of badges
def picker():
    try:
        msg = "Pick your badges"
        title = "Badge picker"
        badgeList = list(csvImporting().keys())
        badgeChoice = multchoicebox(msg, title, badgeList)
        if badgeChoice == None:
            mainFunc()
        choiceDict = {}
        for i in range(len(badgeList)):
            choiceDict[badgeList[i]] = 0
        for i in range(len(badgeChoice)):
            choiceDict[badgeList[badgeList.index(badgeChoice[i])]] = 1

    except TypeError:
        sys.exit(0)

    return choiceDict

# the main function for showing the user their recommendations
# it looks large but most of it is just one line which involves 10 variables
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


#A function for creating new recommendations
def newRecommendations():
    badges = picker()                   #goes off to the picker function to let the user pick badges
    recommendations = recommendation(badges)  #outputs a list of lists
    rec1 = []
    for i in range(len(recommendations)):
        tempRec = recommendations[i]
        rec1.append(tempRec[0])

    for i in range(len(list(badges.keys()))):
        if (list(badges.values()))[i] == 1:
            rec1.remove((list(badges.keys()))[i])

        # takes the final list of recommendations and inputs it into a json file
    with open('recommendations.json', 'w') as f:
        json.dump(rec1, f)

    return

# a function to remove badges from your pool of owned badges
# very messy code
def removeBadges():
    badgeDict = {}
    rec1 = []
    with open('recommendations.json') as json_file:     # opens the previous recommendations
        recommendations = list(json.load(json_file))

    badgeList = list(csvImporting().keys())      # imports a list of badges

    ownedBadges = [x for x in badgeList if x not in recommendations]     # finds out the badges the user owns

    choice = multchoicebox(msg="Please enter the badges you wish to remove", title="Remove Badges",
                           choices=ownedBadges)     # the user selects the badges they want gone
    newOwnedBadges = [x for x in ownedBadges if x not in choice] # creates a list of the new owned badges

    for i in range(len(badgeList)):     # converts it to dictionary form for the recommendation engine
        if badgeList[i] in newOwnedBadges:
            badgeDict[badgeList[i]] = 1
        else:
            badgeDict[badgeList[i]] = 0

    recommendations = recommendation(badgeDict)

    for i in range(len(recommendations)):   # creates a list of badges the user has been recommended
        rec1.append(recommendations[i][0])

    for i in range(len(list(badgeDict.keys()))):    # gets rid of done badges
        if (list(badgeDict.values()))[i] == 1:
            rec1.remove((list(badgeDict.keys()))[i])

    with open("recommendations.json", "w") as json_file:    # puts it back into the json file
        json.dump(rec1, json_file)

    recommendedBadges()     # shows the user the badges they want

# the main control function
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