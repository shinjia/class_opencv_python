import cv2
import numpy as np
import random
import string

def random_code():
    # 隨機產生
    string.ascii_letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string.ascii_number = '012356789'  # 沒有 4
    code = ''
    for i in range(0, 3):
        code += random.choice(string.ascii_letter)
        
    for i in range(3, 7):
        code  += random.choice(string.ascii_number)
    return code


template = './plates/black_white_2014.png'
location = np.array([ [  9, 38,  54, 126],
                      [ 57, 38, 102, 126],
                      [105, 38, 150, 126],
                      [167, 38, 212, 126],
                      [215, 38, 260, 126],
                      [263, 38, 308, 126],
                      [311, 38, 356, 126] ])
                      
img = cv2.imread(template)
h, w = img.shape[0],img.shape[1]  # 155, 365

# 將車牌文字加入白色背景圖片中
# code = 'BMW8888'
code = random_code()

for i in range(0, 7):
    filename = './plates/' + code[i] + '.png'
    img_digit = cv2.imread(filename)
    x1 = location[i][0]
    y1 = location[i][1]
    x2 = location[i][2]
    y2 = location[i][3]
    # img[y1:y2, x1:x2] = (0, 255-i*30, 0)
    img[y1:y2, x1:x2] = img_digit

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
