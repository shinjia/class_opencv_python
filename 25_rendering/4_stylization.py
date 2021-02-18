import numpy as np
import cv2

def main():
    img1 = cv2.imread('./images/cow.jpg', -1)
    img2 = cv2.stylization(img1)
    cv2.imshow("Original Image", img1)
    cv2.imshow("Stylization", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def live():    
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        img2 = cv2.stylization(frame)

        # Display the resulting frame
        cv2.imshow('frame', frame)
        cv2.imshow( "Stylization", img2 )

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

main()
live()
