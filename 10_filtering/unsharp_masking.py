import numpy as np
import cv2

def unsharp_masking( f, k = 1.0 ):
	g = f.copy( )
	nr, nc = f.shape[:2]
	f_avg = cv2.GaussianBlur( f, ( 15, 15 ), 0 )
	for x in range( nr ):
		for y in range( nc ):
			g_mask = int( f[x,y] ) - int( f_avg[x,y] ) 
			g[x,y] = np.uint8( np.clip( f[x,y] + k * g_mask, 0, 255 ) )
	return g
		
def main( ):
	img1 = cv2.imread( "../images/Osaka.bmp", -1 )
	img2 = unsharp_masking( img1, 10.0 )
	cv2.imshow( "Original Image", img1 )	
	cv2.imshow( "Unsharp Masking", img2 )
	cv2.waitKey( 0 )

main( )