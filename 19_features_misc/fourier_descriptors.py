import numpy as np
import cv2
from numpy.fft import fft, ifft

def fourier_descriptor(f, thresh):
	g = f.copy()
	nr, nc = f.shape[:2]
	contours, hierarchy = cv2.findContours(f, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
	contour = np.vstack(contours).squeeze()
	N = len(contour)
	print(N)
	s_arr = np.zeros(N, dtype='complex')
	for n in range(N):
		s_arr[n] = complex(contour[n][1], contour[n][0])
	S_arr = fft(s_arr)
	thresh /= 100
	thresh = int(round(N / 2 * thresh))
	for k in range(thresh, N - thresh):
		S_arr[k] = 0
	s_arr = ifft(S_arr)
	for x in range(nr):
		for y in range(nc):
			if f[x,y] != 0:
				g[x,y] = 100
	for n in range(N):
		x = int(round(s_arr[n].real))
		y = int(round(s_arr[n].imag))
		g[x,y] = 255
	return g

def main():
	thresh = eval(input("Please enter threshold(%):"))
	img1 = cv2.imread("../images/Bug.bmp", 0)
	img2 = fourier_descriptor(img1, thresh)
	cv2.imshow("Original Image", img1)
	cv2.imshow("Fourier Descriptor", img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()