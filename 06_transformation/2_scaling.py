import numpy as np
import cv2

img1 = cv2.imread("../images/Lenna.png", -1)

nr, nc = img1.shape[:2]
scale = eval( input("Please enter scale: "))
nr2 = int(nr * scale)
nc2 = int(nc * scale)
img2 = cv2.resize(img1, (nr2, nc2), interpolation = cv2.INTER_LINEAR)

cv2.imshow("Original Image", img1)
cv2.imshow("Image Scaling", img2)
cv2.waitKey(0)