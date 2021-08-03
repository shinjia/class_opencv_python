import numpy as np
import cv2
import face_recognition
from PIL import Image, ImageDraw # 顯示圖片
from IPython.display import display # 顯示圖片

cap = cv2.VideoCapture(1)

#開啟照片
# Capture frame-by-frame
# ret, img = cap.read()
# print(img.shape)
# widthA, heightA = img.size
widthA, heightA = (480, 640)

#開啟眼鏡圖檔
sun = Image.open('sunglasses.png')
sun = sun.convert('RGBA')
widthB, heightB = sun.size

while True:
    # Capture frame-by-frame
    ret, image = cap.read()

    faces = face_recognition.face_locations(image, model='cnn')
    landmarks = face_recognition.face_landmarks(image, face_locations=faces) # 若沒有加 face_location，它的辨識會用 hog 的人臉數量
    # print('找到臉的數量=', len(faces))
    # for (top, right, bottom, left) in faces: #畫矩形框 可改框的顏色/線條粗細
    #     cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)

    pil_image = Image.fromarray(image) # 從np矩陣讀入圖片
    for face_landmarks in landmarks: 
        d = ImageDraw.Draw(pil_image, 'RGBA') # 人臉馬賽克 繪圖模組 

        #設定眼鏡圖檔的位置參數
        x1=face_landmarks['left_eye'][0][0]
        y1=face_landmarks['left_eye'][0][1]    
        x2=face_landmarks['right_eye'][3][0]
        y2=face_landmarks['right_eye'][3][1]

        #重設眼鏡圖檔的寬
        eye_width = x2 - x1
        newWidthB = int(eye_width * 1.55)

        #重設眼鏡圖檔的高依據新的寬度等比例縮放
        newHeightB = int(heightB/widthB*newWidthB)

        #重設眼鏡圖檔圖片
        sun_resize = sun.resize((newWidthB, newHeightB))

        #眼鏡圖片寬 高
        w, h = sun_resize.size

        #求貼圖的座標 貼圖圖片的左上角
        xy = (int((x1+x2)/2-(w/2)) ,int((y1+y2)/2-(h/2)))

        #paste() 帶有三個參數：im、box、mask
        pil_image.paste(sun_resize, xy, sun_resize)


    img = np.asarray(pil_image)

    # Display the resulting frame
    cv2.imshow('frame', img)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
