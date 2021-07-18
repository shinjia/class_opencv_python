import numpy as np
import cv2

img = cv2.imread("../images/lenna.jpg", -1)


# RGB
imgRGB = img
(b, g, r) = cv2.split(imgRGB)
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
# Merge every channel
resultRGB = cv2.merge((bH, gH, rH))

# YUV
imgYUV = cv2.cvtColor(imgRGB, cv2.COLOR_BGR2YCrCb)
channelsYUV = cv2.split(imgYUV)
channelsYUV[0] = cv2.equalizeHist(channelsYUV[0])  # 只對 Y Channel
# Merge every channel
channels = cv2.merge(channelsYUV)
resultYUV = cv2.cvtColor(channels, cv2.COLOR_YCrCb2BGR)


cv2.imshow("Original Image", img)
cv2.imshow("RGB Equalization", resultRGB)
cv2.imshow("YUV Equalization", resultYUV)
cv2.waitKey(0)