import numpy as np
import cv2

def face_detection(f):
	g = f.copy()
	gray = cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
	faces = face_cascade.detectMultiScale(gray, 1.1, 5)
	for (x, y, w, h) in faces:
		g = cv2.rectangle(g, (x, y), (x + w, y + h), (0, 255, 0), 2)
	return g

def main():
	img1 = cv2.imread('./images/group_photo2.jpg')
	img2 = face_detection(img1)
	cv2.imshow('Face Detection', img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

def live():    
	cap = cv2.VideoCapture(0)
	while True:
		ret, frame = cap.read()
		img2 = face_detection(frame)
		cv2.imshow('Face Detection', img2)
		k = cv2.waitKey(1) & 0xFF
		if k == 27:
			break
	cv2.destroyAllWindows()

main()
live()