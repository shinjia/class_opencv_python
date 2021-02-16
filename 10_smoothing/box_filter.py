import cv2

img = cv2.imread("../images/lenna_noise.png")

r1 = cv2.boxFilter(img, -1, (5,5))
r2 = cv2.boxFilter(img, -1, (2,2), normalize=0) 
r3 = cv2.boxFilter(img, -1, (5,5), normalize=0) 

cv2.imshow("original", img)
cv2.imshow("result 1", r1)
cv2.imshow("result 2", r2)
cv2.imshow("result 3", r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
