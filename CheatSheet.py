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
    print("’%s’ doesn’t start with N!" % name)
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
if short in NAMES: # this tests whether the variable is one of the dictionary’s keys
    print("Name: %s" % NAMES[short])
else:
    print("Unknown shortcut: %s" % short)

# Lists




# Detect errors:
try:
height = int(input("Enter height of rectangle: "))
width = int(input("Enter width of rectangle: "))
except ValueError as e: # if a value error occurs, we will skip to this point
print("Error reading height and width: %s" % e)
# Add this block to while loop:
correct_input = False # this is a boolean value -- it can be either true or false.
while not correct_input: # this is a while loop
    try:
        height = int(input("Enter height of rectangle: "))
        width = int(input("Enter width of rectangle: "))
    except ValueError:
        print("Please enter valid integers for the height and width.")
    else: # this will be executed if there is no value error
        correct_input = True
# See results:
print("The area of the rectangle is %d" % (width * height))


# Print to a file:
with open(’file1.txt’, ’w’) as file1:
print("Hello!", file=file1)
# Can be used with read or write methods:
with open(’file1.txt’, ’w’) as file1:
file1.write("Hello!")


# Using strings:
name = "Nadav"
age = 35
print("Hello! My name is %s." % name)
print("Hello! My name is %s and I am %d years old." % (name, age))
print(’This is one line.\nThis is another line.’)
"""
\\ literal backslash
\’ single quote
\" double quote
\n newline
\t tab
"""

name = "Shipudei Afuli"
# Find the length of a string with the built-in len function
print(len(name))
# Print the string converted to lowercase
print(name.lower())

# Converting integer to string:
print("My number is " + str(3))
print("My number is %d" % 3)

""" Integer operators:
Addition: +
Subtraction: -
Multiplication: *
Division: //
Modulus (remainder): %
Exponent (power): **

The system will first handle brackets (), then **, then *, // and %, and finally + and -
"""



# Indentation:
def kebab_day(day):
    if day == "monday":
        return "This is my kebab day"
    if day != "monday":
        return "Today I eat shipud"

print(kebab_day("sunday"))
print(kebab_day("monday"))


no_chickens = "No chickens here ..."
def append_chickens(text):
    text = text + " Rawwwk!"
    return text

print(append_chickens(no_chickens))
