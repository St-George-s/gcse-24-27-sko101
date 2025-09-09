# for counter in range(10):
#     print("Hello world")


# # Fixed Loops

# # Question 1: Write a program to print your name 10 times:

# for counter in range(10):
#     print("Alina")


# # Question 2: Write a program to ask for your name and print it 1000 times:

# usersName = input("Enter your name: ")
# for counter in range(1000):
#     print(usersName)


# # Question 3: Write a program to ask for your name and print Hello and then your name 1000 times:

# usersSecondName = input("Enter your name again please: ")
# print("Hello ")
# for counter in range(1000):
#     print(usersSecondName)


# # Question 4: Write a program to print the answers to the 8 times table from 1 to 12. 

# for counter in range(1, 13):
#     print(counter * 8)


# # Question 5: Write a Python program to print the answers to the 8 times table from 1 to 1000. 

# for counter in range(1, 1001):
#     print(counter * 8)


# # Question 6: Write a Python program to: 
# # Calculate the 7 times table up to 12. 
# # Print "7 x number = answer" each time. 

# for counter in range(1, 13):
#     print("7 * " + str(counter) + " = " + str(7 * counter))


# # Question 7: Write a Python program to ask the user to input the age of 10 people and print each age. 
# for counter in range(1,11):
#     age = int(input("Enter an age (" + str(counter) + "): "))
#     print(age)


# # Question 8: Write a Python program to: 
# # Ask the user to input the age of 10 people. 
# # Print the age of each person in 10 years' time. 

# for counter in range(1, 11):
#     age = int(input("Enter an age (" + str(counter) + "): "))
#     print(str(age * 10))


# # Question 9: Write a Python program to: 
# # Ask the user to input the age of 10 people. 
# # Add up all the ages. 
# # Print the total ages. 

# total = 0
# for counter in range(1, 11):
#      age = float(input("Enter an age (" + str(counter) + "): "))
#      total = total + age
# print(total)


# Question 10: Write a Python program to output the 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 times tables from 1 to 12. 
        
for counter1 in range(1, 13):
    print("This is the " + str(counter1) + " times table.")
    for counter2 in range(1, 13):
        print(str(counter1) + " * " + str(counter2) + " = " + str(counter1 * counter2))


# Extension task: Write a Python program that: 
# Asks the user which times table they would like to see (e.g. 4, 7, 12). 
# Asks the user how far the table should go (e.g. up to 20). 
# Prints the chosen times table up to the number given. 
# Then asks the user if they would like to see another times table and repeats until they type no.      