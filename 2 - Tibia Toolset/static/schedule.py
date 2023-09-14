from static.getCharacters import getCharacters
from static.getWorlds import getWorlds
import atexit
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

#print("*************desde aca ES CULPA DE SCHEDULE*****************")
# def reloadData():
#     #print("*************desde aca ES CULPA DE SCHEDULE*****************")
#     importlib.reload(getCharacters)
#     currentTime = datetime.datetime.now()
#     print(currentTime)
#     #print("**************HASTA ACA ES CULPA DE SCHEDULE***************")
getWorlds()
getCharacters()
currentTime = datetime.datetime.now()
print("Starting scheduler at: " + str(currentTime))
scheduler = BackgroundScheduler({'apscheduler.timezone': 'Europe/Amsterdam'})
scheduler.add_job(func=getWorlds, trigger="cron", hour=10, minute=10)
scheduler.add_job(func=getCharacters, trigger="interval", seconds=300, coalesce=True)
scheduler.start()


#print("**************HASTA ACA ES CULPA DE SCHEDULE***************")

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())