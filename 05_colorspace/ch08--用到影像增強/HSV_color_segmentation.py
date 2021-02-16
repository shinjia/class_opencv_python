import numpy as np
import cv2

def HSV_color_segmentation( f, H1, H2, S1, S2, V1, V2 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	hsv = cv2.cvtColor( f, cv2.COLOR_BGR2HSV )
	for x in range( nr ):
		for y in range( nc ):
			H = hsv[x,y,0] * 2
			S = hsv[x,y,1] / 255 * 100
			V = hsv[x,y,2] / 255 * 100
			if not ( H >= H1 and H <= H2 and S >= S1 and S <= S2
				     and V >= V1 and V <= V2 ):
				g[x,y,0] = g[x,y,1] = g[x,y,2] = 0
	return g

def main( ):
	img1 = cv2.imread( "Flower.bmp", -1 )
	img2 = HSV_color_segmentation( img1, 30, 70, 30, 100, 30, 100 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "HSV Color Segmentation", img2 )
	cv2.waitKey( 0 )

main( )