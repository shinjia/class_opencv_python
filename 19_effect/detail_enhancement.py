import numpy as np
import cv2

img1 = cv2.imread( "../images/Brunch.bmp", -1 )
img2 = cv2.detailEnhance( img1 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Detail Enhance", img2 )
cv2.waitKey( 0 )