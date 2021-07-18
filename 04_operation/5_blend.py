import numpy as np
import cv2

# main program

# 讀入圖像並顯示 (注意格式是 BGR)
img1 = cv2.imread('./images/blend_landscape.jpg', -1)
img2 = cv2.imread('./images/blend_man.jpg', -1)

blend1 = cv2.bitwise_and(img1, img2)
blend2 = cv2.bitwise_or(img1, img2)
blend3 = cv2.bitwise_xor(img1 ,img2)
blend4 = cv2.add(img1, img2)
blend5 = cv2.addWeighted(img1, 0.3, img2, 0.7, 0)
blend6 = cv2.subtract(img1, img2)
blend7 = cv2.subtract(img2, img1)

cv2.imshow('bitwise_and', blend1)
cv2.imshow('bitwise_or', blend2)
cv2.imshow('bitwise_xor', blend3)
cv2.imshow('add', blend4)
cv2.imshow('addWeighted', blend5)
cv2.imshow('subtract1', blend6)
cv2.imshow('subtract2', blend7)
cv2.waitKey(0)
