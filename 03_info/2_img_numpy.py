# 自由練習程式，分析圖片與 numpy 的關係
import cv2
from matplotlib import pyplot as plt

import sys
# numpy.set_printoptions(threshold=sys.maxsize) # 列印完整的資料內容 (記得要還原)
# numpy.set_printoptions(threshold = False) # 列印完整內容之設定，會還原恢復預設

# 指定圖檔名
# filename = './images/lenna.jpg'
filename = './images/icon_16x16_google.png'
# filename = './images/icon_24x24_google.png'
# filename = './images/icon_32x32_google.png'
# filename = './images/icon_48x48_google.png'
# filename = './images/icon_64x64_google.png'

# 請練習開啟圖檔
img = cv2.imread(filename, 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # 轉為 RGB 格式

# 請練習切片，切出 R, G, B 的陣列
r = img[:,:,0]
g = img[:,:,1]
b = img[:,:,2]

# 請檢查 numpy 裡的陣列數值，了解 numpy 和圖片之間的關連
print(r)

# 請練習顯示圖片
plt.figure(figsize=(9, 5), dpi=80)
plt.subplot(2, 3, 1), plt.imshow(img, cmap='gray'), plt.title('O')
plt.subplot(2, 3, 4), plt.imshow(r, cmap='gray'), plt.title('O')
plt.subplot(2, 3, 5), plt.imshow(b, cmap='gray'), plt.title('O')
plt.subplot(2, 3, 6), plt.imshow(b, cmap='gray'), plt.title('O')
plt.show()
