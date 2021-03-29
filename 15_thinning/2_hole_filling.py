import numpy as np
import cv2

def hole_filling(f):
    g = f.copy()
    nr, nc = f.shape[:2]
    negative = 255 - f
    n, labels = cv2.connectedComponents(negative)
    for x in range(nr):
        for y in range(nc):
            if labels[x,y] > 1:
                g[x,y] = 255
    return g

def main():
    img  = cv2.imread("./images/abc.bmp", -1)
    img2 = hole_filling(img)
    cv2.imshow("Original Image",  img)
    cv2.imshow("Hole Filling", img2)
    cv2.waitKey(0)

main()