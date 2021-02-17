import numpy as np
import cv2

def SURF_feature_detection(f):
	g = cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
	surf = cv2.xfeatures2d.SURF_create()
	kp = surf.detect(f, None)
	g = cv2.drawKeypoints(f, kp, g, flags=4)
	return g

def main():
	img1 = cv2.imread("./images/blox.bmp", 0)
	img2 = SURF_feature_detection(img1)
	cv2.imshow("Original Image", img1)
	cv2.imshow(" SURF Features", img2)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()