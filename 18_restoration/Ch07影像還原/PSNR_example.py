import numpy as np
import cv2
from numpy.random import normal

def gaussian_noise( f, scale ):		# 高斯雜訊
	g = f.copy( )	
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = f[x,y] + normal( 0, scale ) 	
			g[x,y] = np.uint8( np.clip( value, 0, 255 ) )
	return g

def PSNR( f, g ):					# PSNR
	nr, nc = f.shape[:2]
	MSE = 0.0
	for x in range( nr ):
		for y in range( nc ):
			MSE += ( float( f[x,y] ) - float( g[x,y] ) ) ** 2
	MSE /= ( nr * nc )
	PSNR = 10 * np.log10( ( 255 * 255 ) / MSE )
	return PSNR

def main( ):
	f = cv2.imread( "Brunch.bmp", 0 )
	g = gaussian_noise( f, 20 )
	print( "PSNR =", PSNR( f, g ) )
	cv2.imshow( 'Original Image', f )
	cv2.imshow( 'Gaussian Noise', g )
	cv2.waitKey( 0 )

main( )