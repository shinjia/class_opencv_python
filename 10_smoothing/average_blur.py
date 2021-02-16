import cv2

img = cv2.imread("../images/lenna_noise.png")

r3 = cv2.blur(img, (3,3))
r5 = cv2.blur(img, (5,5))
r30 = cv2.blur(img, (30,30))

cv2.imshow("original", img)
cv2.imshow("result 3x3", r3)
cv2.imshow("result 5x5", r5)
cv2.imshow("result 30x30", r30)

cv2.waitKey(0)
cv2.destroyAllWindows()
