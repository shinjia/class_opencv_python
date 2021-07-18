import numpy as np
import cv2

# 矩形
rect = np.zeros((300, 300), dtype='uint8')
cv2.rectangle(rect, (25, 25), (275, 275), 255, -1)

# 圓形
circle = np.zeros((300, 300), dtype='uint8')
cv2.circle(circle,(150, 150), 150, 255, -1)

# Not, And, Or, Xor
bitwiseNOT = cv2.bitwise_not(circle)
bitwiseAND = cv2.bitwise_and(rect, circle)
bitwiseOR = cv2.bitwise_or(rect, circle)
bitwiseXOR = cv2.bitwise_xor(rect ,circle)


cv2.imshow('Rect', rect)
cv2.imshow('Circle', circle)
cv2.imshow('bitwiseNOT', bitwiseNOT)
cv2.imshow('bitwiseAND', bitwiseAND)
cv2.imshow('bitwiseOR', bitwiseOR)
cv2.imshow('bitwiseXOR', bitwiseXOR)
cv2.waitKey(0)
