import numpy as np
import cv2

img1 = cv2.imread( "Poker.bmp", -1 )
nr, nc = img1.shape[:2]
pts1 = np.float32( [ [ 160, 165 ], [ 240, 390 ], [ 270, 125 ] ] )
pts2 = np.float32( [ [ 190, 140 ], [ 190, 375 ], [ 310, 140 ] ] )
T = cv2.getAffineTransform( pts1, pts2 )
img2 = cv2.warpAffine( img1, T, ( nc, nr ) )
cv2.imshow( "Original Image", img1 )
cv2.imshow( "Affine Transform", img2 )
cv2.waitKey( 0 )
cv2.imwrite( "O.bmp", img2 )