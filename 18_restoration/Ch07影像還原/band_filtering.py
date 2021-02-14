import numpy as np
import cv2
from numpy.fft import fft2, ifft2

def band_filtering( f, filter, D0, width, order ):
	nr, nc = f.shape[:2]	

	fp = np.zeros( [ nr, nc ] )				# 前處理
	for x in range( nr ):
		for y in range( nc ):
			fp[x,y] = pow( -1, x + y ) * f[x,y]
	
	F = fft2( fp )							# 離散傅立葉轉換
	G = F.copy( )
	
	if filter == 1:							# 理想帶阻濾波器
		for u in range( nr ):
			for v in range( nc ):
				dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
				                ( v - nc / 2 ) * ( v - nc / 2 ) )
				if dist >= D0 - width / 2 and dist <= D0 + width / 2:
					G[u,v] = 0				

	elif filter == 2:						# 理想帶通濾波器
		for u in range( nr ):
			for v in range( nc ):
				dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
				                ( v - nc / 2 ) * ( v - nc / 2 ) )
				if dist < D0 - width / 2 or dist > D0 + width / 2:
					G[u,v] = 0

	elif filter == 3:						# 高斯帶阻濾波器
		for u in range( nr ):
			for v in range( nc ):
				dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
				                ( v - nc / 2 ) * ( v - nc / 2 ) )
				if dist != 0 and width != 0:
					H = 1.0 - np.exp( -pow( ( dist * dist - D0 * D0 ) / 
			   			( dist * width ), 2 ) )				
					G[u,v] *= H

	elif filter == 4:						# 高斯帶通濾波器
		for u in range( nr ):
			for v in range( nc ):
				dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
				                ( v - nc / 2 ) * ( v - nc / 2 ) )
				if dist != 0 and width != 0:
					H = np.exp( -pow( ( dist * dist - D0 * D0 ) / 
				        ( dist * width ), 2 ) )				
					G[u,v] *= H

	elif filter == 5:						# 巴特沃斯帶阻濾波器
		for u in range( nr ):
			for v in range( nc ):
				dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
				                ( v - nc / 2 ) * ( v - nc / 2 ) )
				if dist != D0:
					H = 1.0 / ( 1.0 + pow( ( dist * width ) / 
		            	( dist * dist - D0 * D0 ), 2 * order ) )
					G[u,v] *= H
				else:
					G[u,v] = 0

	elif filter == 6:						# 巴特沃斯帶通濾波器
		for u in range( nr ):
			for v in range( nc ):
				dist = np.sqrt( ( u - nr / 2 ) * ( u - nr / 2 ) +
				                ( v - nc / 2 ) * ( v - nc / 2 ) )
				if dist != D0:				
					H = 1.0 - 1.0 / ( 1.0 + pow( ( dist * width ) / 
		            	( dist * dist - D0 * D0 ), 2 * order ) )			
					G[u,v] *= H

	gp = ifft2( G )							# 反離散傅立葉轉換

	gp2 = np.zeros( [ nr, nc ] )			# 後處理
	for x in range( nr ):
		for y in range( nc ):
			gp2[x,y] = round( pow( -1, x + y ) * np.real( gp[x,y] ), 0 )
	g = np.uint8( np.clip( gp2, 0, 255 ) )

	return g
	
def main( ):
	img1 = cv2.imread( "Brunch_Periodic_Noise.bmp", -1 )
	img2 = band_filtering( img1, 1, 100, 20.0, 1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Bandreject Filtering", img2 )
	cv2.waitKey( 0 )

main( )