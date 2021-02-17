import cv2

cap = cv2.VideoCapture(0)

ratio = cap.get(cv2.CAP_PROP_FRAME_WIDTH) / \
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width = 400
height = int(width / ratio)

# cv2.namedWindow('frame', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (width, height))

    cv2.imshow('frame', frame)

    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
