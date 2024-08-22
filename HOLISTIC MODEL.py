import cv2
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_holistic=mp.solutions.holistic


####  initialize hikistic model with tracking and detecting accuracy
with mp_holistic.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    vid=cv2.VideoCapture(0)

    while vid.isOpened():
        ret,frame=vid.read()

        
        #image convert into  rgb bcz holistic model need img in the form of  rgb formet
        image=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        results=holistic.process(image)
        #print(results.face_landmarks)
        

        #image convert back to  bgr format bcz opencv fetch that img into bgr format


        image=cv2.cvtColor(image,cv2.COLOR_RGB2BGR)


        #draw  right hand
        mp_drawing.draw_landmarks(image,results.right_hand_landmarks,mp_holistic.HAND_CONNECTIONS,
                                  mp_drawing.DrawingSpec((0,0,255),2,2)
                                  ,mp_drawing.DrawingSpec((255,255,0),2,2)
                                  
                                  )
        # draw left hand
        mp_drawing.draw_landmarks(image,results.left_hand_landmarks,mp_holistic.HAND_CONNECTIONS)
        #draw head
        mp_drawing.draw_landmarks(image,results.face_landmarks,mp_holistic.FACEMESH_CONTOURS,
                                  mp_drawing.DrawingSpec((0,0,255),1,1)
                                  ,mp_drawing.DrawingSpec((255,255,0),2,2))

        #pose
        mp_drawing.draw_landmarks(image,results.pose_landmarks,mp_holistic.POSE_CONNECTIONS)

        
        im=cv2.resize(image,(1000,900))
        cv2.imshow('frame',im)
        
        if cv2.waitKey(10) & 0xFF==ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()
    
