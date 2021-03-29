import numpy as np
import cv2
import matplotlib.pyplot as plt 

def image_negative(f):
	g = 255 - f
	return g

def main():
	img = cv2.imread('./images/messi5.jpg', -1)
	img2 = image_negative(img)
	cv2.imshow('Original Image', img)
	cv2.imshow('Image Negative', img2)	
	
	color = ('b', 'g', 'r') 
	for i, col in enumerate(color): 
		histr = cv2.calcHist([img], [i], None, [256], [0, 256]) 
		plot1 = plt.figure(1)
		plt.plot(histr, color = col) 
		plt.xlim([0, 256]) 
		
		histr = cv2.calcHist([img2], [i], None, [256], [0, 256]) 
		plot2 = plt.figure(2)
		plt.plot(histr, color = col) 
		plt.xlim([0, 256]) 
		
	plt.show()
	cv2.waitKey(0)

main()
