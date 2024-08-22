import cv2
import mediapipe as mp


mp_drawing=mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic

with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    vid=cv2.VideoCapture(0)
    while vid.isOpened():
        ret,frame=vid.read()

        im=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        results=holistic.process(im)

        im=cv2.cvtColor(im,cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(im,results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS
                                     ,mp_drawing.DrawingSpec((0,255,0),2,2)
                                     ,mp_drawing.DrawingSpec((255,255,0),3,3))
        
                                     





        cv2.imshow('frame',im)

        if cv2.waitKey(10)==ord('q'):
                                     break
    vid.release()
    cv2.destroyAllWindows()

        
