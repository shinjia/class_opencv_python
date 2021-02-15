import cv2
import numpy as np

img = cv2.imread("dilation.bmp", cv2.IMREAD_UNCHANGED)
kernel = np.ones((9,9), np.uint8)

r1 = cv2.dilate(img, kernel)
r2 = cv2.dilate(img, kernel, iterations=5)

cv2.imshow("original", img)
cv2.imshow("dilation x1", r1)
cv2.imshow("dilation x5", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
