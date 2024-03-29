import cv2

img = cv2.imread("../images/lenna_noise.png")

r1 = cv2.GaussianBlur(img, (3,3), 0, 0)
r2 = cv2.GaussianBlur(img, (5,5), 0, 0)

cv2.imshow("original",img)
cv2.imshow("result 1 (3x3)", r1)
cv2.imshow("result 2 (5x5)", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
