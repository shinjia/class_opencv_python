import numpy as np
import cv2

def twirl_effect( f, K ):
	nr, nc = f.shape[:2]
	map_x = np.zeros( [nr, nc], dtype = 'float32' )
	map_y = np.zeros( [nr, nc], dtype = 'float32' )
	x0, y0 = nr // 2, nc // 2
	for x in range( nr ):
		for y in range( nc ):
			r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
			if r == 0:  theta = 0
			else:		theta = np.arccos( ( x - x0 ) / r )
			if y - y0 < 0:  theta = -theta
			phi = theta + r / K
			map_x[x,y] = np.clip( y0 + r * np.sin( phi ), 0, nc - 1 )
			map_y[x,y] = np.clip( x0 + r * np.cos( phi ), 0, nr - 1 )
	g = cv2.remap( f, map_x, map_y, cv2.INTER_LINEAR )
	return g

def main( ):
	img1 = cv2.imread('./images/car.bmp', -1 )
	img2 = twirl_effect( img1, 50 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Twirl Effect", img2 )
	cv2.waitKey( 0 )

main( )