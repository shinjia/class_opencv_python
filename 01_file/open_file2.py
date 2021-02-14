import cv2

img = cv2.imread('../images/demo.jpg')
# img = cv2.imread('../images/demo.jpg', cv2.IMREAD_UNCHANGED)  # -1
# img = cv2.imread('../images/demo.jpg', cv2.IMREAD_COLOR)      # 1, default
# img = cv2.imread('../images/demo.jpg', cv2.IMREAD_GRAYSCALE)  # 0

cv2.namedWindow('image', cv2.WINDOW_NORMAL)  # 設定視窗可以調整大小
# cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)  # default

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
