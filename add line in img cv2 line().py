import cv2
q=cv2.imread('w.jpg')
r=cv2.resize(q,(800,800))
sp=(800,0)
ep=(0,800)
color=(0,255,0)
thickness=9
im=cv2.line(r,sp,ep,color,thickness)
cv2.imshow('im',im)
