import cv2
import numpy as np

# img = np.random.randint(-256, 256, size=[4,5], dtype=np.int16)

img = np.random.randint(-256, 256, size=[300,200], dtype=np.int16)
rst = cv2.convertScaleAbs(img)

print("img=\n",img)
print("rst=\n",rst)
