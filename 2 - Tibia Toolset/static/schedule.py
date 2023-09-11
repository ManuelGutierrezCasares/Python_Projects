import static.getCharacters as getCharacters
import importlib
import atexit
import datetime

from apscheduler.schedulers.background import BackgroundScheduler

#print("*************desde aca ES CULPA DE SCHEDULE*****************")
def reloadData():
    #print("*************desde aca ES CULPA DE SCHEDULE*****************")
    importlib.reload(getCharacters)
    currentTime = datetime.datetime.now()
    print(currentTime)
    #print("**************HASTA ACA ES CULPA DE SCHEDULE***************")

scheduler = BackgroundScheduler()
scheduler.add_job(func=reloadData, trigger="interval", seconds=30, coalesce=True)
scheduler.start()


#print("**************HASTA ACA ES CULPA DE SCHEDULE***************")

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())