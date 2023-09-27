# Exiva Friend
#### Video Demo: https://youtu.be/ut_F95Q4bBM
#### Description:
This is a tool for the game called Tibia (https://www.tibia.com/). Tibia is a MMORPG written in C++ that has been online for more than 25 years.

I've been playing this game lately and found that I was having trouble to get people to play with. So I came up with this idea.
**Exiva Friend** ("exiva" is an ingame spell to find a player by his name) is a tool that helps the user to find every player that is currently ingame, providing level, vocation and world.

**Exiva Friend** has three main functionalities:

- Find Online Players: It provides the user with all the players that are online at the current moment.
- Find Party Leads: The user inputs his character level and preferences, and Exiva Friend will show the characters that are online and able to party with (level difference requirements).
- Friends List: The user can add a character's name as a friend to his Friends List to check if that player is online at the moment.

<sub>More features are coming...</sub>


### How does it work?
Two scraping scripts are managed through a scheduler to be running as intended.

- schedule.py: schedule the scrapers according to EU/Amsterdam timezone.

- getWorlds.py: The first script gets the data of which worlds are online. It is scheduled 10 minutes after server save (when Tibia servers shut down to back up data). It runs every day so if a new server is created or two old servers get merged, the app will be updated. 

- getCharacters.py: Ths second script is in charge of scanning through each character of each world and retrieving their data (name, level, vocation, Tibia's URL and world). I did a lot of testing to avoid Tibia's 503 response (because of multiple requests). It runs every 300 seconds interval and it has half a second sleep between each server request.

- myTimer.py: It prints current starting time, ending time and elapsing time of a Python program. You can use it inside a function or to test a file / app. I've built it so I could improve my app's runtime.

- validateCharacter.py: Validates user inputs when trying to add a friend to "Friends List". The main function is to not let the user add a character that does not exist to his own friend list.

- app.py: Main server file. It supports the routes for each functionality. 
"/" for Find Online Players.
"/partyleads" for Find Party Leads.
"/friends" for Friends List.
"/clearfriends" to reset session variable.
"/deletefriend" to delete specific friend.

- requirements.txt: Keeps track of modules the app uses.

- CHANGELOG.md: Keeps track of changes.

- data.json: Stores the characters information that is scraped through getCharacters.py.

- worlds.json: Store the worlds information that is scraped through getWorlds.py.

- existingCharacter.json: Stores the names of validated characters that are added to Friends List so, if added again, the app doesn't have to scrape that data again.
<sub>Working on schedule a task each 20 days to validate all characters in this json, as characters can get deleted.</sub>


### Modules used:
- flask
- json
- math
- datetime
- time
- os
- inspect
- bs4
- selenium
- atexit
- apscheduler


### Attention:

Each user input is validated (server-side) as needed.
No SQL was used, because I wanted to learn more about json files and how to use lists within them.
This web application is deployed in an old laptop at the moment and is running okay inside my local network.
Once I've developed more features to it I'll put it online for monetization purposes.
The focus of the project is server-side (back-end). Front end is simple, because It will be refactored with React components once I get confortable with them.