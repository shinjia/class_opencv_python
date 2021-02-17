import cv2
import numpy as np

def saltpepper(img,n):
    m = int((img.shape[0]*img.shape[1])*n)
    for a in range(m):
        i = int(np.random.random()*img.shape[1])
        j = int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i] = 255
        elif img.ndim==3:
            img[j,i,0] = 255
            img[j,i,1] = 255
            img[j,i,2] = 255
    for b in range(m):
        i = int(np.random.random()*img.shape[1])
        j = int(np.random.random()*img.shape[0])
        if img.ndim==2:
            img[j,i] = 0
        elif img.ndim==3:
            img[j,i,0] = 0
            img[j,i,1] = 0
            img[j,i,2] = 0
    return img


img = cv2.imread('../images/lenna.jpg')
img_salt = saltpepper(img, 0.02)

cv2.imshow('salt Image', img_salt)

cv2.imwrite('../images/output.jpg', img)
print("已儲存檔案到 images/output.jpg")

cv2.waitKey(0)
cv2.destroyAllWindows()
