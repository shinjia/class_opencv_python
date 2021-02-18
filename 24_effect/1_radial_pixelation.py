import numpy as np
import cv2

def radial_pixelation( f, delta_r, delta_theta ):
	nr, nc = f.shape[:2]
	map_x = np.zeros( [nr, nc], dtype = 'float32' )
	map_y = np.zeros( [nr, nc], dtype = 'float32' )
	x0, y0 = nr // 2, nc // 2
	for x in range( nr ):
		for y in range( nc ):
			r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
			if r == 0:  theta = 0
			else:		theta = np.arccos( ( x - x0 ) / r )
			r = r - r % delta_r
			if y - y0 < 0:  theta = -theta
			theta = theta - theta % ( np.radians( delta_theta ) )
			map_x[x,y] = np.clip( y0 + r * np.sin( theta ), 0, nc - 1 )
			map_y[x,y] = np.clip( x0 + r * np.cos( theta ), 0, nr - 1 )
	g = cv2.remap( f, map_x, map_y, cv2.INTER_LINEAR )
	return g

def main( ):
	img1 = cv2.imread('./images/peacock.bmp', -1)
	img2 = radial_pixelation(img1, 5, 5)
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Radial Pixelation", img2 )
	cv2.waitKey( 0 )

main( )