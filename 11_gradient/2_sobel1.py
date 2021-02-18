import cv2

img = cv2.imread('./images/sobel4.bmp', cv2.IMREAD_GRAYSCALE)

sobelx_error = cv2.Sobel(img, -1, 1, 0)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelx = cv2.convertScaleAbs(sobelx)   # 转回uint8  

cv2.imshow("original", img)
cv2.imshow("with error", sobelx_error)
cv2.imshow("x", sobelx)

cv2.waitKey(0)
cv2.destroyAllWindows()
