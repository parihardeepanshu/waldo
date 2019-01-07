import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_Dcascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#this is the cascade we just made. Call what you want
waldo_cascade = cv2.CascadeClassifier('cascade.xml')
print(waldo_cascade)
img = cv2.imread('download.png')
cv2.namedWindow("chal jaa re", cv2.WINDOW_NORMAL)
print(3)
#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('gray',gray)
#cv2.waitKey(0)
waldo = waldo_cascade.detectMultiScale(img,scaleFactor=1.1, minNeighbors=3,minSize=(20,20),maxSize=(40,40))
#print(waldo)
for (i,(x,y,w,h)) in enumerate(waldo):
  # print(inloop)
   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imshow('chal jaa re',img)
cv2.waitKey(0)
#cv2.destroyAllWindows()
