import cv2
import numpy as np
import sqlite3
import os
from ..Speech.srr import speech
from ..Speak.speakerr import spout

def fdata():
    spout('May I have your name please?')
    uname = speech()
    if uname != None:
        gather(uname)
    else:
        fdata()
def gather(uname):
    conn = sqlite3.connect('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/database.db')
    if not os.path.exists('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/dataset'):
        os.makedirs('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/dataset')

    c = conn.cursor()

    face_cascade = cv2.CascadeClassifier('C:/Users/Yash Tandon/Desktop/python course/haar-cascade-files-master/haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)

    c.execute('INSERT INTO users (name) VALUES (?)', (uname,))

    uid = c.lastrowid

    sampleNum = 0

    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 1)
        for (x,y,w,h) in faces:
            sampleNum = sampleNum+1
            cv2.imwrite("C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/dataset/User."+str(uid)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
            cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
            cv2.waitKey(100)
            #cv2.imshow('img',img)
        cv2.waitKey(1);
        if sampleNum > 20:
            break
    cap.release()

    conn.commit()

    conn.close()
    cv2.destroyAllWindows()
