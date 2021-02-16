import numpy as np
import cv2

def inpainting( f, method = 1 ):
	nr, nc = f.shape[:2]
	mask = np.zeros( [ nr, nc ], dtype = 'uint8' )  # 建立遮罩
	for x in range( nr ):
		for y in range( nc ):
			if f[x,y,0] == 0 and f[x,y,1] == 255 and f[x,y,2] == 255:
				mask[x,y] = 255
	if method == 1:
		g = cv2.inpaint( f, mask, 3, cv2.INPAINT_NS )
	else:
		g = cv2.inpaint( f, mask, 3, cv2.INPAINT_TELEA )
	return g

def main( ):
	img1 = cv2.imread( "Shizheng_N7_Mask.bmp", -1 )
	img2 = inpainting( img1, 1 )
	cv2.imshow( "Original Image", img1 )
	cv2.imshow( "Inpainting", img2 )
	cv2.waitKey( 0 )

main( )	