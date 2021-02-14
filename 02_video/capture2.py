import numpy as np
import cv2

# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 避免結束釋放時出現錯誤訊息
idx = 0
print("按 s 鍵可存檔")

while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    # Our operations on the frame come here
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.flip(img, 1)

    # Display the resulting frame
    cv2.imshow('frame', img) 

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord('s'): # 等候按 s 鍵後存檔
        idx += 1
        filename = "output_" + str(idx) + ".png"
        cv2.imwrite(filename, img)
        print("影像檔案儲存到 ", filename)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
