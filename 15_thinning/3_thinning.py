import numpy as np
import cv2

def thinning(f):
    B1 = np.array([[-1, -1, -1], [0, 1, 0], [1, 1, 1]])
    B2 = np.array([[0, -1, -1], [1, 1, -1], [1, 1, 0]])
    B3 = np.array([[1, 0, -1], [1, 1, -1], [1, 0, -1]])
    B4 = np.array([[1, 1, 0], [1, 1, -1], [0, -1, -1]])
    B5 = np.array([[1, 1, 1], [0, 1, 0], [-1, -1, -1]])
    B6 = np.array([[0, 1, 1], [-1, 1, 1], [-1, -1, 0]])
    B7 = np.array([[-1, 0, 1], [-1, 1, 1], [-1, 0, 1]])
    B8 = np.array([[-1, -1, 0], [-1, 1, 1], [0, 1, 1]])
    g  = f.copy()
    g2 = f.copy()
    change = True
    while change:
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B1)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B2)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B3)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B4)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B5)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B6)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B7)
        g = g - temp
        temp = cv2.morphologyEx(g, cv2.MORPH_HITMISS, B8)
        g = g - temp
        if np.array_equal(g, g2):
            change = False
        else:
            g2 = g.copy()
            change = True		
    return g

def main():
    img  = cv2.imread("./images/abc.bmp", -1)
    img2 = thinning(img)
    cv2.imshow("Original Image",  img)
    cv2.imshow("Thinning", img2)
    cv2.waitKey(0)

main()