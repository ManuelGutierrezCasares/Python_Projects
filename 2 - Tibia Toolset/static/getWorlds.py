from static import myTimer
from bs4 import BeautifulSoup
from selenium import webdriver
import json

#Use a function so the module doesn't run on import
def getWorlds():
    
    #Start myTimer
    startTimer = myTimer.startTimer()

    #Setting lists and dicts to work on
    worlds = {}
    worldsList = []

    #Initializing Selenium
    options = webdriver.ChromeOptions()
    options.page_load_strategy = 'normal'
    options.add_argument("--headless")
    driver = webdriver.Chrome(options = options)


    html_doc = driver.get("https://www.tibia.com/community/?subtopic=worlds")

    #Selenium getting page source code for Beautiful Soup
    page_source = driver.page_source

    #Initializing BS
    soup = BeautifulSoup(page_source, 'html.parser')

    #Getting first link to scrape - Antica
    firstUrl = soup.find('td').find('a')
    firstUrl = firstUrl['href'] + '&order=vocation_asc'

    #Getting worlds
    dataWorlds = soup.find('td').findAll('a',href=True)
    #Iterate over worlds list, check if link is world and append to worldsList
    for x in dataWorlds:
        if '?subtopic=worlds' in x['href']:
            worlds['worldName'] = x.string
            worlds['url'] = x['href'] + '&order=vocation_asc'
            worldsList.append(worlds.copy())

    #World data to json
    jsonString = json.dumps(worldsList)
    with open("data/worlds.json","w") as jsonFile:
        jsonFile.write(jsonString)

    #Clear Selenium and BS4
    driver.quit()
    soup.clear()

    #End myTimer
    myTimer.endTimer(startTimer)
    