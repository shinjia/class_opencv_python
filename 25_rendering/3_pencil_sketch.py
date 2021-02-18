import numpy as np
import cv2

def main():
    img = cv2.imread('./images/cow.jpg', -1)
    img1, img2 = cv2.pencilSketch(img)
    cv2.imshow("Original Image", img)
    cv2.imshow("Pencil Sketch 1", img1)
    cv2.imshow("Pencil Sketch 2", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def live():    
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        img1, img2 = cv2.pencilSketch( frame )

        # Display the resulting frame
        cv2.imshow('frame', frame)
        cv2.imshow( "Pencil Sketch 1", img1 )
        cv2.imshow( "Pencil Sketch 2", img2 )

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    cv2.destroyAllWindows()

main()
live()