import numpy as np
import cv2

filename = "../images/Baboon.bmp"
ROI_x, ROI_y = 200, 100
ROI_nr, ROI_nc = 80, 160

# filename = input("Please enter filename: ")
# ROI_x, ROI_y = eval(input("Enter (x, y) for ROI: "))
# ROI_nr, ROI_nc = eval(input("Enter (rows, columns) for ROI: "))

img = cv2.imread(filename, -1)
ROI = img[ROI_x : ROI_x + ROI_nr, ROI_y : ROI_y + ROI_nc]

# 矩形 (注意繪圖的座標系和圖像是不同的)
cv2.rectangle(img, (ROI_y, ROI_x), (ROI_y+ROI_nc, ROI_x+ROI_nr), (0, 255, 0), 1)

cv2.namedWindow('original')
cv2.namedWindow('ROI', cv2.WINDOW_AUTOSIZE)
cv2.imshow('original', img)
cv2.imshow('ROI', ROI)

cv2.waitKey(0)
cv2.destroyAllWindows()
