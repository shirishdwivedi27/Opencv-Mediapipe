import cv2
n=input("ENTER")

vid=cv2.VideoCapture(0)
while(True):
    ret , frame=vid.read()

    font=cv2.FONT_HERSHEY_SIMPLEX
    
    cv2.putText(frame,n,(50,50),font,1,(0,255,255),2,cv2.LINE_4)

    cv2.imshow('video',frame)

    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
