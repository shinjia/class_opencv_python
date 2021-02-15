import numpy as np
import cv2

def face_detection( f ):
	g = f.copy( )
	gray = cv2.cvtColor( f, cv2.COLOR_BGR2GRAY )
	face_cascade = cv2.CascadeClassifier( 'haarcascade_frontalface_default.xml' )
	faces = face_cascade.detectMultiScale( gray, 1.1, 5 )
	for ( x, y, w, h ) in faces:
		g = cv2.rectangle( g, ( x, y ), ( x + w, y + h ), ( 255, 0, 0 ), 2 )
	return g

def main( ):
	img1 = cv2.imread( "../images/Akiyo.bmp", -1 )
	img2 = face_detection( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Face Detection", img2 )
	cv2.waitKey( 0 )

main( )