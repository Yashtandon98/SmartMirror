import os
import cv2
import numpy as np
from PIL import Image

def train():
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    path = 'C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/dataset'
    if not os.path.exists('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/recognizer'):
        os.makedirs('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/recognizer')

    def getImagesWithID(path):
        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faces = []
        IDs = []
        for imagePath in imagePaths:
            faceImg = Image.open(imagePath).convert('L')
            faceNp = np.array(faceImg,'uint8')
            ID = int(os.path.split(imagePath)[-1].split('.')[1])
            faces.append(faceNp)
            IDs.append(ID)
            #cv2.imshow("training",faceNp)
            cv2.waitKey(10)
        return np.array(IDs), faces

    Ids, faces = getImagesWithID(path)
    recognizer.train(faces,Ids)
    recognizer.save('C:/Users/Yash Tandon/Desktop/python course/SmartMirror/SmartMirror/App/Modules/facerecog/recognizer/trainingData.yml')
    cv2.destroyAllWindows()
