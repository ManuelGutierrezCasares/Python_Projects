from time import sleep, time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import json



def getCharacters():
    #Calculate time spent in function
    start_time = time()
    print("Start time of get character: " + str(datetime.now()))

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
    data = open("data/worlds.json","r")
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
    jsonFile = open("data/data.json","w")
    jsonFile.write(jsonString)

    #Clear Selenium and BS4
    driver.quit()
    soup.clear()

    #Calculate time spent on function
    end_time = time()
    print("End time of get character: " + str(datetime.now()))
    elapsed_time = end_time - start_time
    print("Elapsed time of get character: ", elapsed_time) 
