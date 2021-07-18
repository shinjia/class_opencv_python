import numpy as np
import cv2

# main program


# 讀入圖像並顯示 (注意格式是 BGR)
img = cv2.imread('./images/lenna_gray.bmp', 1)

# 黑色
black = np.zeros(img.shape, dtype='uint8')

# 白色
white = np.zeros(img.shape, np.uint8)
white.fill(255)  # 背景變更為白色

# 有顏色
color = np.ones(img.shape, dtype='uint8')
color[:] = (125, 50, 250)

## 兩圖運算 (原本的想法)
# 原本的觀念是直接用 ndarray 運算，但運算有可能會超過 0-255，形成問題
# 因為資料態是 uint8，相加會超過 256
# blend = img + white # 會變成全白 (數值會超過255)
# blend = img + color
# blend = white - img # 會變成反向
# blend = img - color # (數值會有可能為負數)

## 兩圖運算 (實際的做法，呼叫 cv2 的運算功能，可以避免錯誤的發生)
# blend = cv2.add(img, white) # 會變成全白
# blend = cv2.add(img, color)
blend = cv2.subtract(white, img) # 會變成反向
# blend = cv2.subtract(img, color)


cv2.imshow('Original Image', img)
cv2.imshow('Blend', blend)
cv2.waitKey(0)
