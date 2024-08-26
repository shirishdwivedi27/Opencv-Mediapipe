import cv2
import mediapipe as  mp

import time
pt=0
ct=0

r=0
mp_draw=mp.solutions.drawing_utils
mp_hands=mp.solutions.hands
hands=mp_hands.Hands()

with mp_hands.Hands(min_tracking_confidence=0.5,min_detection_confidence=0.5) as hands:
    
    vid=cv2.VideoCapture(0)
    #f_l=[vid]
    while True:
        ret,frame=vid.read()

        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        results=hands.process(image)

        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for num,hand in enumerate(results.multi_hand_landmarks):
                for i,lm in enumerate(hands.landmark):
                    h,w,c=image.shape
                    cx,cy=int(lm.x*w),int(lm.y*h)
                    if id==4:
                        cv2.circle(image,(cx,cy),15,(255,0,255),cv2.FILLED)
                mp_draw.draw_landmarks(image,hand,mp_hands.HAND_CONNECTIONS)
               

                        
                

        ct=time.time()
        fps=1/(ct-pt)
        pt=ct

        cv2.putText(r,str(int(fps)),(10,70),cv2.FONT_HERSHEY_SIMPLEX,2,(255,0,255),2)
        
        
         #for id,file in enumerate(f_l):
             
             
                
        cv2.imshow('image',image)
        if cv2.waitKey(1)==ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

