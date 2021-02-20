import cv2
import numpy as np

img = cv2.imread('./plates/black_white_2014.png')

# 將車牌文字加入白色背景圖片中
# code = 'BMW8888'
img[38:126,   9: 54] = cv2.imread('./plates/B.png')
img[38:126,  57:102] = cv2.imread('./plates/M.png')
img[38:126, 105:150] = cv2.imread('./plates/W.png')
img[38:126, 167:212] = cv2.imread('./plates/8.png')
img[38:126, 215:260] = cv2.imread('./plates/8.png')
img[38:126, 263:308] = cv2.imread('./plates/8.png')
img[38:126, 311:356] = cv2.imread('./plates/8.png')

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
