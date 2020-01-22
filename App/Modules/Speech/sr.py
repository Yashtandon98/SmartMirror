import speech_recognition as sr
import pyaudio
from ..Speak.speaker import *

def process():
    while 1:
        speech()

def ptext(text):
    if 'home' in text:
        hpage()

    if 'news' in text:
        newslist()


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
