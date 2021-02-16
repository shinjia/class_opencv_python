import numpy as np

x3 = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )

x5 = np.array( [ [ 1,  2,  3,  4,  5], 
                 [ 6,  7,  8,  9, 10],
                 [11, 12, 13, 14, 15],
                 [16, 17, 18, 19, 20],
                 [21, 22, 23, 24, 25] ] )

y1 = np.flip(x3)
y2 = np.rot90(x3, 2)

print("x3 =\n", x3)
print("y1 =\n", y1)
print("y2 =\n", y2)


y1 = np.flip(x5)
y2 = np.rot90(x5, 2)

print("-------------------------------")
print("x5 =\n", x5)
print("y1 =\n", y1)
print("y2 =\n", y2)
