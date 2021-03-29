import numpy as np
import cv2

def harris_corner_detection(f):
    g = cv2.cvtColor(f, cv2.COLOR_GRAY2BGR)
    gray = np.float32(f)
    dst = cv2.cornerHarris(gray, 2, 3, 0.04)
    # cv2.imshow("dst", dst)

    nr, nc = f.shape[:2]
    for x in range(nr):
        for y in range(nc):
            if dst[x,y] > 0.1 * dst.max():
                cv2.circle(g, (y,x), 2, [255,0,0], 2)
    return g

def main():
    img = cv2.imread("./images/blox.bmp", 0)
    img2 = harris_corner_detection(img)
    cv2.imshow("Original Image", img)
    cv2.imshow("Harris Corners", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

main()