import cv2
import numpy as np
import matplotlib.pyplot as plt
import math

figure, axes = plt.subplots()

# Feature set containing (x,y) values of 25 known/training data
trainData = np.random.randint(0,100,(25,2)).astype(np.float32)

# Labels each one either Red or Blue with numbers 0 and 1
responses = np.random.randint(0,2,(25,1)).astype(np.float32)

# Take Red families and plot them
red = trainData[responses.ravel()==0]
plt.scatter(red[:,0],red[:,1],80,'r','^')

# Take Blue families and plot them
blue = trainData[responses.ravel()==1]
plt.scatter(blue[:,0],blue[:,1],80,'b','s')


k = 5
newcomer = np.random.randint(0,100,(1,2)).astype(np.float32)
plt.scatter(newcomer[:,0],newcomer[:,1],80,'g','o')

knn = cv2.ml.KNearest_create()
knn.train(trainData, cv2.ml.ROW_SAMPLE, responses)
ret, results, neighbours ,dist = knn.findNearest(newcomer, k)

print ("result: ", results)
print ("neighbours: ", neighbours)
print ("distance: ", dist)

x = newcomer[:,0][0]
y = newcomer[:,1][0]
r = math.sqrt(dist[0][k-1]) # unknown distance unit

circle = plt.Circle( (x, y), r , fill=False)
axes.set_aspect(1) 
axes.add_artist(circle)

plt.show()
