import cv2

o = cv2.imread("../images/lenna.jpg")

down = cv2.pyrDown(o)
up = cv2.pyrUp(down)
diff = up - o    # 查看 down-up 後與原始的區別
print("o.shape=", o.shape)
print("up.shape=", up.shape)

cv2.imshow("original", o)
cv2.imshow("up", up)
cv2.imshow("difference", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
