from easygui import *
import sys
from main import recommendation

while False:
    msgbox("Hello, world!")

    msg ="What is your favorite flavor?"
    title = "Ice Cream Survey"
    choices = ["Vanilla", "Chocolate", "Strawberry", "Rocky Road"]
    choice = choicebox(msg, title, choices)

    # note that we convert choice to string, in case
    # the user cancelled the choice, and we got None.
    msgbox("You chose: " + str(choice), "Survey Result")

    msg = "Do you want to continue?"
    title = "Please Confirm"
    if ccbox(msg, title):     # show a Continue/Cancel dialog
        pass  # user chose Continue
    else:
        sys.exit(0)           # user chose Cancel

def picker():

    try:
        msg = "Pick your badges"
        title = "Badge picker"
        choices = ["Gold Chief Scout Award",
    "Adventure Challenge",
    "Creative Challenge",
    "Expedition Challenge",
    "Outdoor Challenge",
    "Skills Challenge",
    "Team Leader Challenge",
    "Teamwork Challenge",
    "World Challenge",
    "Activity Centre Service",
    "Air Researcher",
    "Air Spotter",
    "Air or Sea Navigation",
    "Angler",
    "Artist",
    "Astronautics",
    "Astronomer",
    "Athletics",
    "Athletics Plus",
    "Camper",
    "Caver",
    "Chef",
    "Circus Skills",
    "Cyclist",
    "DIY",
    "Dragon Boating",
    "Electronics",
    "Entertainer",
    "Enviromental Conservation",
    "Equestrian",
    "Farming",
    "Fire Safety",
    "Forester",
    "Fundraising",
    "Geocaching",
    "Global Issues",
    "Hill Walker",
    "Hobbies",
    "International",
    "Librarian",
    "Lifesaver",
    "Local Knowledge",
    "Martial arts",
    "Master at Arms",
    "Mechanic",
    "Media Relations and Marketing",
    "Meteorologist",
    "Model Maker",
    "My Faith",
    "Naturalist",
    "Orienteer",
    "Parasecending",
    "Photographer",
    "Physical Recreation",
    "Pioneer",
    "Power Coxswain",
    "Pulling(Rowing)",
    "Quartermaster",
    "Snowsports",
    "Sports Enthusiast",
    "Street Sports",
    "Survival Skills",
    "Water Activities",
    "World Faiths",
    "Writer",
    "Air Activites",
    "Community Impact",
    "Digital Citizen",
    "Digital Maker",
    "Emergency Aid",
    "Hikes Away",
    "Musician",
    "Nautical Skills",
    "Navigator",
    "Nights Away",
    "Paddle Sports",
    "Sailing",
    "Snowsports",
    "Swimmer",
    "Time on the Water",
    ]
        choice = multchoicebox(msg,title,choices)
        choicedict = {}
        for i in range(len(choices)):
            choicedict[choices[i]] = 0
        for i in range(len(choice)):
            choicedict[choices[choices.index(choice[i])]] = 1
        print(choicedict)

    except TypeError:
        sys.exit(0)


    return (choicedict)

def output(recs):
    msg = ("The program believes you would like these badges: \n" + str(recs[0]) + "\n" + str(recs[1]) + "\n" + str(recs[2]) + "\n" + str(recs[3]) + "\n" + str(recs[4]))
    title = ("Recommendations")

    if ccbox(msg, title):
        recomendor()
        pass
    else:
        sys.exit(0)


def recomendor():
    badges = picker()
    recommendations = recommendation(badges)
    rec1 = []
    for i in range(len(recommendations)):
        temprec = recommendations[i]
        rec1.append(temprec[0])
    output(rec1)

recomendor()

