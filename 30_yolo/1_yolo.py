# YOLO object detection
import cv2
import numpy as np
import time

img = cv2.imread('images/horse.jpg')
cv2.imshow('window',  img)
cv2.waitKey(1)

# Give the configuration and weight files for the model and load the network.
net = cv2.dnn.readNetFromDarknet('yolov3.cfg', 'yolov3.weights')
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
# net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

ln = net.getLayerNames()
print(len(ln), ln)

# construct a blob from the image
blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), swapRB=True, crop=False)
r = blob[0, 0, :, :]

cv2.imshow('blob', r)
text = f'Blob shape={blob.shape}'
# cv2.displayOverlay('blob', text)
cv2.waitKey(1)

net.setInput(blob)
t0 = time.time()
outputs = net.forward(ln)
t = time.time()

# cv2.displayOverlay('window', f'forward propagation time={t-t0}')
cv2.imshow('window',  img)
cv2.waitKey(0)
cv2.destroyAllWindows()