# data type
import numpy as np
import cv2

# (1) float
img1 = np.zeros([200,300,3])
print(type(img1))
print(type(img1[0,0,0]))

# 指定每一個 pixel
img1[:,:] = (64, 128, 192)
img1[:,:,:] /= 255.0

## (2) int
img2 = np.zeros([200,300,3]).astype(np.uint8)

print(type(img2))
print(type(img2[0,0,0]))

# 指定每一個 pixel
img2[:,:] = (64, 128, 192)

cv2.imshow("image 1", img1)
cv2.imshow("image 2", img2)
cv2.waitKey(0)
