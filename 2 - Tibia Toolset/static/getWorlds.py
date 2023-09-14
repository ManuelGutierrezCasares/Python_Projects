from time import sleep, time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import json

def getWorlds():
    start_time = time()
    print("Start time of get worlds: " + str(datetime.now()))

    #Setting lists and dicts to work on
    worlds = {}
    worldsList = []

    #Replace variables for characters
    old = "\xa0"
    new = " "

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

    #print(worldsList)

    #World data to txt
    jsonString = json.dumps(worldsList)
    jsonFile = open("data/worlds.json","w")
    jsonFile.write(jsonString)

    driver.quit()
    soup.clear()

    end_time = time()
    print("End time of get worlds: " + str(datetime.now()))
    elapsed_time = end_time - start_time
    print("Elapsed time in get worlds: ", elapsed_time) 
#print("*************HASTA aca ES CULPA DE GETCHARACTERS*****************")