import numpy as np
import cv2

# main program


# 讀入圖像並顯示 (注意格式是 BGR)
img = cv2.imread('./images/lenna.jpg', 1)

# ROI
# img = img[200:-200, 200:-200, :]
BLUE = [0,0,255]


b = 10  # 框厚度
replicate = cv2.copyMakeBorder(img,b,b,b,b,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,b,b,b,b,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,b,b,b,b,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,b,b,b,b,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,b,b,b,b,cv2.BORDER_CONSTANT,value=BLUE)


cv2.imshow('Original Image', img)
cv2.imshow('replicate', replicate)
cv2.imshow('reflect', reflect)
cv2.imshow('reflect101', reflect101)
cv2.imshow('wrap', wrap)
cv2.imshow('constant', constant)
cv2.waitKey(0)
