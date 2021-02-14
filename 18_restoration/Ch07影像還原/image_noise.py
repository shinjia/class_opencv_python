import numpy as np
import cv2
from numpy.random import uniform, normal, exponential, rayleigh
import matplotlib.pyplot as plt

def uniform_noise( f, scale ):		# 均勻雜訊
	g = f.copy( )	
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = f[x,y] + uniform( 0, 1 ) * scale	
			g[x,y] = np.uint8( np.clip( value, 0, 255 ) )
	return g

def gaussian_noise( f, scale ):		# 高斯雜訊
	g = f.copy( )	
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = f[x,y] + normal( 0, scale ) 	
			g[x,y] = np.uint8( np.clip( value, 0, 255 ) )
	return g

def exponential_noise( f, scale ):	# 指數雜訊
	g = f.copy( )	
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = f[x,y] + exponential( scale ) 	
			g[x,y] = np.uint8( np.clip( value, 0, 255 ) )
	return g

def rayleigh_noise( f, scale ):		# 瑞雷雜訊
	g = f.copy( )	
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = f[x,y] + rayleigh( scale ) 	
			g[x,y] = np.uint8( np.clip( value, 0, 255 ) )
	return g

def salt_pepper_noise( f, probability ):  # 鹽與胡椒雜訊
	g = f.copy( )	
	nr, nc = f.shape[:2]
	for x in range( nr ):
		for y in range( nc ):
			value = uniform( 0, 1 )
			if value > 0 and value <= probability / 2:
				g[x,y] = 0
			elif value > probability / 2 and value <= probability:
				g[x,y] = 255
			else:
				g[x,y] = f[x,y]
	return g

def histogram( f ):
	if f.ndim != 3:
		hist = cv2.calcHist( [f], [0], None, [256], [0,256] )
		plt.plot( hist )
	else:
		color = ( 'b', 'g', 'r' )
		for i, col in enumerate( color ):
			hist = cv2.calcHist( f, [i], None, [256], [0,256] )
			plt.plot( hist, color = col )
	plt.xlim( [0,256] )
	plt.xlabel( "Intensity" )
	plt.ylabel( "#Intensities" )
	plt.show( )

def main( ):
	print( "Image Degradation with Noise Model" )
	print( "(1) Uniform Noise" )
	print( "(2) Gaussian Noise" )
	print( "(3) Exponential Noise" )
	print( "(4) Rayleigh Noise" )
	print( "(5) Salt and Pepper Noise" )
	method = eval( input( "Please enter your choice: " ) )	
	if method >= 1 and method <= 4:
		scale = eval( input( "Please enter scale(e.g., 20): " ) )
	elif method == 5:
		probability = eval( input ( "Please enter probability(e.g., 0.05): " ) )
	else:
		print( "Noise model not supported!" )
		exit( )
	img1 = cv2.imread( "Pattern.bmp", -1 )
	if method == 1:
		img2 = uniform_noise( img1, scale )
	elif method == 2:
		img2 = gaussian_noise( img1, scale )
	elif method == 3:
		img2 = exponential_noise( img1, scale )
	elif method == 4:
		img2 = rayleigh_noise( img1, scale )
	else:
		img2 = salt_pepper_noise( img1, probability )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Noisy Image", img2 )		
	histogram( img2 )

main( )