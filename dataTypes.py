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
print(str(input1AsAnInt) + " multiplied " + str(input2AsAnInt) + " = ")
print(input1AsAnInt * input2AsAnInt)

# Activity 2 - Input user's age, output age times 7
inputUsersAge = input("Enter your age: ")
inputUsersAgeAsAnInt = int(inputUsersAge)
print(str(inputUsersAge) + " multiplied by 7 =")
print(inputUsersAgeAsAnInt * 7)

# Activity 3 - Take radius as input, output volume of sphere (v = 4/3 x pi x r^3)