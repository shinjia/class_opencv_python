import cv2
import numpy as np
from scipy import ndimage

filename = './images/icon_16x16_google.png'


img = np.array([
     [10,20,30,40,50],
     [20,30,40,50,60],
     [30,40,50,60,70],
     [40,50,60,70,80] ]).astype('uint8')

# prepare the filter
kernel = np.array([[1,1,1],[1,1,0],[1,0,0]])/6
# kernel = np.array([[0,0,1],[0,1,1],[1,1,1]])/6
# kernel = np.array([[1,1,1],[0,0,0],[-1,-1,-1]])
# kernel = np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])

# apply kernel to the original image using correlation filtering
# kernel = np.flip(kernel) 

corr = cv2.filter2D(img, -1, kernel)

# apply kernel to the original image using convolution filtering
# conv  = ndimage.convolve(img, kernel, mode='constant', cval=1.0)
conv  = ndimage.convolve(img, kernel, mode='mirror')

# test
kernel = np.flip(kernel) 
test = cv2.filter2D(img, -1, kernel)

# 將最後一個值調一樣 (讓圖像的顏色真實)
# img[-1,-2] = corr[-1,-2] = conv[-1,-2] = test[-1,-2] = 0
# img[-1,-1] = corr[-1,-1] = conv[-1,-1] = test[-1,-1] = 100

print(img, '\n---------------------------------------')
print(corr, '\n---------------------------------------')
print(conv, '\n---------------------------------------')
print(test, '\n---------------------------------------')

cv2.imshow('Original', img)
cv2.imshow('Correlation', corr)
cv2.imshow('Convolution', conv)
cv2.imshow('flip+filter2D', test)

# wait and quit
cv2.waitKey(0)
cv2.destroyAllWindows()
