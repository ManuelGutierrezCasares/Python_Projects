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
v0.12   Fix get name of caller module for myTimer
v0.13   Add "CHANGELOG.md", "README.md"; change footer in "layout.html"; create styles.css (placeholder for future updates); and typo in "partyleads.html"

v0.14   WORKING IN CHANGE FRONTEND TO REACT? MORE TOOLS? WILL SEE...       ALSO MIGHT WANT TO ADD A JSON FOR CHARACTERS THAT DONT EXIST ATM FOR PERFORMANCE ISSUES
