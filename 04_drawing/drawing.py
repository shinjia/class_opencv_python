import numpy as np
import cv2

# 定義全黑影像
img = np.zeros([400, 500, 3], dtype='uint8')

# 直線
cv2.line(img, (50, 50),  (150, 150), (255, 0, 0), 2, cv2.LINE_AA, 0)

# 矩形
cv2.rectangle(img, (200, 50), (300, 150), (0, 255, 0), -1)

# 圓形
cv2.circle(img, (400, 100), 50, (0, 0, 255), -1)

# 橢圓形
cv2.ellipse(img, (100, 300), (60, 40), 135, 0, 360, (255, 255, 0), 1)

# 多邊形
points = np.array([ [200, 220], [220, 350], [280, 320], [300, 250] ])
cv2.polylines(img, [points], True, (255, 0, 255))

# 填滿多邊形
points = np.array( [ [400, 220], [350, 300], [420, 350], [450, 250] ])
cv2.fillPoly(img, [points], (255, 255, 0))

# 顯示影像
cv2.imshow("image", img)
cv2.waitKey(0)
