# Source: https://github.com/sunsided/python-conv2d/blob/master/convolutions.py

import cv2
import numpy as np

filename = './images/icon_16x16_google.png'

# load the image and scale to 0..1
img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE).astype(float) / 255.0

# load + show the original
cv2.imshow('original', img)

kernel = np.array([
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]]) / 9.0

# kernel = np.array([
#   [1, 0, -1],
#   [1, 0, -1],
#   [1, 0, -1]])

img1 = cv2.filter2D(src=img, kernel=kernel, ddepth=-1)

cv2.imshow('Filter', img1)

# wait and quit
cv2.waitKey(0)
cv2.destroyAllWindows()
