import cv2
import time
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic

with mp_holistic.Holistic(min_tracking_confidence=0.5,min_detection_confidence=0.5) as holistic:
    vid=cv2.VideoCapture(0)

    while True:
        ret, frame=vid.read()

        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

        results=holistic.process(image)

        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        #draw head

        mp_drawing.draw_landmarks(image,results.face_landmarks,mp_holistic.FACEMESH_CONTOURS
                                  ,mp_drawing.DrawingSpec((255,0,0),1,1)
                                  ,mp_drawing.DrawingSpec((0,255,0),2,2))







        cv2.imshow('frame',image)

        if cv2.waitKey(1)==ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
