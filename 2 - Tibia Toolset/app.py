from flask import Flask, render_template, request, session
import json
import math
#import static.schedule
from static.getCharacters import worldsList


"""
v0.0    Initialize project and create Selenium + Beautiful Soup scraper inside app.py file. Only working for Collabra world
v0.1    Move Selenium + BS to getCharacters.py file
v0.2    Add /partyleads and /friends routes
v0.3    Add feature to /partyleads where you can select vocation and lvl to get possible party members
v0.4    Add schedule.py and scheduler to getCharacters.py so you don't have to run that file on every call to any route
v0.5    Factorize getCharacters so it get all character from all worlds, not just Collabra
v0.6    Done on scheduler and error 403 on multiple requests
v0.7    
"""

app = Flask(__name__)

app.secret_key = 'THIS_IS_THE_KEY'


#friends = []

@app.route("/")
def index():
    #importlib.reload(getCharacters)
    print(worldsList)
    data = open("data/data.json","r")
    data_dict = json.load(data)
    players = len(data_dict)

    return render_template("index.html", data = data_dict, players = players)

@app.route("/partyleads", methods=["GET", "POST"])
def partyed():
    
    if request.method == "POST":
        #importlib.reload(getCharacters)

        userLvl = request.form.get("user")
        try:
            userLvl = int(userLvl)
        except:
            pass
        maxLvl = math.floor(userLvl * 3/2)
        minLvl = math.ceil(userLvl * 2/3)

        userElection = request.form.get('voc')


        party = []
        data = open("data/data.json","r")
        data_dict = json.load(data)

        for x in data_dict:
            if (int(x['level']) >= minLvl and int(x['level']) <= maxLvl):
                if userElection == "All":
                    party.append(x)
                elif x['vocation'] == userElection:
                    party.append(x)
                

        return render_template("partyleads.html",data=party,selectedLevel=userLvl,selectedVoc=userElection)
    
    else:
        return render_template("partyleads.html")

@app.route("/friends", methods=['GET','POST'])
def friend():
    #importlib.reload(getCharacters)
    # if request.method == 'POST':
    #     friends.append(request.form.get('friendName'))
    friends = ['Best Kina', 'Laniakeas', 'Sorczin Hur', 'Aldorusz', 'Vedras', 'Korur']    
    print(friends)
    friendsOnline = []
    data = open("data/data.json","r")
    data_dict = json.load(data)

    for x in data_dict:
        if x['name'] in friends:
            friendsOnline.append(x)

    return render_template("friends.html",data=friendsOnline)


