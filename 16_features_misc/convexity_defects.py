import cv2
import numpy as np

def convexity_defects( f ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	contours, hierarchy = cv2.findContours( f, 
              cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE )
	cnt = contours[0]
	hull = cv2.convexHull( cnt,returnPoints = False)
	defects = cv2.convexityDefects( cnt, hull )
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y] != 0:
				g[x,y] = 100
	for i in range(defects.shape[0]):
		s,e,f,d = defects[i,0]
		start = tuple( cnt[s][0] )
		end = tuple( cnt[e][0] )
		far = tuple( cnt[f][0] )
		cv2.line( g, start, end, ( 255,255,255 ), 1 )
		cv2.circle( g, far, 5, ( 255,255,255 ), -1 )
	return g

def main( ):
	img1 = cv2.imread( "../images/Hand.bmp", -1 )
	img2 = convexity_defects( img1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Convex Defects", img2 )
	cv2.waitKey( 0 )

main( )