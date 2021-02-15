import numpy as np

x = np.array( [ 1, 2, 4, 3, 2, 1, 1 ] )
h = np.array( [ 1, 2, 3, 1, 1 ] )
y1 = np.convolve(x, h, 'full')
y2 = np.convolve(x, h, 'same')

print("x =", x)
print("h =", h)
print("Full Convolution y1 =", y1)
print("Convolution y2 =", y2)