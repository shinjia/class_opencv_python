import numpy as np
import cv2

def gamma_correction(f, gamma = 2.0):
	g = f.copy()
	nr, nc = f.shape[:2]
	c = 255.0 / (255.0 ** gamma)
	table = np.zeros(256)
	for i in range(256):
		table[i] = round(i ** gamma * c, 0)
	if f.ndim != 3:
		for x in range(nr):
			for y in range(nc):
				g[x,y] = table[f[x,y]]
	else:
		for x in range(nr):
			for y in range(nc):
				for k in range(3):
					g[x,y,k] = table[f[x,y,k]]		
	return g
	
def main():
	img = cv2.imread("../images/Museum.bmp", 0)
	img1 = gamma_correction(img, 0.1)
	img2 = gamma_correction(img, 0.2)
	img3 = gamma_correction(img, 0.5)
	cv2.imshow("Original Image", img)	
	cv2.imshow("Gamma = 0.1", img1)
	cv2.imshow("Gamma = 0.2", img2)
	cv2.imshow("Gamma = 0.5", img3)		
	cv2.waitKey(0)

main()