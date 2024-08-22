import cv2
vid=cv2.VideoCapture(0)
i=0
while(True):
    ret,frame=vid.read()

    font=cv2.FONT_HERSHEY_SIMPLEX
    x=str(i)
    cv2.putText(frame,x,(200,200),font,1,(0,255,255),2,cv2.LINE_4)
    i+=1
    if i==100:
        ret,img=vid.read()
        cv2.imshow('image',img)
        cv2.waitKey(2000)
        cv2.imwrite('camera.jpg',img)
        
    ims=cv2.resize(frame,(1200,1000))

    cv2.imshow('frame',ims)

    if cv2.waitKey(1)==ord('r'):
        break
vid.release()
cv2.destroyAllWindows()

    
