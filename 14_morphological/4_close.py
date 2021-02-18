
import cv2
import numpy as np

img1 = cv2.imread("./images/closing.bmp")
img2 = cv2.imread("./images/closing2.bmp")

k = np.ones((10,10), np.uint8)

r1 = cv2.morphologyEx(img1, cv2.MORPH_CLOSE, k, iterations=3)
r2 = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, k, iterations=3)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("result1", r1)
cv2.imshow("result2", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
