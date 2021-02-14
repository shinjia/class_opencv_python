import numpy as np
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Define the codec and create VideoWriter object
filename = "output.avi"
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# filename = "output.mp4"
# fourcc = cv2.VideoWriter_fourcc(*'MP4V')

out = cv2.VideoWriter(filename, fourcc, 20.0, (640,480))
# 第一個參數：輸出的檔名
# 第二個參數：指定 FourCC，指定影像編碼方式
# 第三個參數：fps 影像幀率
# 第四個參數：frameSize 影像大小

while(cap.isOpened()):
    ret, img = cap.read()
    if ret==True:
        img = cv2.flip(img, 0)

        # write the flipped frame
        out.write(img)

        cv2.imshow('frame', img)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
print("影片檔案已儲存 ", filename)
