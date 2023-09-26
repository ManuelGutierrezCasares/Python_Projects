from static import myTimer
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import json

#Function that returns true if character exist
def validateCharacter(name):

    #Start myTimer
    startTimer = myTimer.startTimer()

    #Avoid bugs
    name = name.strip()

    #Check if character already exist in json
    with open("data/existingCharacters.json","r") as data:
        data_dict = json.load(data)

    for x in data_dict:
        if x['name'] == name:
            #HERE I NEED TO UPDATE TIMESTAMP FOR LAST MODIFIED
            #End myTimer
            myTimer.endTimer(startTimer)
            return True

    #Initializing Selenium
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)


    #Replace space for URL
    old = " "
    new = "+"
    nameForUrl = name.replace(old,new)
    
    html_doc = driver.get(f"https://www.tibia.com/community/?name={nameForUrl}")

    #Selenium getting page source code for Beautiful Soup
    page_source = driver.page_source

    #Initializing BS
    soup = BeautifulSoup(page_source, 'html.parser')


    
    #Getting first link to scrape - Antica
    if soup.find('div', class_='Text').string == "Could not find character":
        characterExist = False
    else:
        #timeru = myTimer.startTimer("EL ELSE")
        characterDict = {}
        with open("data/existingCharacters.json", "r+") as data:
            fileContent = data.read()
            fileList = json.loads(fileContent)
            characterDict['name'] = name
            characterDict['url'] = "https://www.tibia.com/community/?name=" + nameForUrl
            characterDict['lastModified'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            fileList.append(characterDict)
            json_string = json.dumps(fileList)
            data.seek(0)
            data.truncate()
            data.write(json_string)
        characterExist = True
        #myTimer.endTimer(timeru,"EL ELSE")
    


    #Clear Selenium and BS4
    driver.quit()
    soup.clear()

    #End myTimer
    myTimer.endTimer(startTimer)

    return characterExist
