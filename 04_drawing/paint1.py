import cv2
import numpy as np

# mouse callback function
def draw_circle(event,x,y,flags,param):
    # if event == cv2.EVENT_LBUTTONDBLCLK:
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),-1)
    elif event == cv2.EVENT_MOUSEMOVE:
        cv2.circle(img,(x,y),5,(0,0,255),-1)

# Create a black image, a window and bind the function to window
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()
