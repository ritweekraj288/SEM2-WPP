#Take N (N >= 10) random 2-dimensional points represented in cartesian coordinate space.Store them in a numpy array. Convert them to polar coordinates.



import numpy as np
import random 
N = int(input("Enter the number of points"))
points = np.random.randn(N,2)
print("Cartesian Points :",points)
x = points[:,0]
y = points[:,1]
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y,x)
polar = np.column_stack((r,theta))
print("Polar points :",polar)