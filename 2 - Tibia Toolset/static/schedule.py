from static.getCharacters import getCharacters
from static.getWorlds import getWorlds
import atexit
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

#Run for the first time the scrapper on Worlds and Characters
getWorlds()
getCharacters()

#Print time now to know when the scheduler is running. Time is LOCAL
currentTime = datetime.datetime.now()
print("Starting scheduler at: " + str(currentTime))

#Set up scheduler CET/CEST time to be compatible with Tibia Timezone
scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Amsterdam'})

#Schedule to run Scrappers. Worlds after Tibia Server Save (in case any new World gets created) and Characters each 300 seconds 
scheduler.add_job(func=getWorlds, trigger="cron", hour=10, minute=10)
scheduler.add_job(func=getCharacters, trigger="interval", seconds=300, coalesce=True)

#Run schedule
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())