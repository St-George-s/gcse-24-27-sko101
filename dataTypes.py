# Data Types
name = "Alina" # This is a string
myAge = 14 # This is an integer
height = 10.1 # This is a decimal number (float/real)
hasADriversLicence = False # This is a boolean (True/False)

# Casting (Change from one data type to another)
age = input("Enter age: ")
print(age)
print(age + "10") # Concatenate two strings together (join them)
ageAsAnInt = int(age)
print(ageAsAnInt + 10) # Add two integers together (maths addition)
print("Your age is: " + str(ageAsAnInt))

# Data types - more examples
stillAnInteger = -4
myNumber = "078782282873" # Always store as a string (As it will remove the 0)

# Arithmetic operators
add = 10 + 10
subtract = 10 - 10
multiply = 10 * 10
divide = 10 / 10 # Will output a float, not an integer like the others
integerDivide = 10 // 10 # Will divide and output an integer, and will automatically round it to be one if needed
print(add, subtract, multiply, divide)
print(integerDivide)
modulo = 12 % 10 # Remainder of the division
print(modulo)
exponent = 2 ** 3 # To the power of
print(exponent)

# Activity 1 - Take two inputs, multiply them together and output answer
input1 = input("Enter a number: ")
input1AsAnInt = int(input1)
input2 = input("Enter another number: ")
input2AsAnInt = int(input2)
print(str(input1AsAnInt) + " multiplied " + str(input2AsAnInt) + " = " + str(input1AsAnInt * input2AsAnInt))

# Activity 2 - Input user's age, output age times 7
inputUsersAge = input("Enter your age: ")
inputUsersAgeAsAnInt = int(inputUsersAge)
print(str(inputUsersAge) + " multiplied by 7 = " + str(inputUsersAgeAsAnInt * 7))


# Activity 3 - Take radius as input, output volume of sphere (v = 4/3 x pi x r^3)
inputRadius = input("Enter a radius to find the volume of a sphere: ")
inputRadiusAsAnInt = int(inputRadius)
import math
print("Volume = 4 / 3 * pi * " + inputRadius + " to the power of 3 ")
print("Volume = " + str(4/3 * math.pi * (inputRadiusAsAnInt ** 3)))

# It is better to turn numbers into floats instead of integers e.g. number1 = float(input("Enter a number: ")) as using an integer means that you would not have any decimals.
# I just turned the numbers into integers above.
# For example, if you did the last question again but changed the radius to a float instead of an integer, it would look like this:

radius = float(input("Enter a radius: "))
print(4/3 * math.pi * radius ** 3)




number1 = float(input("Enter Number: "))