import  cv2
vid=cv2.VideoCapture(0)
while(True):
    ret,frame=vid.read()

    im=cv2.resize(frame,(700,800))
    cv2.imshow('frrram',im)

    if cv2.waitKey(1)==ord('q'):
        break
vid.release()
cv2.destroyAllWindows()
