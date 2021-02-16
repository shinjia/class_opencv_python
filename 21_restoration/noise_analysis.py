import numpy as np
import cv2
import matplotlib.pyplot as plt

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

f = cv2.imread( "Noisy_Pattern.bmp", 0 )
ROI = f[55:95, 55:95]
histogram( ROI )
print( "Sigma =", np.std( ROI ) )