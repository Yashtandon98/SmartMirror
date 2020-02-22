import cv2
import numpy as np
import sqlite3
import os
from App.Modules.Speak.speakerr import spout
from App.Modules.facerecog.data_gatering import fdata
from App.Modules.facerecog.trainer import train

def recog():
    print('hello')
    conn = sqlite3.connect('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/database.db')
    c = conn.cursor()
    fname = "C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/recognizer/trainingData.yml"
    if not os.path.isfile(fname):
        print("Please train the data first")
        fdata()
        train()
    face_cascade = cv2.CascadeClassifier('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(fname)

    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
        ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
        c.execute("select name from users where id = (?);", (ids,))
        result = c.fetchall()
        name = result[0][0]
        if conf < 50:
            print(name)
            return name
        else:
            break
    #cv2.imshow('Face Recognizer',img)
    cap.release()
    cv2.destroyAllWindows()
