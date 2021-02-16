import numpy as np
import cv2

def RGB_model( f, channel ):
	if channel == 1:	# Red
		return f[:,:,2]
	elif channel == 2:	# Green
		return f[:,:,1]
	else:				# Blue
		return f[:,:,0]

def main( ):
	img = cv2.imread( "../images/Rose.bmp", -1 )
	R = RGB_model( img, 1 )
	G = RGB_model( img, 2 )
	B = RGB_model( img, 3 )	
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Red", R )
	cv2.imshow( "Green", G )
	cv2.imshow( "Blue", B )
	cv2.waitKey( 0 )

main( )