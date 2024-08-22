import cv2
q=cv2.imread('w.jpg')
w=cv2.resize(q,(800,800))
img=cv2.rectangle(w,(100,100),(700,700),(255,0,0),-1)  ##if thickness==-1 thenbox created filled color
cv2.imshow('image',img)
