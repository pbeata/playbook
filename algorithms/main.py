
# print("\nhello world")
# print "this is just a test", 42


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
		print "Guess #", k, "  ", value
		
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
print index

target2 = 10
index = binarySearch(primes, n, target2)
print index

target3 = 73
index = binarySearch(primes, n, target3)
print index
