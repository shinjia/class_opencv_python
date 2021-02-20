import numpy as np
import cv2

img1 = cv2.imread('./images/cow.jpg', -1)
img2 = cv2.edgePreservingFilter(img1)
cv2.imshow("Original Image",img1)
cv2.imshow("Edge-Preserving Filter", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()