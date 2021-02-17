import numpy as np
import cv2

img1 = cv2.imread("./images/shapes.bmp", 0)
img2 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

contours, hierarchy = cv2.findContours(img1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(img2, contours, -1, (255, 0, 0), thickness=2)

# 顯示結果
print("一共有" + str(len(contours)) + "個 contours")
idx = 0
for one in contours:
    print("contour[", idx, "] 有", str(len(one)), "個點")
    idx += 1

cv2.imshow("Original", img1)
cv2.imshow("Contours", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
