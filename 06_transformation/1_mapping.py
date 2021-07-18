import numpy as np
import cv2

def forward_mapping(f):
	nr, nc = f.shape[:2]
	g = np.zeros([nr*2, nc*2, 3], dtype = 'uint8')
	for x in range(nr):
		for y in range(nc):
			for k in range(3):
				g[x*2, y*2, k] = f[x,y,k]
	return g			

def main():
	img1 = cv2.imread("../images/Baboon.bmp", -1)
	img2 = forward_mapping(img1)

	cv2.imshow("Original Image", img1)
	cv2.imshow("Forward Mapping", img2)
	cv2.waitKey(0)

main()