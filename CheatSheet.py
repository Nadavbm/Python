""" One line comment start with #
multi line with """

# Import libraries:
import string
import math

# Python functions:
def main():
    print("Hello World")

main()

# Using input and print:
def vorname():
    first_name = raw_input('Enter your name: ')
    print("Hello " + first_name)

vorname()

# Python data-types: integer, float, complex, string, boolean
# Variables:
x = 3
str = "Hello"
# Define three variables at once:
count, result, total = 0, 0, 0
# Add 1 or minus 1:
count += 1
# All assignment operators: += , -= , *= , /= , %=
# Determine the type of a variable:
print(type(1))
print(type("a"))
print(type(2+3j))

# Using strings:
name = "Nadav"
age = 35
print("Hello! My name is %s." % name)
print("Hello! My name is %s and I am %d years old." % (name, age))
print('This is one line.\nThis is another line.')
"""
\\ literal backslash
\' single quote
\" double quote
\n newline
\t tab
"""
name = "Shipudei Afuli"
print(len(name)) # Find the length of a string with the built-in len functio
print(name.lower()) # Print the string converted to lowercase
# Converting integer to string:
print("My number is " + str(3))
print("My number is %d" % 3)
# Using integers
""" Integer operators:
Addition: +
Subtraction: -
Multiplication: *
Division: //
Modulus (remainder): %
Exponent (power): **
The system will first handle brackets (), then **, then *, // and %, and finally + and -
"""
# Global variable:
a = 0
def my_func():
    print(a)
my_func()
# Modify global variable value:
a = 0
def my_func():
    global a
    a = 3
    print(a)
# my_func print 3:
my_func()

# Constants - Variable which can be assigned a value only once (once set - it cannot be changed):
MAXIMUM_SPEED = 240
MINMUM_SPEED = 0

# Use input as a variable:
height = int(input("Enter height of rectangle: "))
width = int(input("Enter width of rectangle: "))
print("The area of the rectangle is %d" % (width * height))

# Convert to String - Casting:
print("3%d" % 2) # will give 32
print("3%d" % 2)
print(int("3") + 8) # will give 11
print("3" + str(8))
# More conversions:
int("6")
int(float("3.5"))

# Selection control statements:
if name == "Kebab":
    print("Hello Kebab!")
if (x > 4):
    x -= 1
# Using is or is not:
a = "Kebab"
b = "Kebab"
if a is b:
    print("Both a and b are Kebabs and both on fire")
if a is not b:
    print("Both Kebabs, but a cooked longer than b")
# if else clause:
if x < 3:
    print("x = 3")
else:
    print("x != 3")
# Nested if statement:
kebabs = raw_input('how many kebabs would you like to eat? ')
if kebabs <= 10:
    if kebabs <= 3:
        cost = 3*kebabs
    else:
        cost = 2*2*kebabs
    print("Your dinner cost: %d" % cost)
else:
    print("You better go to all you can eat restaurant")
# elif statement:
if mark >= 80:
    grade = A
elif mark >= 65:
    grade = B
elif mark >= 50:
    grade = C
else:
    grade = D
# Boolean type:
name = raw_input('Enter your name: ')
if name:
    print("Hello, %s!" % name)
# The same as this:
if bool(name) == True:
    print("Hello, %s!" % name)
# and operator:
if (age >= 50 and age <= 70):
    print("You should go to pension dude")
# More and examples:
if i < len(mylist) and mylist[i] == 3:
    print("There is a value 3 in the list")
if key in mydict and mydict[key] == 3:
    print("There is a key equal to 3")
# or operator:
if age < 18 or age > 80:
    print("You can't use our porn site in the age of %d" % age)
# not operator
name = raw_input('Enter your name: ')
if not name.startswith("N"):
    print("'%s' doesn't start with N!" % name)
# more not operator:
if not x == 5:
    x += 1
# conditional operator:
result = "Pass" if (score >= 50) else "Fail"
# There is no switch statements but however it could be acheived from dictionaries:
NAMES = {
"MA": "Moel Akol",
"BA": "Bar Ashipudi",
"SN": "Sar Netanyahu", # Trailing commas like this are allowed in Python!
}
if short in NAMES: # this tests whether the variable is one of the dictionary's keys
    print("Name: %s" % NAMES[short])
else:
    print("Unknown shortcut: %s" % short)

# Lists:
# a list of strings
food = ['kebab', 'shipud', 'boesh', 'hagav']
# a list of integers
numbers = [13124, 3217, 343, 212, 1]
# an empty list
empty_list = []
# a list of variables we defined somewhere else
vars = [
var1,
var2,
var3, # this trailing comma is legal in Python
]
# Call list objects
print(food[0]) # Will print kebab
print(numbers[3]) # 212
# Count from the end
print(food[-1]) # the last element hagav
print(numbers[-2]) # 212
# Use slices:
print(food[0:2]) # Shipud ve Kebab ahi
print(food[1:-2]) # Shipud ve boesh
print(food[:2]) # Shipud ve Kebab
# Modify add and remove from list:
food[3] = "hummus"
food.append("chips")
del food[2]
# Can contain few data types:
list = ['str', 12, 321.21]
# Find number:
numbers = [123, 321, 32, 1122, 435]
some_number = 32
if number in numbers:"
    print("I have %d" % number)
if number not in numbers:
    print("%d did let you win the lottery" % number)
# List methods and functions:
len(some_list) # Length of a List
sum(number) # Sum of a List
any([1,0,1,0,1]) # Are nay of these True?
numbers = [4, 5, 6, 7, 8]
numbers.append(5)
print(numbers) # 4,5,6,7,8,5
numbers.count(6) # Return 1 if exist 0 if not
numbers.extend([56, 2, 12])
print(numbers) # 4,5,6,7,8,5,56,2,12
numbers.index(56) # value = 6
numbers.index(95) # This is an error
numbers.insert(4, 45) # 4,5,6,7,45,8,5,56,2,12
numbers.remove(56) # Remove element by its value
# Set new list and check more functions:
numbers = [6, 2, 3, 5, 1, 4]
print(sorted(numbers))
print(list(reversed(numbers)))
# Or do it like this:
numbers.sort()
print(numbers)
numbers.reverse()
print(numbers)
# Arithemtic operators abd list:
print([1, 2, 3] + [4, 5, 6])  # output: [1, 2, 3, 4, 5, 6]
print([1, 2, 3] * 3) # output: [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Tuples:
WEEKDAYS = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
print(WEEKDAYS[0])
print(WEEKDAYS[3:])
WEEKDAYS.index('Tuesday')
WEEKDAYS.remove('Sunday')
WEEKDAYS.append('Sunday')
print("%d %d %d" % (1, 2, 3))

# Sets:
food = {'shishkebab', 'chips', 'orez'}
print(sorted(food))
even_numbers = {2, 4, 6, 8, 10}
