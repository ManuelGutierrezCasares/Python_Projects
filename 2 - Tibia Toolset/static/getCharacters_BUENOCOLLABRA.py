from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
import json

#print("*************desde aca ES CULPA DE GETCHARACTERS*****************")
options = webdriver.ChromeOptions()
options.page_load_strategy = 'normal'
options.add_argument("--headless")
driver = webdriver.Chrome(options = options)


html_doc = driver.get("https://www.tibia.com/community/?subtopic=worlds&world=Collabra&order=vocation_asc")

#selenium
page_source = driver.page_source

#sleep(5)

#beautiful soup
soup = BeautifulSoup(page_source, 'html.parser')

online = []
character = {}
worldsList = []

dataCharacters = soup.find_all('td')
dataWorlds = soup.find_all('option')
for x in dataWorlds:
    worldsList.append(x.string)
    
for x in worldsList:
    print("https://www.tibia.com/community/?subtopic=worlds&world=" + x + "&order=vocation_asc")
old = "\xa0"
new = " "


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


jsonString = json.dumps(online)
jsonFile = open("data/data.json","w")
jsonFile.write(jsonString)

jsonShow = driver.get("file:///E:/Python%20Projects/2%20-%20Tibia%20toolset/data/data.json")
driver.quit()
#print("*************HASTA aca ES CULPA DE GETCHARACTERS*****************")