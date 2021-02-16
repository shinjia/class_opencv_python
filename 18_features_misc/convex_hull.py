import numpy as np
import cv2

def convex_hull( f ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	contours, hierarchy = cv2.findContours( f, 
              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
	hull = []
	for i in range( len( contours ) ):
		hull.append( cv2.convexHull( contours[i], False ) )
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y] != 0:
				g[x,y] = 100
	cv2.drawContours( g, contours, -1, ( 255, 255, 255 ), 1, 8 )		
	cv2.drawContours( g, hull, -1, ( 255, 255, 255 ), 2, 8 )
	return g

def main( ):
	img1 = cv2.imread( "../images/Hand.bmp", 0 )
	img2 = convex_hull( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Convex Hull", img2 )
	cv2.waitKey( 0 )

main( )