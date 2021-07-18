import numpy as np
import cv2

def ripple_effect(f, method, amplitude, period):
	nr, nc = f.shape[:2]
	map_x = np.zeros([nr, nc], dtype = 'float32')
	map_y = np.zeros([nr, nc], dtype = 'float32')
	x0, y0 = nr // 2, nc // 2
	for x in range(nr):
		for y in range(nc):
			if method == 1:		# x-direction
				xx = np.clip(x + amplitude * np.sin(x / period), 0, nr - 1)
				map_x[x,y] = y
				map_y[x,y] = xx
			elif method == 2:	# y-direction
				yy = np.clip(y + amplitude * np.sin(y / period), 0, nc - 1)
				map_x[x,y] = yy
				map_y[x,y] = x
			elif method == 3:	# x & y direction
				xx = np.clip(x + amplitude * np.sin(x / period), 0, nr - 1)
				yy = np.clip(y + amplitude * np.sin(y / period), 0, nc - 1)
				map_x[x,y] = yy
				map_y[x,y] = xx
			else:				# Radial
				r = np.sqrt((x - x0) ** 2 + (y - y0) ** 2)
				if r == 0:  theta = 0
				else:		theta = np.arccos((x - x0) / r)
				r = r + amplitude * np.sin(r / period)
				if y - y0 < 0:  theta = -theta
				map_x[x,y] = np.clip(y0 + r * np.sin(theta), 0, nc - 1)
				map_y[x,y] = np.clip(x0 + r * np.cos(theta), 0, nr - 1)
	g = cv2.remap(f, map_x, map_y, cv2.INTER_LINEAR)
	return g

def main():
	img1 = cv2.imread('./images/snow_mountain.bmp', -1)
	img2 = ripple_effect(img1, 1, 5, 2)
	cv2.imshow("Original Image", img1)
	cv2.imshow("Ripple Effect", img2)
	cv2.waitKey(0)

main()