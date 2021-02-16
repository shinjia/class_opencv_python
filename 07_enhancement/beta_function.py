import numpy as np
import cv2
import scipy.special as special
import matplotlib.pyplot as plt

x = np.linspace( 0, 1, 256 )
x1 = x * 255
y1 = special.betainc( 0.5, 0.5, x ) * 255
y2 = x1
y3 = special.betainc( 2.0, 2.0, x ) * 255

plt.plot( x1, y1, '--', label = 'a = 0.5, b = 0.5' )			
plt.plot( x1, y2, '-',  label = 'a = 1.0, b = 1.0' )
plt.plot( x1, y3, '--', label = 'a = 2.0, b = 2.0' )
plt.xlabel( 'Input Intensity' )
plt.ylabel( 'Output Intensity' )
plt.legend( loc = 'lower right' )

plt.show( )