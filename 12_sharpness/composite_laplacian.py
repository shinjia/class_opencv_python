import numpy as np
import cv2

def composite_laplacian(f):
	kernel = np.array([ [0, -1, 0], [-1, 5, -1], [0, -1, 0] ])
	temp = cv2.filter2D(f, cv2.CV_32F, kernel)
	g = np.uint8(np.clip(temp, 0, 255))
	return g
		
def main():
	img = cv2.imread("../images/osaka.bmp", -1)
	r = composite_laplacian(img)
	cv2.imshow("Original Image", img)	
	cv2.imshow("Composite Laplacian", r)
	cv2.waitKey(0)

main()