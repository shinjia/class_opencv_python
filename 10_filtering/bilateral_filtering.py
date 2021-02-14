import numpy as np
import cv2

img1 = cv2.imread( "../images/Jenny.bmp", -1 )
img2 = cv2.bilateralFilter( img1, 11, 50, 50 )
cv2.imshow( "Original Image", img1 )	
cv2.imshow( "Bilateral Filtering", img2 )
cv2.waitKey( 0 )