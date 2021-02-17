import numpy as np
import cv2

def shape_feature(f, method):
	nr, nc = f.shape[:2]
	if method == 1:    # Area
		return np.count_nonzero(f)
	if method == 2:    # Geometric Center
		nr, nc = f.shape[:2]
		xc = yc = 0
		area = 0
		for x in range(nr):
			for y in range(nc):
				if f[x,y] != 0:
					xc += x
					yc += y
					area += 1
		xc /= area
		yc /= area
		return xc, yc
	if method == 3:    # Compactness
		area = 0
		p = 0
		for x in range(1, nr - 1):
			for y in range(1, nc -1):
				if f[x,y] != 0:
					area += 1	
					if ( f[x-1,y] == 0 or f[x+1,y] == 0 or
					   f[x,y-1] == 0 or f[x+1,y] == 0):
						p += 1
		return (p * p) / area	
	if method == 4:    # Circularity
		area = shape_feature(f, 1)
		xc, yc = shape_feature(f, 2)
		radius = np.sqrt(area / np.pi)
		n = 0
		for x in range(nr):
			for y in range(nc):
				if f[x,y] != 0:
					if (x - xc) ** 2 + (y - yc) ** 2 \
                       < radius * radius:
					   n += 1
		return n / area
	return 0

def extract_object(f, label):
	n, labels = cv2.connectedComponents(f)
	g = f.copy()
	nr, nc = f.shape[:2]
	for x in range(nr):
		for y in range(nc):
			if labels[x,y] == label:
				g[x,y] = 255
			else:
				g[x,y] = 0
	return g			

def main():
	number = eval(input("Please Object No. = "))
	img1 = cv2.imread("./images/shapes.bmp", -1)
	img2 = extract_object(img1, number)
	area = shape_feature(img2, 1)
	xc, yc = shape_feature(img2, 2)
	compactness = shape_feature(img2, 3)
	circularity = shape_feature(img2, 4)	
	print("Area =", area)
	print("Geometric Center =", xc, ",", yc)
	print("Compactness =", compactness)
	print("Circularity =", circularity)
	cv2.imshow("Original Image",  img1)
	cv2.imshow("Extracted Object", img2)	
	cv2.waitKey(0)
	cv2.destroyAllWindows()

main()