from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import json

#Setting lists and dicts to work on
online = []
character = {}
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


#html_doc = driver.get("https://www.tibia.com/community/?subtopic=worlds&world=Collabra&order=vocation_asc")
html_doc = driver.get("https://www.tibia.com/community/?subtopic=worlds")

#Selenium getting page source code for Beautiful Soup
page_source = driver.page_source

#sleep(5)

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
        worlds['url'] = x['href']
        worldsList.append(worlds.copy())

print(worldsList)



#Navigating to first URL to scrape
html_doc = driver.get(firstUrl)
page_source = driver.page_source
soup.reset()
soup = BeautifulSoup(page_source, 'html.parser')

#Get data from page source
dataCharacters = soup.find_all('td')


#Generating data for characters
for x in dataCharacters:

    try:
        link = x.find('a')
        href = link.get('href')
        name = link.string

        correct = 'https://www.tibia.com/community/?subtopic=characters&'
        
        if href != None and correct in href and name != None:
            character['name'] = name.replace(old,new)
            character['href'] = href.replace(old,new)

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


    if len(character) == 4:
        online.append(character.copy())
        character.clear()

#print(dataWorlds)

#Dict Data to Json
jsonString = json.dumps(online)
jsonFile = open("data/data.json","w")
jsonFile.write(jsonString)

jsonShow = driver.get("file:///E:/Python%20Projects/2%20-%20Tibia%20toolset/data/data.json")
driver.quit()
#print("*************HASTA aca ES CULPA DE GETCHARACTERS*****************")