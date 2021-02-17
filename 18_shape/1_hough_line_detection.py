import numpy as np
import cv2
import math

img1 = cv2.imread("./images/traffic_lanes.bmp", -1)
img2 = img1.copy()
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 200)
lines = cv2.HoughLines(edges, 1, math.pi/180.0, 120)
if lines is not None:
	a,b,c = lines.shape
	for i in range(a):
		rho = lines[i][0][0]
		theta = lines[i][0][1]
		a = math.cos(theta)
		b = math.sin(theta)
		x0, y0 = a*rho, b*rho
		pt1 = (int(x0+1000*(-b)), int(y0+1000*(a)))
		pt2 = (int(x0-1000*(-b)), int(y0-1000*(a)))
		cv2.line(img2, pt1, pt2, (255, 0, 0), 1, cv2.LINE_AA)
cv2.imshow("Original Image", img1)
cv2.imshow("Canny Edge Detection", edges)
cv2.imshow("Hough Line Detection", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
