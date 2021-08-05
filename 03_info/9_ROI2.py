import cv2

RECT = ((220, 20), (370, 190))
(left, top), (right, bottom) = RECT

cap = cv2.VideoCapture(0)
ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / \
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

WIDTH = 400
HEIGHT = int(WIDTH / ratio)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (WIDTH, HEIGHT))
    frame = cv2.flip(frame, 1)

    # 取出子畫面
    roi = frame[top:bottom, left:right]
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    # 將處理完的子畫面貼回到原本畫面中
    frame[top:bottom, left:right] = roi

    # 在 ROI 範圍處畫個框
    cv2.rectangle(frame, RECT[0], RECT[1], (0,0,255), 2)
    cv2.imshow('frame', frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
