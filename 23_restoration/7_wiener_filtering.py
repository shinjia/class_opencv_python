import numpy as np
import cv2
from numpy.fft import fft2, ifft2

def gaussian_lowpass(f, cutoff):
	nr, nc = f.shape[:2]	

	fp = np.zeros([nr, nc])				# 前處理
	for x in range(nr):
		for y in range(nc):
			fp[x,y] = pow(-1, x + y) * f[x,y]
	
	F = fft2(fp)							# 離散傅立葉轉換
	G = F.copy()
	
	for u in range(nr):
		for v in range(nc):
			dist = np.sqrt((u - nr / 2) * (u - nr / 2) +
			                (v - nc / 2) * (v - nc / 2))
			H = np.exp(-(dist * dist) / (2 * cutoff * cutoff))
			G[u,v] *= H	
					
	gp = ifft2(G)							# 反離散傅立葉轉換

	gp2 = np.zeros([nr, nc])			# 後處理
	for x in range(nr):
		for y in range(nc):
			gp2[x,y] = round(pow(-1, x + y) * np.real(gp[x,y]), 0)
	g = np.uint8(np.clip(gp2, 0, 255))

	return g

def wiener_filtering(f, cutoff, K):
	nr, nc = f.shape[:2]	

	fp = np.zeros([nr, nc])				# 前處理
	for x in range(nr):
		for y in range(nc):
			fp[x,y] = pow(-1, x + y) * f[x,y]
	
	F = fft2(fp)							# 離散傅立葉轉換
	G = F.copy()
	
	for u in range(nr):					# 維納濾波
		for v in range(nc):
			dist = np.sqrt((u - nr / 2) * (u - nr / 2) +
			                (v - nc / 2) * (v - nc / 2))
			H = np.exp(-(dist * dist) / (2 * cutoff * cutoff))
			H = H / (H * H + K)
			G[u,v] *= H
					
	gp = ifft2(G)								# 反離散傅立葉轉換

	gp2 = np.zeros([nr, nc])				# 後處理
	for x in range(nr):
		for y in range(nc):
			gp2[x,y] = round(pow(-1, x + y) * np.real(gp[x,y]), 0)
	g = np.uint8(np.clip(gp2, 0, 255))

	return g

def main():
	img1 = cv2.imread("images/Brunch.bmp", 0)
	img2 = gaussian_lowpass(img1, 50)
	img3 = wiener_filtering(img2, 50, 0.05)
	cv2.imshow("Original Image", img1)
	cv2.imshow("Lowpass Image", img2)
	cv2.imshow("Wiener Filtering", img3)
	cv2.waitKey(0)

main()