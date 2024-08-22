import cv2
import numpy as np

#vid=cv2.VideoCapture('w.jpg')
q=cv2.imread('w.jpg')
cv2.waitKey(2000)
w=cv2.resize(q,(1240,1000))
gray=cv2.cvtColor(w,cv2.COLOR_BGR2LAB)
cv2.imshow('image',w)
cv2.imshow('image',gray)

