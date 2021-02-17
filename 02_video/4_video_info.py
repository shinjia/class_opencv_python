import cv2

cap = cv2.VideoCapture(0)

# 解析 Fourcc 格式資料的函數
def decode_fourcc(v):
  v = int(v)
  return "".join([chr((v >> 8 * i) & 0xFF) for i in range(4)])

# 取得影像的尺寸大小
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print('Image Size: %d x %d' % (width, height))

# 取得 Codec 名稱
fourcc = cap.get(cv2.CAP_PROP_FOURCC)
codec = decode_fourcc(fourcc)
print('Codec: ' + codec)

## 更多資訊
brightness = cap.get(cv2.CAP_PROP_BRIGHTNESS)
contrast   = cap.get(cv2.CAP_PROP_CONTRAST)
saturation = cap.get(cv2.CAP_PROP_SATURATION)
hue        = cap.get(cv2.CAP_PROP_HUE)
gain       = cap.get(cv2.CAP_PROP_GAIN)
exposure   = cap.get(cv2.CAP_PROP_EXPOSURE)

print('brightness: ', brightness)
print('contrast  : ', contrast)
print('saturation: ', saturation)
print('hue       : ', hue)
print('gain      : ', gain)
print('exposure  : ', exposure)

# When everything done, release the capture
cap.release()
