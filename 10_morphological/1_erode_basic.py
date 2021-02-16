import cv2
import numpy as np

# demo 1
img = np.zeros((5,5), np.uint8)
img[1:4,1:4] = 1
kernel = np.ones((3,1), np.uint8)
r = cv2.erode(img, kernel)

print("img=\n", img)
print("kernel=\n", kernel)
print("erosion=\n", r)

# demo 2
img = np.zeros((7,7), np.uint8)
img[1:6,1:6] = 1
r1 = cv2.erode(img, kernel, iterations=1)
r2 = cv2.erode(img, kernel, iterations=2)

print("img=\n", img)
print("kernel=\n", kernel)
print("erosion 1=\n", r1)
print("erosion 2=\n", r2)
