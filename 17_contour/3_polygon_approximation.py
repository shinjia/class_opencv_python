import numpy as np
import cv2

def polygon_approximation(f, epislon):
	g = f.copy()
	nr, nc = f.shape[:2]
	contours, hierarchy = cv2.findContours(f, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)	
	approx = cv2.approxPolyDP(contours[0], epislon, True)
	for x in range(nr):
		for y in range(nc):
			if f[x,y] != 0:
				g[x,y] = 100
	cv2.drawContours(g, [approx], -1, (255, 255, 255))
	return g

def main():
	epislon = eval(input("Please enter epislon:"))	
	img = cv2.imread("./images/bug.bmp", 0)
	r = polygon_approximation(img, epislon)
	cv2.imshow("Original Image", img)
	cv2.imshow("Polygon Approximation", r)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()