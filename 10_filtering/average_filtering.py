import numpy as np
import cv2

img1 = cv2.imread( "../images/Lenna.bmp", -1 )
img2 = cv2.blur( img1, ( 5, 5 ) )
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Average Filtering", img2 )
cv2.waitKey( 0 )