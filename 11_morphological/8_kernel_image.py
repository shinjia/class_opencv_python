import cv2

img = cv2.imread("kernel.bmp", cv2.IMREAD_UNCHANGED)

kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59,59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS,  (59,59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,  (59,59))

r1 = cv2.dilate(img, kernel1)
r2 = cv2.dilate(img, kernel2)
r3 = cv2.dilate(img, kernel3)

cv2.imshow("orriginal", img)
cv2.imshow("r1 (RECT)", r1)
cv2.imshow("r2 (CROSS)", r2)
cv2.imshow("r3 (ELLIPSE)", r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
