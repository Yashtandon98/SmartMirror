import cv2
import numpy as np
import sqlite3
import os
import sr

conn = sqlite3.connect('database.db')
c = conn.cursor()
fname = "recognizer/trainingData.yml"
if not os.path.isfile(fname):
  print("Please train the data first")
  exit(0)
face_cascade = cv2.CascadeClassifier('C:/Users/Yash Tandon/Desktop/python course/haar-cascade-files-master/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read(fname)
list=[]
print(list)
while(len(list) != 1):
  ret, img = cap.read()
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray, 1.3, 1)
  for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    ids,conf = recognizer.predict(gray[y:y+h,x:x+w])
    c.execute("select name from users where id = (?);", (ids,))
    result = c.fetchall()
    name = result[0][0]
    if conf < 50:
      cv2.putText(img, name, (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (150,255,0),2)
      list.append(name)
    else:
      cv2.putText(img, 'No Match', (x+2,y+h-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255),2)
  #cv2.imshow('Face Recognizer',img)
  k = cv2.waitKey(30) & 0xff
  if k == ord("q"):
    break
cap.release()
cv2.destroyAllWindows()
print('Hi ' + list[0])
print("How can I help you?")
sr.speech()
