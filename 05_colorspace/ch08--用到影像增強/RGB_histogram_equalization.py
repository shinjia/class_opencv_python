import numpy as np
import cv2

def RGB_histogram_equalization( f ):
	g = f.copy( )
	for k in range( 3 ):
		g[:,:,k] = cv2.equalizeHist( f[:,:,k] )
	return g

def main( ):
	img1 = cv2.imread( "Rose.bmp", -1 )
	img2 = RGB_histogram_equalization( img1 )
	cv2.imshow( "Original Image", img1 )	
	cv2.imshow( "Histogram Equalization(RGB)", img2 )
	cv2.waitKey( 0 )

main( )