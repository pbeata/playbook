
import numpy as np

# print("\nhello world")
# print "this is just a test", 42


def findMinValue(inArray, arraySize, index1, index2):
	minVal = inArray[index1]
	minIndex = index1
	for i in range(index1 + 1, index2):
		if (inArray[i] < minVal):
			minVal = inArray[i]
			minIndex = i
	# print("min global index: ", minIndex)
	# return minVal
	return minIndex


def swapValues(inArray, arraySize, index1, index2):
	if ( 0 <= index1 and index1 < arraySize ):
		temp = inArray[index1]
		if ( 0 <= index2 and index2 < arraySize ):
			inArray[index1] = inArray[index2]
			inArray[index2] = temp;
		else:
			print("out of bounds error")
	else:
		print("out of bounds error")



# Binary Search Function
# 	input: (array of integers, size of array, target value)
# 	output:	index of target OR -1 if target is not found in array
def binarySearch(inArray, arraySize, findValue):
	iMin = 0
	iMax = arraySize - 1

	k = 0
	while True:
		if (iMax < iMin):
			# target value is not in the array
			return -1
		
		guess = (iMin + iMax) // 2	# this is the FLOOR division operator
		value = inArray[guess]

		k = k + 1
		print("Guess #", k, "  ", value)
		
		if (value == findValue):
			return guess
		elif (value < findValue):
			iMin = guess + 1
		else:
			iMax = guess - 1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
n = len(primes)

target1 = 67
index = binarySearch(primes, n, target1)
print (index)

target2 = 10
index = binarySearch(primes, n, target2)
print (index)

target3 = 73
index = binarySearch(primes, n, target3)
print (index)




A = np.array([22.0, 34.2, 1.2, 3.0, 77.2])
n = int((A.shape)[0])

print(A) 
swapValues(A, n, 2, 4)
print(A)


cards = [13, 19, 18, 4, 10]
m = len(cards)
print(cards)
print( np.arange(0, m) )
k = findMinValue(cards, m, 0, m)

print("==========")

print(cards)
for i in range(0, m):
	k = findMinValue(cards, m, i, m)
	# print("min card value: ", minCard)
	swapValues(cards, m, i, k)
	print(cards)

