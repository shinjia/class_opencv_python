import numpy as np
import cv2

img1 = cv2.imread( "Baboon.bmp", -1 )
img2 = cv2.GaussianBlur( img1, ( 5, 5 ), 0 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Gaussian Filtering", img2 )
cv2.waitKey( 0 )