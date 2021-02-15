import numpy as np
import cv2

def apply_kernel(img, kernel): 
    return np.sum(np.multiply(img, kernel)) 

def naive_correlation(image, kernel):
    image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
    image_padded[1:-1, 1:-1] = image
    out = np.zeros_like(image)
    for x in range(image.shape[1]):
        for y in range(image.shape[0]):
            # out[y, x] = (kernel * image_padded[y:y + 3, x:x + 3]).sum()
            out[y, x] = apply_kernel(image_padded[y:y + 3, x:x + 3], kernel)
    return out
    
x = np.array( [ [1, 1, 1], [1, 1, 1], [1, 1, 1] ] )
h = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )

y1 = naive_correlation(x, h)
y2 = naive_correlation(x, np.flip(h))

print("x =")
print(x)
print("h =")
print(h)
print("Correlation y1 =")
print(y1)
print("Convolution y2 =")
print(y2)

# [[12 21 16]
#  [27 45 33]
#  [24 39 28]]