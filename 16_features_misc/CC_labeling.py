import numpy as np
import cv2

img1 = cv2.imread( "../images/ABC.bmp", -1 )
n, labels = cv2.connectedComponents( img1 )
print( "Number of Connected Components =", n )
cv2.normalize( labels, labels, 0, 255, cv2.NORM_MINMAX )
img2 = np.uint8( labels )
cv2.imshow( "Original Image",  img1 )
cv2.imshow( "Connected Component Labeling", img2 )	
cv2.waitKey( 0 )