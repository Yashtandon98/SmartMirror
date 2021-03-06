import speech_recognition as sr
import pyaudio
from ..Speak.speaker import *
import sys
import time
import os

def process():
    while 1:
        speech()

def ptext(text):
    global result
    li = text.split()
    for word in li:
        if word == 'login':
            log()

        elif word == 'signup':
            sign()

        elif word == 'home':
            hpage()

        elif word == 'news':
            newslist(text)

        elif word == 'weather':
            wpage(text)

        elif word == 'Wiki':
            wikipage(text)

        elif word == 'cricket' or word == 'soccer' or word == 'basketball' or word == 'tennis':
            spage(text)

        elif word == 'quit' or word == 'exit' or word == 'logout':
            exi()


def speech():
    while True:
        r = sr.Recognizer()
        fname = "C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/recognizer/trainingData.yml"
        with sr.Microphone() as source:
            print('Speak up : ')
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language="en-IN")
                print(text)
                ptext(text)
                if not os.path.isfile(fname) and (text == 'login' or text == 'signup') :
                    time.sleep(20)
            except sr.UnknownValueError:
                print('Sorry could not recognize your voice')

            except sr.RequestError as e:
                print("request error")
#    text = input('Speak up:')
#    try:
#        ptext(text)
#    except:
#        print("please try again")
