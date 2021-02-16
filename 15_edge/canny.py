import numpy as np
import cv2

img = cv2.imread("../images/osaka.bmp", -1)

canny = cv2.Canny(img, 50, 200)

cv2.imshow("Original Image", img)
cv2.imshow("Canny Edge Detection", canny)

cv2.waitKey(0)
