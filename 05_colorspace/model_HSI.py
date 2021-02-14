import numpy as np
import cv2

def RGB_to_HSI( R, G, B ):
	r = R / 255
	g = G / 255
	b = B / 255
	if R == G and G == B:  
		H = -1.0  
		S =  0.0
		I = ( r + g + b ) / 3
	else:                  
		x = ( 0.5 * ( ( r - g ) + ( r - b ) ) ) / \
		    np.sqrt( ( r - g ) ** 2 + ( r - b ) * ( g - b ) )
		if x < -1.0:  x = -1.0
		if x >  1.0:  x =  1.0
		theta = np.arccos( x ) * 180 / np.pi
		if B <= G:  
			H = theta
		else:
			H = 360.0 - theta
		S = 1.0 - 3.0 / ( r + g + b ) * min( r, g, b )
		I = ( r + g + b ) / 3
	return H, S, I

def HSI_model( f, channel ):
	nr, nc = f.shape[:2]
	g = np.zeros( [nr, nc], dtype = 'uint8' )
	if channel == 1:		# Hue
		for x in range( nr ):
			for y in range( nc ):
				H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
				if H == -1: 
					k = 0
				else:		
					k = round( H * 255 / 360 )
				g[x,y] = np.uint8( k )
	elif channel == 2:		# Saturation
		for x in range( nr ):
			for y in range( nc ):
				H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
				k = round( S * 255 )
				g[x,y] = np.uint8( k )
	else:					# Intensity
		for x in range( nr ):
			for y in range( nc ):
				H, S, I = RGB_to_HSI( f[x,y,2], f[x,y,1], f[x,y,0] )
				k = round( I * 255 )
				g[x,y] = np.uint8( k )
	return g
	
def main( ):
	img = cv2.imread( "../images/Rose.bmp", -1 )
	H = HSI_model( img, 1 )
	S = HSI_model( img, 2 )
	I = HSI_model( img, 3 )
	cv2.imshow( "Original Image", img )
	cv2.imshow( "Hue", H )
	cv2.imshow( "Saturation", S )
	cv2.imshow( "Intensity", I )
	cv2.waitKey( 0 )

main( )