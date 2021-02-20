import cv2
import numpy as np

# 黑色
image = np.zeros((300, 400, 3), dtype='uint8')
cv2.imshow('image black', image)

# 有顏色
image = np.ones((300, 400, 3), dtype='uint8')
image[:] = (125, 50, 250)
cv2.imshow('image color', image)

# 白色
image = np.zeros((300, 400, 3), np.uint8)
image.fill(255)  # 背景變更為白色
cv2.imshow('image white', image)

# 漸層色 (水平黑到白)
image = np.zeros((300, 400, 3), np.uint8)
for j in range(300):
    for i in range(400):
        value = (255/400) * i
        image[j][i].fill(value)  # 背景變更為白色
cv2.imshow('image gradient', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
