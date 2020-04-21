# NumPy Tutorial

import sys
import numpy as np


def run_math():
	a = np.array([1,2,3,4])
	print(a)
	print(a + 2)
	# print(a += 2)
	print(a - 2)
	print(a * 2)
	print(a / 2)
	b = np.array([1,0,1,0])
	print(a + b)
	print(a ** 2)
	print( np.sin(a) )
	print( np.cos(a) )

	# more math routines in the link


# Linear Algebra
def run_linalg():
	a = np.ones((2,3), dtype=float)
	b = np.full((3,2), 2, dtype=float)
	print(a)
	print(b)
	# matrix multiplication
	c = np.matmul(a,b)
	print(c)

	d = np.identity(99)
	# find the determinant
	print( np.linalg.det(c) )

	# eigenvalues 
	# inverse of a matrix
	# trace
	# SVD
	# norms
	# ETC


# Statistics
def run_stats():
	a = np.array([[1,2,3],[4,5,6]])
	print( np.min(a, axis=0) )
	print( np.min(a) )
	print( np.max(a, axis=1) )
	print( np.sum(a, axis=0) )





a = np.array([1,2,3])
a = np.array([1,2,3], dtype='int32')
print(a)

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])
print(b)

# get dimension
print(a.ndim)
print(b.ndim)
print(b.shape)

# get type
print(a.dtype)
print(b.dtype)

# get size
print(a.itemsize)  # output bytes

# get total size
print(a.size)
print(b.size)

print(a.nbytes)
print(b.nbytes)

# floats are usually bigger than ints of course

# access and changing rows and columns

aa = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(aa)
print(aa.shape)

# get a specific element [row, column]
print(aa[1, 5])

# get a row
print(aa[0, :])

# get a column
print(aa[:, 2])

# getting fancy [startIndex : endIndex : stepSize]
print(aa[0, 1:6:2])
print(aa[0, 1:-1:2])

# change an entry
aa[1,5] = 22
print(aa)

aa[:,2] = 5
print(aa)

aa[:,2] = [1,2]
print(aa)



# 3D example

bb = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(bb)

# get specific element (work outside in)
# get 4
print(bb[0,1,1])
print(bb[:,1,:])

# replace
bb[:,1,:] = [[9,9],[8,8]]
print(bb)



# different types of arrays

# all ZEROS
print(np.zeros(5))
print(np.zeros((2,3)))
print(np.zeros((2,3,3,2)))

print('example: ')
m = 4
n = 10
A = np.zeros((m,n))
print( A.dtype )
A[2,1] = 10.0
A[:,5] = 10.0
print( A )
print( A.dtype )

# all ONES
print(np.ones((3,6), dtype='int32'))

# init all to some other number
print( np.full((2,2), 99, dtype='float32') )

# full-like function
print( np.full(aa.shape, 4) )

# init an a matrix of random decimal numbers between 0 and 1
print( np.random.rand(4,2) )
print( np.random.rand(3,3) )
print( np.random.rand(3,3,2) )
print( np.random.random_sample(aa.shape) )

# random integer values
print( np.random.randint(7, size=(3,3)) )
print( np.random.randint(100, size=(3,3)) )
print( np.random.randint(0,7, size=(3,3)) )

# identity matrix
print( np.identity(5) )
print( np.identity(5, dtype='int16') )

# repeat an array
c = np.array([1,2,3])
r1 = np.repeat(c, 3, axis=0)
print(r1)

c = np.array([[1,2,3]])
r2 = np.repeat(c, 3, axis=0)
print(r2)


# EXAMPLE
print("\nEXAMPLE #1: ")
n = 5
B = np.zeros((n,n), dtype='int16')
B[:,0] = 1
B[:,n-1] = 1
B[0,:] = 1
B[n-1,:] = 1
B[2,2] = 9
print(B)
print(B.dtype)

# his solution
output = np.ones((5,5))
z = np.zeros((3,3))
z[1,1] = 9
print(z)
output[1:4,1:4] = z  # note that the index values are EXCLUSIVE
print(output)


# be careful when copying arrays!
a = np.array([1,2,3])
b = a
c = a.copy()
print(b)

b[0] = 100
print(b)
print("**WARNING: it changes vector a too because it's a pointer!")
print(a)
print(c)




# MATHEMATICS
run_math()
run_linalg()
run_stats()





# REORGANIZING ARRAYS
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((8,1))
print(after)

# vertical stacks
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print( np.vstack([v1,v2,v1,v2]) )

# horizontal stack
h1 = np.ones((2,4))
h2 = np.zeros((2,2))

print(np.hstack((h1,h2)))


# MISC: Load Data from File
D = np.genfromtxt('data.txt', delimiter=',')
print(D)  # auto cast to float type
D = D.astype('int32')  # convert to int type


# MISC: Advanced Indexing
# (and boolean masking)
print( D > 50 )
print( D >= 50 )
print( D[D>50] )  # index by values > 50

# you can index with a list like in MATLAB
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]])  #index with list

# which columns are greater than 50
print(np.any(D > 50, axis=0))

print(np.all(D > 50, axis=0))  # only if all values of col

print(np.all(D > 50, axis=1))  # rows

print( (D > 50) & (D < 100)  )

print( ~(D > 50) & ~(D < 100)  )


# EXAMPLE 2
A = np.ones((6,5))
subA = A[2:4, 0:2]  # note that the indexing is exclusive

print( A[[0,1,2,3], [1,2,3,4]] )

# print( A[[0,4,5], [3,4]] ) # WRONG

print( A[[0,4,5], 3:5] ) 
print( A[[0,4,5], 3: ] ) 




# end
print(sys.version)



