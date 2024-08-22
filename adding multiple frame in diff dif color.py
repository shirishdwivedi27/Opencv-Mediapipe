import cv2
import numpy as np
vid=cv2.VideoCapture(0)

while(True):
    ret,frame=vid.read()

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gr=cv2.cvtColor(frame,cv2.COLOR_BGR2LAB)   ####BGR2HSV
    

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('gray',gr)

    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
