
# import the math module so we can use more functions
from math import *


# print statement
print("hello world")
print("draw a triangle: ")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

# variables (strings)
character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old.")

# update variable
character_name = "Paul"

print("He really like the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

# storing a number
my_age = 30
his_age = 29.88

# strings, integers, floating point numbers, and boolean operators
is_male = True

# WORKING WITH STRINGS

print("Hippo Academy")
print("Hippo\nAcademy")
print("\"Hippo\"Academy")

phrase = "Hippo Academy"
print(phrase)

# concatenate
print(phrase + " is the top rated zoo school in the US")

print(phrase.lower())
print(phrase.upper())

# check if upper
print(phrase.isupper())
print(phrase.upper().isupper())

# lenght of string
print(len(phrase))

# access characters in the string

# phrase = "Hippo Academy"
#           0123456789012

print(phrase[0])  # Python is 0-based

# index function
print(phrase.index("A"))
print(phrase.index("Acad"))

# throws an error if index value does not exist
# print(phrase.index("Z"))

print(phrase.replace("Hippo", "Hot Dog"))


# WORKING WITH NUMBERS
print(3 + 4.5)
print(3 * 4.5)
print(3 * 4 + 5)
print(3 * (4 + 5))

# 10 mod 3 --> 10/3 and print remainder 1
print(10 % 3)

x = 5
print(x)
print(str(x))
print(str(x) + " is my fave number")

y = -10
print(abs(y))

print(pow(3,3))
print(pow(x, y))

print(max(4,6))
print(min(4,6))

print(round(4.22))
print(round(4.82))

print(floor(3.7))
print(ceil(3.7))

print(sqrt(36))
print(sqrt(36.22))


'''
# USER INPUT
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old.")

# CALCULATOR
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

result = num1 + num2  # wrong! this adds the STRINGS
print(result)

result = int(num1) + int(num2)  # only works if input is INT
print(result)

result = float(num1) + float(num2)  # in order to accept FP input
print(result)
'''


# WORKING WITH LISTS
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends)
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[-1])
print(friends[1:])
print(friends[1:4])

friends[1] = "Mike"
print(friends)




# tuples: you cannot change it once you create it
my_tuple = ('Paul', 30, 175.5, False)
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])

# dictionary reminds me of a C/C++ struct data type
# key value mapping type

user = {
	"name": "Paul A. Beata",
	"email": "pbeata@live.com",
	"age": 30,
	"subscribed": True 
}

# access the values by the key name
print(user['name'])
print('age' in user)
print('last_name' in user)
print(user)

# sets and dictionaries are unordered data structures

# sets are a bag that contain elements in any order
my_set = {3, 1, 5, 7, 3, 2, 6, 9, 3}
print(my_set)
print("note that the set only has unique values")

# special feature is the membership operation
print(3 in my_set)
print(0 in my_set)

# SETS ARE VERY USEFUL FOR WHEN YOU ARE CHECKING FOR MEMBERSHIP

# iterating through collections

evens = [0, 2, 4, 6, 8]
for x in evens:
	print(x)

# default for dictionary iteration is by KEY
for key in user:
	print(key.title(), ' ==> ', user[key])


# .. but you can also switch to iterated by values:
for val in user.values():
	print(val)

# ... or you can iterate over both key and value with items:
for key, value in user.items():
	print(key, value)

for i in range(5):
	print(i)

# MODULES

import random
a = random.randint(0, 99)
print(a)

# EXCEPTIONS

age = "18"
try:
	if age > 21:
		print("you are allowed to enter")
except TypeError:
	print("the variable \'age\' is probably of the wrong type: check type = " + str(type(age)))



