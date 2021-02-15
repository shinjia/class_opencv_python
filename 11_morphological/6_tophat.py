import cv2
import numpy as np

img1 = cv2.imread("tophat.bmp", cv2.IMREAD_UNCHANGED)
img2 = cv2.imread("lena.bmp", cv2.IMREAD_UNCHANGED)

k = np.ones((5,5), np.uint8)

r1 = cv2.morphologyEx(img1, cv2.MORPH_TOPHAT, k)
r2 = cv2.morphologyEx(img2, cv2.MORPH_TOPHAT, k)

cv2.imshow("original1", img1)
cv2.imshow("original2", img2)
cv2.imshow("result1", r1)
cv2.imshow("result2", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
