import numpy as np
import cv2

img1 = cv2.imread("../images/sudoku.jpg", -1)

nr, nc = img1.shape[:2]
pts1 = np.float32([[70, 79], [495, 66], [34, 514], [521, 520]])
pts2 = np.float32([[10, 10], [490, 10], [10, 490], [490, 490]])
T = cv2.getPerspectiveTransform(pts1, pts2)
img2 = cv2.warpPerspective(img1, T, (500, 500))

cv2.imshow("Original Image", img1)
cv2.imshow("Perspective Transform", img2)
cv2.waitKey(0)