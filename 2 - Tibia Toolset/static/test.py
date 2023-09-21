import myTimer
import json

def testJsonTimes(name):
    #Start myTimer
    startTimer = myTimer.startTimer()


    #World data to json
    #jsonString = json.dumps(worldsList)
    with open("data/worlds.json","r") as jsonFile:
        result = None
        data = json.load(jsonFile)
        #jsonFile.write(jsonString)
        for x in data:
            if x['worldName'] == name:
                result = True

    #End myTimer
    myTimer.endTimer(startTimer)

    return True if (result) else False


print(testJsonTimes('Antica'))