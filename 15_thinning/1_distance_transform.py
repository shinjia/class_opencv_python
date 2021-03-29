import numpy as np
import cv2

img1 = cv2.imread("./images/shapes.bmp", 0)

dist = cv2.distanceTransform(img1, cv2.DIST_L1, 3)
cv2.normalize(dist, dist, 0, 255, cv2.NORM_MINMAX)
img2 = np.uint8(dist)

cv2.imshow("Original Image", img1)
cv2.imshow("Distance Transform", img2)
cv2.waitKey(0)