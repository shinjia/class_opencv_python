import numpy as np
import cv2

def laplacian( f ):
	temp = cv2.Laplacian( f, cv2.CV_32F ) + 128
	g = np.uint8( np.clip( temp, 0, 255 ) )
	return g
		
def main( ):
	img1 = cv2.imread( "../images/Osaka.bmp", -1 )
	img2 = laplacian( img1 )
	cv2.imshow( "Original Image", img1 )	
	cv2.imshow( "Laplacian", img2 )
	cv2.waitKey( 0 )

main( )