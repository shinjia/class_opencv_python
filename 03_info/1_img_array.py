# 圖形轉為數字表示
import numpy as np
import cv2
from matplotlib import pyplot as plt

# (1) 整數，用 0 和 1 來表示黑白
p1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
p2 = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]

# (2) 整數，用 0 到 255 來表示黑白 (灰階)
# p1 = [[255, 255, 255], [255, 0, 255], [255, 255, 255]]
# p2 = [[255, 0, 255], [0, 255, 0], [255, 0, 255]]

# (3) 用浮點數來表示黑白 (通常正規化在 0.0 到 1.0 之間)
# p1 = [[1., 1., 1.], [1., 0., 1.], [1., 1., 1.]]
# p2 = [[1., 0., 1.], [0., 1., 0.], [1., 0., 1.]]

print('data type:', type(p1))

# 轉為 numpy 的陣列
# img1 = np.array(p1)
# img2 = np.array(p2)
img1 = np.array(p1).astype(np.uint8)  # 強制轉換為 uint8
img2 = np.array(p2).astype(np.uint8)  # 強制轉換為 uint8
print('data type:', type(img1))
print(img1.dtype)

# cv2.imshow("O", img1)
# cv2.imshow("X", img2)
# cv2.waitKey(0)

plt.figure(figsize=(9, 3), dpi=80)
plt.subplot(1, 2, 1), plt.imshow(img1, cmap='gray'), plt.title('O')
plt.subplot(1, 2, 2), plt.imshow(img2, cmap='gray'), plt.title('X')
plt.show()
