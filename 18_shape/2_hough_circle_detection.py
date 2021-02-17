import numpy as np
import cv2
import math

img1 = cv2.imread( "./images/cans.bmp", -1 )
img2 = img1.copy( )
gray = cv2.cvtColor( img1, cv2.COLOR_BGR2GRAY )
circles = cv2.HoughCircles( gray, cv2.HOUGH_GRADIENT, 1, 150, 200, 50, 
                            minRadius = 120, maxRadius = 200 )
circles = np.uint16( np.around( circles ) )
for i in circles[0,:]:
	cv2.circle( img2, ( i[0], i[1] ), i[2], ( 0, 255, 0 ), 2 )
	cv2.circle( img2, ( i[0], i[1] ), 2, ( 0, 0, 255 ), 3 )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Circle Detection", img2 )
cv2.waitKey( 0 )
cv2.destroyAllWindows()
