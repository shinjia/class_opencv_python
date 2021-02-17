import numpy as np
import cv2

# You don't need to convert NumPy array to Mat because OpenCV cv2 module
# can accept NumPyarray. The only thing you need to care for is that {0,1}
# is mapped to {0,255} and any value bigger than 1 in NumPy array is equal
# to 255. So you should divide by 255 in your code, as shown below.

img = np.zeros([200,300,3])

img[   :100,   :100] = (255, 255, 255)
img[   :100,100:200] = (  0,   0, 255)
img[   :100,200:300] = (  0, 255, 255)
img[100:200,   :200] = (  0, 255,   0)
img[100:200,100:200] = (255,   0,   0)
img[100:200,200:300] = (  0,   0,   0)

img[:,:,:] /= 255.0

cv2.imshow("image", img)
cv2.waitKey(0)
