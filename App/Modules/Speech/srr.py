import speech_recognition as sr
import pyaudio

def speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Speak up : ')
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-IN")
            print(text)
            return text
        except sr.UnknownValueError:
            print('Sorry could not recognize your voice')

        except sr.RequestError as e:
            print("request error")
#    text = input('Speak up:')
#    try:
#        ptext(text)
#    except:
#        print("please try again")
