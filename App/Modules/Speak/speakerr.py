import pyttsx3

def spout(spdata):
    mirror = pyttsx3.init()
    rate = mirror.setProperty('rate', 150)
    mirror.say(spdata)
    mirror.runAndWait()
