import cv2
cv2.namedWindow('output',cv2.WINDOW_NORMAL)
img=cv2.imread('w.jpg',cv2.IMREAD_COLOR)
#cv2.resize('w.jpg',(100,100),100,100,cv2.INTER_LINEAR)
ims=cv2.resize(img,(1260,480))
cv2.imshow('Image',ims)
cv2.waitKey(0)
cv2.destroyAllWindows()
