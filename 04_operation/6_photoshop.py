import numpy as np
import cv2

# 不透明度
def Transparent(img_1, img_2, alpha):
    img = img_1 * alpha + img_2 * (1-alpha)
    return img

# 正片疊底
def Multiply (img_1, img_2):
    img = img_1 * img_2
    return img

# 颜色加深 
def Color_burn (img_1, img_2):
    img = 1 - (1 - img_2) / (img_1 + 0.001)

    mask_1 = img  < 0 
    mask_2 = img  > 1

    img = img * (1-mask_1)
    img = img * (1-mask_2) + mask_2

    '''
    row, col, channel = img.shape
    for i in range(row):
        for j in range(col):
            img[i, j, 0] = min(max(img[i, j, 0], 0), 1)
            img[i, j, 1] = min(max(img[i, j, 1], 0), 1)
            img[i, j, 2] = min(max(img[i, j, 2], 0), 1)
    '''
    return img

# 颜色减淡
def Color_dodge(img_1, img_2):
    img = img_2 / (1.0 - img_1 + 0.001)
    mask_2 = img  > 1
    img = img * (1-mask_2) + mask_2          
    return img 

# 線性加深 
def Linear_burn(img_1, img_2):
    img = img_1 + img_2 - 1
    mask_1 = img  < 0 
    img = img * (1-mask_1)
    return img

# 線性减淡
def Linear_dodge(img_1, img_2):
    img = img_1 + img_2
    mask_2 = img  > 1
    img = img * (1-mask_2) + mask_2
    return img

# 變亮
def Lighten(img_1, img_2):
    img = img_1 - img_2
    mask = img > 0
    img = img_1 * mask + img_2 * (1-mask) 

    return img 

# 變暗
def Dark(img_1, img_2):
    img = img_1 - img_2
    mask = img < 0
    img = img_1 * mask + img_2 * (1-mask) 
    return img 

# 濾色
def Screen(img_1, img_2):
    img = 1- (1-img_1)*(1-img_2)
    return img

# 疊加
def Overlay(img_1, img_2):
    mask = img_2 < 0.5
    img = 2 * img_1 * img_2 * mask + (1-mask) * (1- 2 * (1-img_1)*(1-img_2))
    return img

# 柔光
def Soft_light(img_1, img_2):
    mask = img_1 < 0.5
    T1 = (2 * img_1 -1)*(img_2 - img_2 * img_2) + img_2
    T2 = (2 * img_1 -1)*(np.sqrt(img_2) - img_2) + img_2
    img = T1 * mask + T2 * (1-mask)
    return img

# 强光
def Hard_light(img_1, img_2):
    mask = img_1 < 0.5
    T1 = 2 * img_1 * img_2
    T2 = 1 - 2 * (1 - img_1) * (1 - img_2)
    img = T1 * mask + T2 * (1-mask)
    return img

# 亮光
def Vivid_light(img_1, img_2):
    mask = img_1 < 0.5
    T1 = 1 - (1 - img_2)/(2 * img_1 + 0.001)
    T2 = img_2 / (2*(1-img_1) + 0.001)
    mask_1 = T1 < 0
    mask_2 = T2 > 1
    T1 = T1 * (1-mask_1)
    T2 = T2 * (1-mask_2) + mask_2
    img = T1 * mask  + T2 * (1 - mask)
    return img 

# 點光
def Pin_light(img_1, img_2):
    mask_1 = img_2 < (img_1 * 2 -1)
    mask_2 = img_2 > 2 * img_1
    T1 = 2 * img_1 -1 
    T2 = img_2
    T3 = 2 * img_1 
    img = T1 * mask_1 + T2 * (1 - mask_1) * (1 - mask_2) + T3 * mask_2
    return img

# 線性光
def Linear_light(img_1, img_2):
    img = img_2 + img_1 * 2 - 1
    mask_1 = img < 0
    mask_2 = img > 1
    img = img * (1-mask_1)
    img = img * (1-mask_2) + mask_2
    return img

# 實色混合
def Hard_mix(img_1, img_2):
    img = img_1 + img_2 
    mask = img_1 + img_2 > 1 
    img = img * (1-mask) + mask 
    img = img * mask
    return img

import math

# main program

# 讀入圖像並顯示 (注意格式是 BGR)
img1 = cv2.imread('./images/blend_landscape.jpg', -1)
img2 = cv2.imread('./images/blend_man.jpg', -1)

img_1 = img1 / 255.0
img_2 = img2 / 255.0
alpha = 0.5


img = Transparent(img_1, img_2, alpha)  # 不透明度
# img = Multiply (img_1, img_2)  # 正片疊底
# img = Color_burn(img_1, img_2)  # 颜色加深 
# img = Color_dodge(img_1, img_2)  # 颜色减淡
# img = Linear_burn(img_1, img_2)  # 線性加深
# img = Linear_dodge(img_1, img_2)  # 線性减淡
# img = Lighten(img_1, img_2)  # 變亮
# img = Dark (img_1, img_2)  # 變暗
# img = Screen(img_1, img_2)  # 濾色
# img = Overlay(img_1, img_2)  # 疊加
# img = Soft_light(img_1, img_2)  # 柔光
# img = Hard_light(img_1, img_2)  # 强光
# img = Vivid_light(img_1, img_2)  # 亮光
# img = Pin_light(img_1, img_2)  # 點光
# img = Linear_light(img_1, img_2)  # 線性光
# img = Hard_mix(img_1, img_2)  # 實色混合

cv2.imshow('Blend', img)
cv2.waitKey(0)
