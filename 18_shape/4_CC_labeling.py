import numpy as np
import cv2

img = cv2.imread("./images/abc.bmp", -1)

n, labels = cv2.connectedComponents(img)
print("Number of Connected Components =", n)

cv2.normalize(labels, labels, 0, 255, cv2.NORM_MINMAX)
r = np.uint8(labels)

cv2.imshow("Original Image",  img)
cv2.imshow("Connected Component Labeling", r)
cv2.waitKey(0)
cv2.destroyAllWindows()
