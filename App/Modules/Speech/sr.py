import speech_recognition as sr
import pyaudio
from modules.weather.weather import query_api
from server import webprint, app
from selenium import webdriver

def process():
    while 1:
        speech()

def ptext(text):
    if 'home' in text:
        chromeOptions = webdriver.ChromeOptions()
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:5000/')
        driver.maximize_window()

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak up : ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            print(text)
            ptext(text)
        except sr.UnknownValueError:
            print('Sorry could not recognize your voice')

        except sr.RequestError as e:
            print("request error")

#while 1:
#    speech()
