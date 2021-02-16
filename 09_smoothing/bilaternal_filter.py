import cv2

img = cv2.imread("../images/lenna.png")

r1 = cv2.bilateralFilter(img, 11,  50,  50)
r2 = cv2.bilateralFilter(img, 25, 100, 100)

cv2.imshow("original", img)
cv2.imshow("result 1", r1)
cv2.imshow("result 2", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
