import cv2
import numpy as np

img = cv2.imread("erode.bmp", cv2.IMREAD_UNCHANGED)
kernel = np.ones((5,5), np.uint8)

r1 = cv2.erode(img, kernel)
r2 = cv2.erode(img, kernel, iterations=10)

cv2.imshow("orriginal", img)
cv2.imshow("erosion x1", r1)
cv2.imshow("erosion x10", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
