import speech_recognition as sr
import pyaudio
from ..Speak.speaker import *

def process():
    while 1:
        speech()

def ptext(text):
    li = text.split()
    for word in li:
        if word == 'home':
            hpage()

        elif word == 'news':
            newslist()

        elif word == 'weather':
            wpage(text)

        elif word == 'Wiki':
            wikipage(text)

        elif word == 'cricket' or word == 'soccer' or word == 'basketball' or word == 'tennis':
            spage(text)


def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak up : ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-IN")
            print(text)
            ptext(text)
        except sr.UnknownValueError:
            print('Sorry could not recognize your voice')

        except sr.RequestError as e:
            print("request error")
#    text = input('Speak up:')
#    ptext(text)
