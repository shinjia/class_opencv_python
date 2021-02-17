import cv2

# img = cv2.imread('./images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('./images/osaka.bmp', cv2.IMREAD_GRAYSCALE)

# 將 sobel 的 ksize 設為 -1，即為 scharr
ksize = -1  ## -1, 1, 3, 5

sobelx = cv2.Sobel(img,cv2.CV_64F, 1, 0, ksize=ksize)
sobelx = cv2.convertScaleAbs(sobelx)   # 轉回 uint8
sobely = cv2.Sobel(img,cv2.CV_64F, 0, 1, ksize=ksize)
sobely = cv2.convertScaleAbs(sobely)   # 轉回 uint8  
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0) 

scharrx = cv2.Scharr(img,cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)   # 轉回 uint8
scharry = cv2.Scharr(img,cv2.CV_64F, 0, 1)
scharry = cv2.convertScaleAbs(scharry)   # 轉回 uint8
scharrxy =  cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0) 

cv2.imshow("original", img)
cv2.imshow("sobelxy", sobelxy)
cv2.imshow("scharrxy", scharrxy)
cv2.imshow("diff", sobelxy-scharrxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
