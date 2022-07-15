import cv2 
import numpy as np 
import mediapipe as mp 
from keras.models import load_model
import os
import random
import subprocess
import time
import sys
now = time.time()
future = now + 20
parent_directory=os.path.join(sys.path[0],"Songs")   #'C:/Users/OM/Downloads/13_07_2022 EBMP/EBMP/Songs/'

model  = load_model("model.h5")
label = np.load("labels.npy")



holistic = mp.solutions.holistic
hands = mp.solutions.hands
holis = holistic.Holistic()
drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
def emotion(calls):
        
        randomfile=[]
        file=[]
        called_folder=os.path.join(parent_directory,calls)
        num_of_file= os.listdir(called_folder)


        if len(num_of_file)==0:
                calls="Default"
                print('''No songs has been Assigned to that emotion
                        ***PLAYING DEFAULT PLAYLIST***''')
                called_folder=os.path.join(parent_directory,calls)


        for song in os.listdir(called_folder):
                if song[-3:]=='mp3':
                        randomfile.append(song)
        random.shuffle(randomfile)
        for song in randomfile:
                #print('You are '+calls+' :) ,I playing special song for you: ' + song)
                file.append(os.path.join(called_folder,song))
                #random.shuffle(file)
        return file


while True:
        lst = []   
        _,frm = cap.read()
        frm = cv2.flip(frm, 1)
        res = holis.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))
        if res.face_landmarks:
                for i in res.face_landmarks.landmark:
                        lst.append(i.x - res.face_landmarks.landmark[1].x)
                        lst.append(i.y - res.face_landmarks.landmark[1].y)

                if res.left_hand_landmarks:
                        for i in res.left_hand_landmarks.landmark:
                                lst.append(i.x - res.left_hand_landmarks.landmark[8].x)
                                lst.append(i.y - res.left_hand_landmarks.landmark[8].y)
                else:
                        for i in range(42):
                                lst.append(0.0)

                if res.right_hand_landmarks:
                        for i in res.right_hand_landmarks.landmark:
                                lst.append(i.x - res.right_hand_landmarks.landmark[8].x)
                                lst.append(i.y - res.right_hand_landmarks.landmark[8].y)
                else:
                        for i in range(42):
                                lst.append(0.0)

                lst = np.array(lst).reshape(1,-1)

                pred = label[np.argmax(model.predict(lst))]
                
                print(pred)
                cv2.putText(frm, pred, (50,50),cv2.FONT_ITALIC, 1, (255,0,0),2)
                tex=pred

		
        #drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
        #drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
        #drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)
        cv2.imshow("window", frm)
        if time.time() > future:
                cv2.destroyAllWindows()
                mp = "C:/Program Files (x86)/Windows Media Player/wmplayer.exe"
                file=emotion(tex)
                
                subprocess.call([mp,*file])
                break
        if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                cap.release()
                break
