import numpy as np
import cv2

img = cv2.imread("../images/Baboon.bmp", -1)
nr, nc = img.shape[:2]

T = np.float32([[1, 0, 100], [0, 1, 150]])
img2 = cv2.warpAffine(img, T, (nc, nr))

cv2.imshow("Original Image", img)
cv2.imshow("Image Translate", img2)
cv2.waitKey(0)