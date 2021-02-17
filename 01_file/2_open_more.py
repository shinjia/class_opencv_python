import cv2

img  = cv2.imread('./images/demo.jpg')
img1 = cv2.imread('./images/demo.jpg', cv2.IMREAD_UNCHANGED)  # -1
img2 = cv2.imread('./images/demo.jpg', cv2.IMREAD_COLOR)      # 1, default
img3 = cv2.imread('./images/demo.jpg', cv2.IMREAD_GRAYSCALE)  # 0

cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 設定視窗可以調整大小
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)  # default

cv2.imshow('image', img)
cv2.imshow('image 1:unchanged', img1)
cv2.imshow('image 2:color'    , img2)
cv2.imshow('image 3:grayscale', img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
