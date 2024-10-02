import mediapipe as mp 
import numpy as np 
import cv2 
import tkinter
import os
import sys

def data_collection(name):
	try:

		cap = cv2.VideoCapture(0)
		name = name
		print(name)
		print(type(name))

		#Creating Folder
		
		parent_dir=os.path.join(sys.path[0],"Songs")
		path=os.path.join(parent_dir,name)
		path_default=os.path.join(parent_dir,'Default')

		try:
			os.makedirs(path,exist_ok=True)
			os.makedirs(path_default,exist_ok=True)
			print("folder just created")
		except OSError as error:
			print("folder already created")



		# name = input("Enter the name of the data : ")
		# print(name)
		# print(type(name))
		holistic = mp.solutions.holistic
		hands = mp.solutions.hands
		holis = holistic.Holistic()
		drawing = mp.solutions.drawing_utils

		X = []
		data_size = 0

		while True:
			lst = []

			_, frm = cap.read()

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

				X.append(lst)
				data_size = data_size + 1

			drawing.draw_landmarks(frm, res.face_landmarks, holistic.FACEMESH_CONTOURS)
			drawing.draw_landmarks(frm, res.left_hand_landmarks, hands.HAND_CONNECTIONS)
			drawing.draw_landmarks(frm, res.right_hand_landmarks, hands.HAND_CONNECTIONS)

			cv2.putText(frm, str(data_size), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

			cv2.imshow("window", frm)

			if cv2.waitKey(1) == 27 or data_size > 99:
				cv2.destroyAllWindows()
				cap.release()
				break

		np.save(f"{name}.npy", np.array(X))
		print(np.array(X).shape)

	except Exception as e:
			print(f"Error occured at data collection :  {e}")
