import numpy as np
import cv2

def radial_blur( f, filter_size ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	x0, y0 = nr // 2, nc // 2
	half = filter_size // 2
	for x in range( nr ):
		for y in range( nc ):
			r = np.sqrt( ( x - x0 ) ** 2 + ( y - y0 ) ** 2 )
			if r == 0:  theta = 0
			else:		theta = np.arccos( ( x - x0 ) / r )
			if y - y0 < 0:  theta = -theta
			R = G = B = n = 0
			for k in range( -half, half + 1 ):
				phi = theta + np.radians( k )
				xp = int( round( x0 + r * np.cos( phi ) ) )
				yp = int( round( y0 + r * np.sin( phi ) ) )
				if ( xp >= 0 and xp < nr and yp >= 0 and yp < nc ):
					R += f[xp,yp,2]
					G += f[xp,yp,1]
					B += f[xp,yp,0]
					n += 1
			R = round( R / n )
			G = round( G / n )
			B = round( B / n )
			g[x,y,2] = np.uint8( R )
			g[x,y,1] = np.uint8( G )
			g[x,y,0] = np.uint8( B )
	return g

def main( ):
	img1 = cv2.imread('./images/brunch.bmp', -1 )
	img2 = radial_blur( img1, 15 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Radial Blur", img2 )
	cv2.waitKey( 0 )

main( )