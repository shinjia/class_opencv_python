import cv2
import numpy as np

img = cv2.imread('./images/lenna.jpg')

img = cv2.resize(img, None, fx=0.5, fy=0.5)   # 為了完整顯示，縮小一倍
blur2 = cv2.blur(img, (2,2))
blur3 = cv2.blur(img, (5,5))
blur4 = cv2.blur(img, (10,10))

h1 = np.hstack((img,blur2))
h2 = np.hstack((blur3,blur4))
v = np.vstack((h1, h2))

cv2.imshow("merged_img", v)

cv2.waitKey(0)
cv2.destroyAllWindows()
