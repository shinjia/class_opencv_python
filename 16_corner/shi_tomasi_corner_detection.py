import numpy as np
import cv2

def shi_tomasi_corner_detection(f):
	g = cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
	corners = cv2.goodFeaturesToTrack(f, 20, 0.01, 10)
	corners = np.int0(corners)
	for corner in corners:
		x, y = corner.ravel()
		cv2.circle(g, (x,y), 2, [255,0,0], 2)
	return g

def main():
	img1 = cv2.imread("./images/blox.bmp", 0)
	img2 = shi_tomasi_corner_detection(img1)
	cv2.imshow("Original Image", img1)
	cv2.imshow("Shi-Tomasi Corners", img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()