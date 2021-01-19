
import numpy as np
import sys
import time

print("This is a tutorial on the NumPy library")

# general array creation
a = np.array([0,1,2,3,4])
b = np.array([0.0, 0.5, 1.0, 1.5, 2.0])

print(a[0])  # index the same as Python list
print(a[1:])

print(b[-1])
print(b[[0,2,-1]])  # this type of indexing is different from Python lists

# data types
print(a.dtype)  # integer array
print(b.dtype)	# float array

# we can also choose the data type we want to use during array definition 
c = np.array([0,1,2,3], dtype=np.int8)
print(c.dtype)
d = np.array([0,1,2,3], dtype=np.float)
print(d.dtype)

# (usually do not use NumPy to store strings)

# create a matrix or multi-dimensional array
A = np.array([
	[1,2,3],
	[4,5,6]
	])

print(A.shape) # in 2D case, this is the mxn rows by cols
print(A.ndim)  # number of dimensions
print(A.size)  # total number of elements in the array

B = np.array([
	[
		[12, 11, 10],
		[9, 8, 7]
	],
	[
		[6, 5, 4],
		[3, 2, 1]
	]
	])

print(B.shape) # in 2D case, this is the mxn rows by cols
print(B.ndim)  # number of dimensions
print(B.size)  # total number of elements in the array


# Indexing for a Matrix
A = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
	])

# index row 1
print(A[1])
print(A[1][0])
print(A[1,0])  # this one is better for slicing
print(A[:, :2])

# overwriting elements of the array
A[1] = np.array([10,10,10])
A[2] = 99 # takes care of assigning each column's value to this scalar 
print(A)


# Summary Stats
print(a.sum())
print(a.mean())
print(a.std())
print(a.var())

# if we have a matrix, then we can do summary stats by axis (by rows or columns)
A = np.array([
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
	])
print(A)

# (full matrix stats)
print(A.sum())
print(A.mean())
print(A.std())

# (slicing using axis 0 --> stats by COLUMN)
print(A.sum(axis=0))
print(A.mean(axis=0))
print(A.std(axis=0))

print(A.sum(axis=1))
print(A.mean(axis=1))
print(A.std(axis=1))


# Broadcasting and Vectorized Operations
a = np.arange(4)
print(a)
b = a + 10  # ***vectorized: each element of a has 10 added to it
# operation is performed on EACH individual element
print(b)
c = a * 10  # this types of operations are optimized to be extremely fast
print(c)

print(a)
a += 100  # a -= 100, a *= 0.1, etc..
print(a)


# Vector Addition with NumPy Arrays
a = np.array([0, 1, 2, 3])
b = np.array([0, 10, 20, 30])
c = a + b
print(c)


# Boolean Arrays (***VERY IMPORTANT***)
a = np.arange(4)

# indexing with boolean arrays
print(a[[True, False, False, True]])

# we get a boolean array as a result too:
print(a >= 2)

# now we can use that result to index our array very easily
print(a[a >= 2])

# return values that are greater than the mean
print(a[a > a.mean()])

# same with matrices
A = np.random.randint(100, size=(3,3))
print(A)
print(A > 30)
print(A[A > 30])


# LINEAR ALGEBRA (important for ML)
B = np.array([
	[6, 5],
	[4, 3],
	[2, 1]
	])

print(A.dot(B))
print(A @ B)   # cross product
print(B.T)
print(B.T @ A)


# Size of Objects in Memory

# int, floats in NumPy versus noraml Python

print("an integer in Python is: " + str(sys.getsizeof(1)) + " bytes")
print("a long integer in Python is: " + str(sys.getsizeof(10**100)) + " bytes")

print("an int in NumPy is: " + str(np.dtype(int).itemsize) + " bytes")
print("an int8 in NumPy is: " + str(np.dtype(np.int8).itemsize) + " bytes")
print("a float in NumPy is: " + str(np.dtype(float).itemsize) + " bytes")


# Performance
n = 10000
x = list(range(n))
y = np.arange(n)

sumx = sum([xi ** 2 for xi in x]) 	#slower
sumy = np.sum(y ** 2)				#faster


# Useful Functions:
# (check the notebooks for examples and exercises)


