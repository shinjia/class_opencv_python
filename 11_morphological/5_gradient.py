import cv2
import numpy as np

img = cv2.imread("gradient.bmp", cv2.IMREAD_UNCHANGED)
k = np.ones((5,5), np.uint8)

# 方法一：膨脹 - 腐蝕
e = cv2.erode(img, k)
d = cv2.dilate(img, k)
r1 = d - e

## 方法二：使用型態梯度
r2 = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)

cv2.imshow("original", img)
cv2.imshow("d-e", r1)
cv2.imshow("result", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
