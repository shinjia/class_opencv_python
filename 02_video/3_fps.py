import numpy as np
import cv2
import time

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  # 對速度有影響

n, time_begin = 0, time.time()
while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    # Display the resulting frame
    cv2.imshow('frame', img) 
    n += 1
    print('FPS: {:5.2f}'.format(n/(time.time()-time_begin)))

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
