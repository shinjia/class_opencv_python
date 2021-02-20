import numpy as np
import cv2

# img1 = cv2.imread("./images/DSP.bmp", 0)
# img2 = cv2.imread("./images/DSP_Scene.bmp", 0)
img1 = cv2.imread('./images/box.png', -1)
img2 = cv2.imread('./images/box_in_scene.png', -1)


orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = bf.match(des1,des2)
img3 = cv2.drawMatches(img1, kp1, img2, kp2, matches, None, flags=2)
cv2.imshow("Feature Matching", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
