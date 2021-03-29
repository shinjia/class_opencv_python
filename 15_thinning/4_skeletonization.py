import numpy as np
import cv2

def skeletonization(f):
    nr, nc = f.shape[:2]
    temp = f.copy()
    g = f.copy()
    change = True
    step = 1
    while change:
        change = False
        if step == 1:
            for x in range(1, nr):
                for y in range(1, nc):
                    p = [False] * 10
                    if temp[x,y] != 0:
                        if temp[x-1,y]   != 0:  p[2] = True
                        if temp[x-1,y+1] != 0:  p[3] = True
                        if temp[x,y+1]   != 0:  p[4] = True
                        if temp[x+1,y+1] != 0:  p[5] = True
                        if temp[x+1,y]   != 0:  p[6] = True
                        if temp[x+1,y-1] != 0:  p[7] = True
                        if temp[x,y-1]   != 0:  p[8] = True
                        if temp[x-1,y-1] != 0:  p[9] = True
                        N = 0
                        for k in range(2, 10):
                            if p[k] == True:
                                N += 1	
                        T = 0
                        for k in range(2, 9):
                            if p[k] == False and p[k + 1] == True:
                                T += 1
                        if p[9] == False and p[2] == True:
                            T += 1
                        if ((N >= 2 and N <= 6) and (T == 1) and 
                           ((p[2] and p[4] and p[6]) == False) and 
                           ((p[4] and p[6] and p[8]) == False)):
                            g[x,y] = 0
                            change = True
        if step == 2:
            for x in range(1, nr):
                for y in range(1, nc):
                    p = [False] * 10
                    if temp[x,y] != 0:
                        if temp[x-1,y]   != 0:  p[2] = True
                        if temp[x-1,y+1] != 0:  p[3] = True
                        if temp[x,y+1]   != 0:  p[4] = True
                        if temp[x+1,y+1] != 0:  p[5] = True
                        if temp[x+1,y]   != 0:  p[6] = True
                        if temp[x+1,y-1] != 0:  p[7] = True
                        if temp[x,y-1]   != 0:  p[8] = True
                        if temp[x-1,y-1] != 0:  p[9] = True
                        N = 0
                        for k in range(2, 10):
                            if p[k] == True:
                                N += 1	
                        T = 0
                        for k in range(2, 9):
                            if p[k] == False and p[k + 1] == True:
                                T += 1
                        if p[9] == False and p[2] == True:
                            T += 1
                        if ((N >= 2 and N <= 6) and (T == 1) and 
                           ((p[2] and p[4] and p[8] ) == False) and 
                           ((p[2] and p[6] and p[8] ) == False)):
                            g[x,y] = 0
                            change = True
        temp = g.copy()
        if step == 1:  step = 2
        else:          step = 1
    return g

def main():
    img  = cv2.imread("./images/abc.bmp", -1)
    img2 = skeletonization(img)
    cv2.imshow("Original Image", img)
    cv2.imshow("Skeletonization", img2)
    cv2.waitKey(0)

main()