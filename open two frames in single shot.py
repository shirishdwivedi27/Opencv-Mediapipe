import cv2
import numpy as np
vid=cv2.VideoCapture(0)
#cid=cv2.VideoCapture(0)
while(True):
    ret,frame=vid.read()
    #ret,frame1=cid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)

    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
#cid.release()
cv2.destroyAllWindows()
