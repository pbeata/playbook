
import numpy as np

# checking pass-by-reference for list and array

def myFunc(myList):
	myList[0] = 42
	print(myList)

def updateArray(myArray):
	myArray[0] = 42
	print(myArray)


# STANDARD LIST
a = [1, 2, 3, 4]
print(a)
myFunc(a)
print(a)

# NUMPY ARRAY
b = np.array([1, 2, 3, 4], dtype='int32')
print(b)
updateArray(b)
print(b)


print(b.dtype)
