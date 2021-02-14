import numpy as np
import cv2

def RGB_gamma_correction( f, channel, gamma ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	c = 255.0 / ( 255.0 ** gamma )
	table = np.zeros( 256 )
	for i in range( 256 ):
		table[i] = round( i ** gamma * c, 0 ) 
	if channel == 1:    k = 2
	elif channel == 2:  k = 1
	else:    		    k = 0
	for x in range( nr ):
		for y in range( nc ):
			g[x,y,k] = table[f[x,y,k]]
	return g	

def main( ):	
	img  = cv2.imread( "Rose.bmp", -1 )
	gamma = eval( input( "Please enter gamma: " ) )
	img1 = RGB_gamma_correction( img, 1, gamma )
	img2 = RGB_gamma_correction( img, 2, gamma )
	img3 = RGB_gamma_correction( img, 3, gamma )
	cv2.imshow( "Original Image", img )	
	cv2.imshow( "Gamma Correction(R)", img1 )
	cv2.imshow( "Gamma Correction(G)", img2 )
	cv2.imshow( "Gamma Correction(B)", img3 )	
	cv2.waitKey( 0 )

main( )