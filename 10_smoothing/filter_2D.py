import cv2
import numpy as np

img = cv2.imread("../images/lenna.png")
kernel = np.ones((9,9), np.float32) / 81

r = cv2.filter2D(img, -1, kernel)

cv2.imshow("original", img)
cv2.imshow("Gaussian", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
