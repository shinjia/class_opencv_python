import cv2

img = cv2.imread("../images/bil_test.bmp")

g = cv2.GaussianBlur(img, (55, 55), 0, 0)
b = cv2.bilateralFilter(img, 55, 100, 100)

cv2.imshow("original", img)
cv2.imshow("Gaussian", g)
cv2.imshow("bilateral", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
