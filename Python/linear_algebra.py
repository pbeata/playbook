
'''

LINEAR ALGEBRA TOOLKIT

LU Decomposition
Gaussian Elimination

1. Implement my own versions of LU and GE (+PP)
2. Compare with results from built-in linear algebra packages
3. Do performance testing in Linux
4. Use various sizes of n to observe accuracy/performance
5. Investigate sparse methods   

'''

import numpy as np
import matplotlib.pyplot as plt

n = 4
c = 1.0

A = c * np.random.rand(n,n)
x = np.random.rand(n)
# x = np.ones((n,1))

b = np.matmul(A,x)
print(A)
print(x)
print(b)

# print(A.dtype)


