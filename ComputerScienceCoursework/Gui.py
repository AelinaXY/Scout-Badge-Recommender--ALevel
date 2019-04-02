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

        if choice in recommendations:
            badgeFunc(choice)
    return


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

    recommendedBadges()

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

    try:
        choice = multchoicebox(msg="Please enter the badges you wish to remove", title="Remove Badges",
                           choices=ownedBadges)     # the user selects the badges they want gone
        newOwnedBadges = [x for x in ownedBadges if x not in choice] # creates a list of the new owned badges
        for i in range(len(badgeList)):  # converts it to dictionary form for the recommendation engine
            if badgeList[i] in newOwnedBadges:
                badgeDict[badgeList[i]] = 1
            else:
                badgeDict[badgeList[i]] = 0

        recommendations = recommendation(badgeDict)

        for i in range(len(recommendations)):  # creates a list of badges the user has been recommended
            rec1.append(recommendations[i][0])

        for i in range(len(list(badgeDict.keys()))):  # gets rid of done badges
            if (list(badgeDict.values()))[i] == 1:
                rec1.remove((list(badgeDict.keys()))[i])

        with open("recommendations.json", "w") as json_file:  # puts it back into the json file
            json.dump(rec1, json_file)

        recommendedBadges()  # shows the user the badges they want

    except:
        mainFunc()

    return

def addBadges():

    badgeDict = {}
    rec1 = []
    with open('recommendations.json') as json_file:
        recommendations = list(json.load(json_file))

    badgeList = list(csvImporting().keys())

    notOwnedBadges = [x for x in badgeList if x in recommendations]

    try:
        choice = multchoicebox(msg="Please enter the badges you wish to add", title="Add Badges",
                               choices=notOwnedBadges)

        ownedBadges = [x for x in badgeList if x not in recommendations]

        newOwnedBadges = ownedBadges + choice

        for i in range(len(badgeList)):
            if badgeList[i] in newOwnedBadges:
                badgeDict[badgeList[i]] = 1
            else:
                badgeDict[badgeList[i]] = 0

        recommendations = recommendation(badgeDict)

        for i in range(len(recommendations)):
            rec1.append(recommendations[i][0])

        for i in range(len(list(badgeDict.keys()))):
            if (list(badgeDict.values()))[i] == 1:
                rec1.remove((list(badgeDict.keys()))[i])

        with open("recommendations.json", "w") as json_file:
            json.dump(rec1, json_file)

        recommendedBadges()

    except:
        mainFunc()

    return

def allBadgeFunc():
    badgeList = list(csvImporting().keys())
    badgeChoice = choicebox(msg="Choose your badge", title="Badges", choices = badgeList)

    if badgeChoice == None:
        mainFunc()

    else:
        badgeFunc(badgeChoice)


def badgeFunc(choice):
    with open('badge.json') as json_file:
        badgeRequirements = json.load(json_file)[choice]
    selection = textbox(text=("{0}".format("\n\n".join(badgeRequirements))), msg="{0} \n Requirements:".format(choice), title=choice)

    if selection == None:
        mainFunc()
    if selection == "\n\n".join(badgeRequirements):
        badgeFuncImage(choice)

def badgeFuncImage(choice):
    image = "badges\{0}.png".format(choice)
    buttonbox(image=image, title=choice, choices=["Back"])
    badgeFunc(choice)

# the main control function
def mainFunc():
    image = "logo.png"
    choice = buttonbox("Welcome to the Scout Badge Recommendation Engine", "Main", choices=["Quit", "Enter new recommendations", "Add New Badges", "Remove Badges", "Badges", "Your Recommended Badges"], image=image)

    # If statements which control which way you go
    if choice == "Enter new recommendations":
        newRecommendations()

    if choice == "Your Recommended Badges":
        recommendedBadges()

    if choice == "Remove Badges":
        removeBadges()

    if choice == "Add New Badges":
        addBadges()

    if choice == "Badges":
        allBadgeFunc()

mainFunc()