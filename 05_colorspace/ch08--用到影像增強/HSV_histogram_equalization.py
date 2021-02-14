import numpy as np
import cv2

def HSV_histogram_equalization( f ):
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	hsv[:,:,2] = cv2.equalizeHist( hsv[:,:,2] )
	g = cv2.cvtColor( hsv, cv2.COLOR_HSV2BGR )
	return g

def main( ):
	img1 = cv2.imread( "Rose.bmp", -1 )
	img2 = HSV_histogram_equalization( img1 )
	cv2.imshow( "Original Image", img1 )	
	cv2.imshow( "Histogram Equalization(HSV)", img2 )
	cv2.waitKey( 0 )

main( )