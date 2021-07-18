import numpy as np
import cv2

filename = './images/blend_landscape.jpg'

img = cv2.imread(filename)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # 轉為 HSV 格式

lower_green = np.array([35,43,46])
upper_green = np.array([77,255,255])
mask = cv2.inRange(hsv,lower_green,upper_green)

ret = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("Original Image", img)
cv2.imshow("Result", ret)
cv2.waitKey(0)
