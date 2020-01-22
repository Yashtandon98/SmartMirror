import pyttsx3
from news import getnews
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chromeOptions = Options()
chromeOptions.add_argument("--kiosk")
chromeOptions.add_experimental_option("excludeSwitches", ['enable-automation'])
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('http://127.0.0.1:5000/')

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
