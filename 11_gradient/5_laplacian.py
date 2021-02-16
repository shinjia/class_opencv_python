import cv2

# img = cv2.imread('./images/Laplacian.bmp', cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('../images/lenna_gray.bmp', cv2.IMREAD_GRAYSCALE)
img = cv2.imread('../images/osaka.bmp', cv2.IMREAD_GRAYSCALE)

Laplacian = cv2.Laplacian(img, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)   

cv2.imshow("original", img)
cv2.imshow("Laplacian", Laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
