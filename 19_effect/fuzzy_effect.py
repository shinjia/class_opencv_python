import numpy as np
import cv2
from numpy.random import uniform

def fuzzy_effect( f, W ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			xp = int( x + W * uniform() - W // 2 )
			yp = int( y + W * uniform() - W // 2 )
			xp = np.clip( xp, 0, nr - 1 )
			yp = np.clip( yp, 0, nc - 1 )
			g[x,y] = f[xp,yp]	
	return g

def main( ):
	img1 = cv2.imread( "../images/Brunch.bmp", -1 )
	img2 = fuzzy_effect( img1, 3 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Fuzzy Effect", img2 )
	cv2.waitKey( 0 )

main( )