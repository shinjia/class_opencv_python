import numpy as np
import cv2

def SIFT_feature_detection(f):
    g = cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(f, None)
    g = cv2.drawKeypoints(f, kp, g)
    return g

def main():
    img = cv2.imread("./images/blox.bmp", 0)
    img2 = SIFT_feature_detection(img)
    cv2.imshow("Original Image", img)
    cv2.imshow("SIFT Features", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()