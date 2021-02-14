import numpy as np
import cv2

global img

def onMouse(event, x, y, flags, param):
	x, y = y, x
	if img.ndim != 3:
		print("(x,y) = (%d, %d)" % (x, y), end = "  ")
		print("Gray-Level = %3d" % img[x, y] )
	else:
		print("(x,y) = (%d, %d)" % (x, y), end = "  ")
		print("(R, G, B) = (%3d, %3d, %3d)" % 
			   (img[x, y, 2], img[x, y, 1], img[x, y, 0]))		

filename = input("Please enter filename: ")
img = cv2.imread(filename, -1)
cv2.namedWindow(filename)
cv2.setMouseCallback(filename, onMouse)
cv2.imshow(filename, img)
cv2.waitKey(0)
