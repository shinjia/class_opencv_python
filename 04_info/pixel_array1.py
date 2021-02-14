import numpy as np
import cv2

# OpenCV cv2 module can accept NumPyarray.
# The only thing you need to care for is that {0,1} is mapped to {0,255}
# and any value bigger than 1 in NumPy array is equal to 255.
# So we should divide by 255 in our code

img = np.zeros([200,300,3])

b, g, r = 64, 128, 192

# 指定每一個 pixel 的 b,g,r 顏色值
w, h = img.shape[0], img.shape[1]
img[:,:,0] = np.ones([w, h])*b/255.0
img[:,:,1] = np.ones([w, h])*g/255.0
img[:,:,2] = np.ones([w, h])*r/255.0

# 指定每一個 pixel
# img[:,:] = (b, g, r)
# img[:,:,:] /= 255.0

cv2.imshow("image", img)
cv2.waitKey(0)
