from static import myTimer
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import json



def getCharacters():
    #Start myTimer
    startTimer = myTimer.startTimer()

    #Initialize lists and dicts to work on
    online = []
    character = {}

    #Replace variables for characters
    old = "\xa0"
    new = " "

    #Start Selenium
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)

    #Get worlds from json file
    with open("data/worlds.json","r") as data:
        worldsList = json.load(data)

    #Iterate over worlds.json
    for w in worldsList:

        #Navigate to first URL to scrape
        html_doc = driver.get(w['url'])
        sleep(0.5)
        page_source = driver.page_source
        soup = BeautifulSoup(page_source, 'html.parser')

        #Get data from page source
        dataCharacters = soup.find_all('td')

        #Generate data for characters
        for x in dataCharacters:

            try:
                link = x.find('a')
                href = link.get('href')
                name = link.string

                correct = 'https://www.tibia.com/community/?subtopic=characters&'
                
                if href != None and correct in href and name != None:
                    character['name'] = name.replace(old,new)
                    character['href'] = href.replace(old,new)
                    character['name'] = character['name'].title()

            except:
                pass

            try:
                selector = x.get('style')
                voc = 'width:20%;'
                lvl = 'width:10%;'

                if selector == voc:
                    character['vocation'] = x.string.replace(old,new)
                elif selector == lvl:
                    character['level'] = x.string.replace(old,new)

            except:
                pass
            
            character['world'] = w['worldName']

            if len(character) == 5:
                online.append(character.copy())
                character.clear()


    #Dict Data to Json
    jsonString = json.dumps(online)
    with open("data/data.json","w") as jsonFile:
        jsonFile.write(jsonString)

    #Clear Selenium and BS4
    driver.quit()
    soup.clear()

    #End myTimer
    myTimer.endTimer(startTimer)
