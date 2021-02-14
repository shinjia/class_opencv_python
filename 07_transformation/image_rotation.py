import numpy as np
import cv2

img1 = cv2.imread( "../images/Lenna.bmp", -1 )
nr2, nc2 = img1.shape[:2]
rotation_matrix = cv2.getRotationMatrix2D( ( nr2 / 2, nc2 / 2 ), 30, 1 )
img2 = cv2.warpAffine( img1, rotation_matrix, ( nr2, nc2 ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Image Rotation", img2 )
cv2.waitKey( 0 )