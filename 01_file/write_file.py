import cv2

img = cv2.imread('../images/demo.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)

print("等候按 s 鍵後存檔")
k = cv2.waitKey(0) & 0xFF
if k == 27:         # 等候按 ESC 鍵後離開
    cv2.destroyAllWindows()
elif k == ord('s'): # 等候按 s 鍵後存檔
    cv2.imwrite('output.png', img)
    cv2.destroyAllWindows()
    print("灰階影像檔案已儲存到 output.png")