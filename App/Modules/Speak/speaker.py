import pyttsx3
from ..News.news import getnews
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..Sports.spdata import *
from ..Weather.weather import query_api
from ..Wikipedia.wiki import getwiki

chromeOptions = Options()
#chromeOptions.add_argument("--kiosk")
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('http://127.0.0.1:5000/')

sdata = None
wikidata = None
wedata = None

def spout(spdata):
    mirror = pyttsx3.init()
    rate = mirror.setProperty('rate', 150)
    mirror.say(spdata)
    mirror.runAndWait()

def newslist():
    ndata = getnews()
    driver.get('http://127.0.0.1:5000/news')
    for news in ndata:
        spout(news)

def hpage():
    driver.get('http://127.0.0.1:5000/')

def wpage(text):
    #loop to check city in text and then pass it too the function
    global wedata
    list = text.split()
    with open('C:/Users/Yash Tandon/Desktop/python course/basic projects/indiancities.txt','r') as f, open('cities.txt','w') as fo:
        for line in f:
            fo.write(line.replace('"', ' ').replace("'", " "))
    file = open('cities.txt')
    for cities in file:
        cities = cities.strip().split()
        for word in list:
            if word in cities:
                wedata = query_api(word)
    driver.get('http://127.0.0.1:5000/weather')

def spage(text):
    global sdata
    if 'cricket' in text:
        sdata = cmatches()
    elif 'basketball' in text:
        sdata = bkmatch()
    elif 'tennis' in text:
        sdata = tmatch()
    elif 'hockey' in text:
        sdata = hmatch()
    elif 'soccer' in text:
        sdata = smatch()
    print(sdata)
    driver.get('http://127.0.0.1:5000/sports')

def wikipage(text):
    global wikidata
    print("In Wiki")
    select = text[5:]
    wikidata = getwiki(select)
    print(wikidata)
    driver.get('http://127.0.0.1:5000/wiki')
