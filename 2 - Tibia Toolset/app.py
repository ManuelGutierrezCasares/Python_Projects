from flask import Flask, render_template, request, session, redirect
import json
import math
from static.validateCharacter import validateCharacter
from datetime import timedelta
#import static.schedule


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


#Delete single friend from list
@app.route("/deletefriend")
def deleteFriend():
    name = request.args.get('name')
    if name in session["friends"]:
        session["friends"].remove(name)
    return redirect("/friends")

#Clear friends list
@app.route("/clearfriends")
def clearFriends():
    if "friends" in session:
        session.pop("friends")
    return redirect("/friends")





#Run app
## Needs to be at bottom of python file so all routes are loaded first. Otherwise, 404.
if __name__ == "__main__":
    app.run(host="0.0.0.0")