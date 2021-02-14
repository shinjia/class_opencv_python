import numpy as np
import cv2

img1 = cv2.imread( "../images/Indoor_Over_Exposure.bmp", -1 )
img2 = cv2.equalizeHist( img1 )

cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Histogram Equalization", img2 )

cv2.waitKey( 0 )