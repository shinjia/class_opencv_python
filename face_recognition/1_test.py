import numpy as np
import cv2
import face_recognition
from PIL import Image, ImageDraw # 顯示圖片 （必須再次匯入）

cap = cv2.VideoCapture(1)

while True:
    # Capture frame-by-frame
    ret, img = cap.read()

    faces = face_recognition.face_locations(img, model='cnn')
    # print('找到臉的數量=', len(faces))
    for (top, right, bottom, left) in faces: #畫矩形框 可改框的顏色/線條粗細
        cv2.rectangle(img, (left, top), (right, bottom), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('frame', img)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
