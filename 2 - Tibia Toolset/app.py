from flask import Flask, render_template, request, session, redirect
import json
import math
from static.validateCharacter import validateCharacter
from datetime import timedelta
import static.schedule


"""
v0.0    Initialize project and create Selenium + Beautiful Soup scraper inside app.py file. Only working for Collabra world
v0.1    Move Selenium + BS to getCharacters.py file
v0.2    Add /partyleads and /friends routes
v0.3    Add feature to /partyleads where you can select vocation and lvl to get possible party members
v0.4    Add schedule.py and scheduler to getCharacters.py so you don't have to run that file on every call to any route
v0.5    Factorize getCharacters so it get all character from all worlds, not just Collabra
v0.6    Done on scheduler and error 403 on multiple requests
v0.7    Add support to run locally
v0.8    Refactorizing to getWorlds.py and getCharacters.py, instead of all in one python script; and refactorizing schedule to only run getWorlds when necessary; and added world support to /partyleads route
v0.9    Add comments to code; Support to add friends lo look for; session permanent to keep friends for 31 days; and support for capitalize /friends
v0.10   Validate /partyleads and /friends inputs; and comments to /friends; and change capitalize() for title() on /friends user input; and Capitalized names when scrapping in getCharacters.py (some old char names don't have each word of name capitalized)
v0.11   Validate if /friends user input does exist as a character; and refactor all open to with statements to avoid memory leaks; and create a character validator; and improve time of execution of character validator storing validated characters in a json (WILL NEED TO SCHEDULE A MONTHLY PROCCESS TO RECHECK THIS); and create own timer module to refactor the affected parts of the code; and refactor all code to use myTimer module

v0.12 --- WORKING IN GET NAME OF CALLER MODULE FOR myTimer (IT STICKS WITH THE FIRST TIME CALLED because code runs once only on import)


"""

#Set up flask app
app = Flask(__name__)
#Set up secret key for security issues
app.secret_key = 'THIS_IS_THE_KEY'
app.permanent_session_lifetime = timedelta(days=31)

VOCATIONS = ['All', 'Elite Knight', 'Royal Paladin', 'Master Sorcerer', 'Elder Druid']

#Define app routes and logic inside each route

#Show all characters online
@app.route("/")
def index():
    with open("data/data.json","r") as data:
        data_dict = json.load(data)
        players = len(data_dict)

    return render_template("index.html", data = data_dict, players = players)

#Show possible party members based on user choices
@app.route("/partyleads", methods=["GET", "POST"])
def party():

    if request.method == "POST":

        #Validate user lvl
        if request.form.get("user"):
            userLvl = request.form.get("user")
        else:
            return render_template("error.html",error = "No user Lvl input")
        
        try:
            userLvl = int(userLvl)
        except:
            return render_template("error.html", error = "Level must be a number")
        
        #Calculate max and min lvl to party
        maxLvl = math.floor(userLvl * 3/2)
        minLvl = math.ceil(userLvl * 2/3)

        #Validate user vocation
        if request.form.get('voc') in VOCATIONS:
            userElection = request.form.get('voc')
        else:
            return render_template("error.html", error = "Wrong Vocation")

        #Get worlds for validation
        with open("data/worlds.json","r") as worlds:
            worlds_dict=json.load(worlds)

        #Validate user world
        userWorld = None
        for x in worlds_dict:
            if request.form.get('world') == x["worldName"]:
                userWorld = request.form.get('world')
                break
            
        if not userWorld:
            return render_template("error.html", error = "Wrong world")

        #Open json data
        with open("data/data.json","r") as data:
            data_dict = json.load(data)

        party = []

        #Check possible party and store it in party list
        for x in data_dict:
            if (int(x['level']) >= minLvl and int(x['level']) <= maxLvl) and userWorld == x['world']:
                if userElection == "All":
                    party.append(x)
                elif x['vocation'] == userElection:
                    party.append(x)
                
        return render_template("partyleads.html",data=party,selectedLevel=userLvl,selectedVoc=userElection, selectedWorld = userWorld, worlds = worlds_dict)
    
    else:
        with open("data/worlds.json","r") as worlds:
            worlds_dict=json.load(worlds)

        return render_template("partyleads.html", worlds = worlds_dict)

#Show friends online
@app.route("/friends", methods=['GET','POST'])
def friend():

    #Create session if not exist
    if "friends" not in session:
        session["friends"] = []
    
    #Declarate that session will last (serverside) as long as configured
    session.permanent = True

    #Create list of friends online
    friendsOnline = []

    #Get new friend if user inputs new friend
    #Validate if friend already exist in friendList
    if request.method == 'POST':
        userInput = request.form.get('friendName').title()
        
        #Valdiate input no blank
        if not userInput:
            return render_template("error.html", error = "Can't add blank friend")
        
        #Validate input no numeric
        try:
            userInput = float(userInput)
        except:
            pass
        else:
            return render_template("error.html", error = "Can't add a number as a name")

        #Check if character exist
        if not validateCharacter(userInput):
            return render_template("error.html", error = "Can't add a character that does not exist")

        #Add friend to session friends list
        if userInput not in session["friends"]:
            session["friends"].append(userInput)

    #Open data characters
    with open("data/data.json","r") as data:
        data_dict = json.load(data)

    #Populate friendsOnline list
    for x in data_dict:
        if x['name'] in session["friends"]:
            friendsOnline.append(x)

    return render_template("friends.html",data=friendsOnline, friendsList = session["friends"])

#clear friends list
@app.route("/clearfriends")
def clearFriends():
    if "friends" in session:
        session.pop("friends")
    return redirect("/friends")





#Run app
## Needs to be at bottom of python file so all routes are loaded first. Otherwise, 404.
if __name__ == "__main__":
    app.run(host="0.0.0.0")