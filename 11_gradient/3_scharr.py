import cv2

img = cv2.imread('./images/scharr.bmp', cv2.IMREAD_GRAYSCALE)

scharrx = cv2.Scharr(img, cv2.CV_64F, 1, 0)
scharrx = cv2.convertScaleAbs(scharrx)   # 轉回uint8

scharry = cv2.Scharr(img, cv2.CV_64F, 0, 1)  
scharry = cv2.convertScaleAbs(scharry)   # 轉回uint8

scharrxy =  cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)  

# 注意：下列式子是錯誤的，因為 dx+dy 必須等於 1
# scharrxy11 = cv2.Scharr(img, cv2.CV_64F, 1, 1)

cv2.imshow("original", img)
cv2.imshow("x", scharrx)
cv2.imshow("y", scharry)
cv2.imshow("x+y", scharrxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
