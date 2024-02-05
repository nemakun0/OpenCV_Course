import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier("c:/Users/emine/Desktop/OpenCv/faces/haar_face.xml")

people = ["Ben Afflek", "Elton John", "Jerry Seinfield", "Madonna", "Mindy Kaling"]

features = np.load("C:/Users/emine/Desktop/OpenCv/faces/features.npy", allow_pickle=True)
labels = np.load("C:/Users/emine/Desktop/OpenCv/faces/labels.npy", allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

face_recognizer.read("C:/Users/emine/Desktop/OpenCv/faces/face_train.yml"),

img = cv.imread(r"C:\Users\emine\Desktop\OpenCv\faces\faces_train\val\elton_john\1.jpg")

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("person", gray)

#  Detect the face in the image

faces_rect = haar_cascade.detectMultiScale(gray, 1.1,4)
for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label, confidence = face_recognizer.predict(faces_roi)
    print(f"label = {people[label]} with a confidence of {confidence} ")

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), thickness=2)
    cv.rectangle (img, (x,y), (x+w,y+h),(0,255,0), thickness=2)

cv.imshow("detected face", img)

cv.waitKey(0)