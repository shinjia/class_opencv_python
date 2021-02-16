import cv2

img = cv2.imread('../images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobelx = cv2.convertScaleAbs(sobelx)   # 轉回 uint8

sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobely = cv2.convertScaleAbs(sobely)   # 轉回 uint8

sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)  

sobelxy11 = cv2.Sobel(img, cv2.CV_64F, 1, 1)
sobelxy11 = cv2.convertScaleAbs(sobelxy11) 

cv2.imshow("original", img)
cv2.imshow("x+y", sobelxy)
cv2.imshow("xy11", sobelxy11)

cv2.waitKey(0)
cv2.destroyAllWindows()
