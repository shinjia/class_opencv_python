import numpy as np
import cv2
from matplotlib import pyplot as plt

k = 3 ## 分群的數量 (2 or 3)

# 刻意明顯的三群
group1 = np.random.randint(25, 50, (25,2))
group2 = np.random.randint(60, 85, (25,2))
group3 = np.random.randint(40, 75, (25,2))
Z = np.vstack((group1, group2, group3))

# 隨機的
Z = np.random.randint(0, 100, (300,2))

# convert to np.float32
Z = np.float32(Z)
# define criteria and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
ret,label,center=cv2.kmeans(Z,k,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

# Now separate the data, Note the flatten()
A = Z[label.ravel()==0]
B = Z[label.ravel()==1]
C = Z[label.ravel()==2]

# Plot the data (group=2)
if k==2:
  plt.scatter(A[:,0],A[:,1])
  plt.scatter(B[:,0],B[:,1],c = 'r')
  plt.scatter(center[:,0],center[:,1],s = 80,c = 'y', marker = 's')
elif k==3:
  plt.scatter(A[:,0],A[:,1])
  plt.scatter(B[:,0],B[:,1],c = 'r')
  plt.scatter(C[:,0],C[:,1],c = 'g')
  plt.scatter(center[:,0], center[:,1], s = 80, c = 'y', marker = 's')

# Plot
plt.xlabel('Height'),plt.ylabel('Weight')
plt.show()