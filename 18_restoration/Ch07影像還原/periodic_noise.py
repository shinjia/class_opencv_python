import numpy as np
import cv2
from numpy.fft import fft2, ifft2, fftshift

def fourier_spectrum( f ):
	F = fft2( f )
	Fshift = fftshift( F )
	mag = np.abs( Fshift )
	mag = mag / mag.max( ) * 255.0 * 100.0
	g = np.uint8( np.clip( mag, 0, 255 ) )
	return g

def periodic_noise( f, scale, frequency, angle ):
	g = f.copy( )
	nr, nc = f.shape[:2]

	fp = np.zeros( [ nr, nc ] )				# 前處理
	for x in range( nr ):
		for y in range( nc ):
			fp[x,y] = pow( -1, x + y ) * f[x,y]
	
	F = fft2( fp )							# 離散傅立葉轉換
	G = F.copy( )

	magnitude = np.sum( F ) * scale			# 週期性雜訊
	for theta in range( 0, 360, angle ):
		u = int( frequency * np.cos( theta * np.pi / 180 ) + nr / 2 )
		v = int( frequency * np.sin( theta * np.pi / 180 ) + nc / 2 )
		G[u,v] = magnitude

	gp = ifft2( G )							# 反離散傅立葉轉換

	gp2 = np.zeros( [ nr, nc ] )			# 後處理
	for x in range( nr ):
		for y in range( nc ):
			gp2[x,y] = round( pow( -1, x + y ) * np.real( gp[x,y] ), 0 )
	g = np.uint8( np.clip( gp2, 0, 255 ) )

	return g
	
def main( ):
	f = cv2.imread( "Brunch.bmp", 0 )
	g = periodic_noise( f, 0.05, 100, 45 )
	g_spectrum = fourier_spectrum( g )
	cv2.imshow( "Original Image", f )
	cv2.imshow( "Periodic Noise", g )
	cv2.imshow( "Spectrum", g_spectrum )
	cv2.waitKey( 0 )

main( )