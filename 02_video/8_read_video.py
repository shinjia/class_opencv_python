import cv2

# 開啟影片檔案
cap = cv2.VideoCapture('./images/vtest.avi')

# 以迴圈從影片檔案讀取影格，並顯示出來
while(cap.isOpened()):
    ret, img = cap.read()

    cv2.imshow('frame', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        cap.release()

cv2.destroyAllWindows()
