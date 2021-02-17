import numpy as np
import cv2

def HSV_model( f, channel ):
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	if channel == 1:	# Hue
		return hsv[:,:,0]
	elif channel == 2:	# Saturation
		return hsv[:,:,1]
	else:				# Value
		return hsv[:,:,2]

def main( ):
	img = cv2.imread( "../images/Rose.bmp", -1 )
	H = HSV_model( img, 1 )
	S = HSV_model( img, 2 )
	V = HSV_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Hue", H )
	cv2.imshow( "Saturation", S )
	cv2.imshow( "Value", V )
	cv2.waitKey( 0 )

main( )