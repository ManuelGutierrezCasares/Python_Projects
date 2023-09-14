from flask import Flask, render_template, request, session
import json
import math
import static.schedule


"""
v0.0    Initialize project and create Selenium + Beautiful Soup scraper inside app.py file. Only working for Collabra world
v0.1    Move Selenium + BS to getCharacters.py file
v0.2    Add /partyleads and /friends routes
v0.3    Add feature to /partyleads where you can select vocation and lvl to get possible party members
v0.4    Add schedule.py and scheduler to getCharacters.py so you don't have to run that file on every call to any route
v0.5    Factorize getCharacters so it get all character from all worlds, not just Collabra
v0.6    Done on scheduler and error 403 on multiple requests
v0.7    Added support to run locally
v0.8    Refactorizing to getWorlds.py and getCharacters.py, instead of all in one python script; and refactorizing schedule to only run getWorlds when necessary; and added world support to partyleads route
"""

app = Flask(__name__)

app.secret_key = 'THIS_IS_THE_KEY'


#friends = []

@app.route("/")
def index():
    data = open("data/data.json","r")
    data_dict = json.load(data)
    players = len(data_dict)

    return render_template("index.html", data = data_dict, players = players)

@app.route("/partyleads", methods=["GET", "POST"])
def party():
    
    if request.method == "POST":

        userLvl = request.form.get("user")
        try:
            userLvl = int(userLvl)
        except:
            pass
        maxLvl = math.floor(userLvl * 3/2)
        minLvl = math.ceil(userLvl * 2/3)

        userElection = request.form.get('voc')

        userWorld = request.form.get('world')

        party = []
        data = open("data/data.json","r")
        data_dict = json.load(data)
        worlds = open("data/worlds.json","r")
        worlds_dict=json.load(worlds)

        for x in data_dict:
            if (int(x['level']) >= minLvl and int(x['level']) <= maxLvl) and userWorld == x['world']:
                if userElection == "All":
                    party.append(x)
                elif x['vocation'] == userElection:
                    party.append(x)
                

        return render_template("partyleads.html",data=party,selectedLevel=userLvl,selectedVoc=userElection, selectedWorld = userWorld, worlds = worlds_dict)
    
    else:
        worlds = open("data/worlds.json","r")
        worlds_dict=json.load(worlds)

        return render_template("partyleads.html", worlds = worlds_dict)

@app.route("/friends", methods=['GET','POST'])
def friend():
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

if __name__ == "__main__":
    app.run(host="0.0.0.0")