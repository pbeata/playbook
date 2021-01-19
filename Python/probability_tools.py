
import numpy as np


# flip a two-sided coin one time
def coin_flip():
	flip = np.random.rand(1, 1)[0]
	# print(flip)
	if (flip < 0.5):
		value = "heads"
	else:
		value = "tails"
	return value

# compute n! (n factorial)
def my_factorial(n):
	if (n < 0):
		print("***Error: to use the factorial factorial, N must not be negative!")
		return -1
	elif (n == 0):
		return 1
	else:
		result = n * my_factorial(n-1)
		return result

# Variations with repitions
def computeVRep(n, p):
	return (n ** p)

# Variations without repitions
def computeV(n, p):
	top = my_factorial(n)
	bot = my_factorial(n - p)
	return int(top / bot)




#==========================================================
# MAIN

print("\n")

# Flip a coin: result is either heads or tails
x = coin_flip()
print("Your test flip returned " + x + ".")

# Flip a coin N times to compute experimental probability 
numTrials = 2 ** 12
expectedValue = "heads"
count = 0
for i in range(0, numTrials):
	x = coin_flip()
	if (x == expectedValue):
		count += 1

experimentalProbability = float(count) / numTrials
print("The experimental probability after " + str(numTrials) + " coin flips is "
 + str(experimentalProbability))

# Factorials
print("Testing my_factorial function with various N values: ")
print(my_factorial(-1))
print(my_factorial(0))
print(my_factorial(1))
print(my_factorial(2))
print(my_factorial(3))
print(my_factorial(4))
print(my_factorial(5))
print(my_factorial(6))

# Variations with repitions
numSlots = 4;
possibleLetters = ['P', 'A', 'S', 'W', 'O', 'R', 'D']
# possibleLetters = ['A', 'B', 'C']
numLetters = len(possibleLetters)
numPasswords = computeVRep(numLetters, numSlots)
print("\nnumber of possible password combinations with repitions: " + str(numPasswords))

# Variations without repitions
numPositions = 4;
playerList = ['11', '16', '5', '52', '23']#, '91', '70', '3']
numPlayers = len(playerList)
numLineCombos = computeV(numPlayers, numPositions)
print("number of possible line combinations without repitions: " + str(numLineCombos))

print("\n")

