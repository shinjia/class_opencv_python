import numpy as np
from scipy.signal import convolve2d

x = np.array( [ [1, 1, 1], [1, 1, 1], [1, 1, 1] ] )
h = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
y1 = convolve2d( x, h, 'full' )
y2 = convolve2d( x, h, 'same' )

print("x =\n", x)
print("h =\n", h)
print("Full Convolution y1 =\n", y1)
print("Convolution y2 =\n", y2)
