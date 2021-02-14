import numpy as np
import cv2

colormap = 0

while colormap in range(0, 20):    

    img1 = cv2.imread("../images/Gray_Level.bmp", -1)
    # img1 = cv2.imread("../images/Lenna.bmp", -1)

    img2 = cv2.applyColorMap(img1, colormap)
    
    cv2.imshow("Original Image", img1)
    cv2.imshow("Pseudocolor Image", img2)

    cv2.waitKey(1)

    print( "Pseudocolor Image Processing:")
    print( "(0) Autumn   (1) Bone     (2) Jet       (3) Winter   ")
    print( "(4) Rainbow  (5) Ocean    (6) Summer    (7) Spring   ")
    print( "(8) Cool     (9) HSV      (10) Pink     (11) Hot     ")
    print( "(12) Parula  (13) Magma   (14) Inferno  (15) Plasma  ")
    print( "(16) Viridis (17) Cividis (18) Twilight (19) Twilight Shifted")
    
    colormap = eval(input("Enter your choice: "))
