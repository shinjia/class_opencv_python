import numpy as np
import cv2

img = cv2.imread("./images/test3.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 0)

contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (255, 0, 0), thickness=2)

# 顯示結果
print("一共有" + str(len(contours)) + "個 contours")
idx = 0
for one in contours:
    print("contour[", idx, "] 有", str(len(one)), "個點")
    idx += 1

cv2.imshow("Original", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
