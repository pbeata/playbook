# generate n random points in 3D
import numpy as np

n = 164
x = np.random.uniform(size=n)
y = np.random.uniform(size=n)
z = np.random.uniform(size=n)
w = np.random.uniform(size=n)

for i in range(0, n):
  # print( "%d %f %f %f" % (i+1, x[i], y[i], z[i]) )
  print( "%d %f %f %f %f" % (i+1, x[i], y[i], z[i], w[i] + 1.0) )
