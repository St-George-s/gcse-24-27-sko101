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


# # Question 10: Write a Python program to output the 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, and 12 times tables from 1 to 12. 
        
# for counter1 in range(1, 13):
#     print("This is the " + str(counter1) + " times table.")
#     for counter2 in range(1, 13):
#         print(str(counter2) + " * " + str(counter1) + " = " + str(counter1 * counter2))


# Extension task: Write a Python program that: 
# Asks the user which times table they would like to see (e.g. 4, 7, 12). 
# Asks the user how far the table should go (e.g. up to 20). 
# Prints the chosen times table up to the number given. 
# Then asks the user if they would like to see another times table and repeats until they type no.      

# #attempt 1


# working one
another = "Y"

while another == "Y":
    timesTable = int(input("Enter the times table you would like to see: "))
    howFarItShouldGo = int(input("Enter how far it should go: "))
    print("This is the " + str(timesTable) + " times table.")
    for counter1 in range(1, howFarItShouldGo + 1):
        print(str(counter1) + " times " + str(timesTable) + " equals " + str(timesTable * counter1) + ".")
    another = input("Would you like another? (Y/N): ")
print("Goodbye! ")



# random stuff
# #attempt 2

# counter33 = 2
# for counter32 in range(counter33):
#     timesTable = int(input("Enter the times table you would like to see: "))
#     howFarItShouldGo = int(input("Enter how far it should go: "))
#     print("This is the " + str(timesTable) + " times table.")
#     for counter1 in range(1, howFarItShouldGo + 1):
#         print(str(counter1) + " times " + str(timesTable) + " equals " + str(timesTable * counter1) + ".")
#     wouldLikeToContinue = input("Would you like to do another one? Input Yes or No: ")
#     if wouldLikeToContinue == "No":
#         print("Goodbye! ")
#         counter33 = counter33 - 3
#     if wouldLikeToContinue == "Yes":
#         print("Ok.")
#         counter33 = counter33 + 1 

# #attempt 2bb

# three = 3
# counter34 = 1
# for counter34 in range(counter34):
#     counter33 = 1
#     for counter32 in range(counter33):
#         timesTable = int(input("Enter the times table you would like to see: "))
#         howFarItShouldGo = int(input("Enter how far it should go: "))
#         print("This is the " + str(timesTable) + " times table.")
#         for counter1 in range(1, howFarItShouldGo + 1):
#             print(str(counter1) + " times " + str(timesTable) + " equals " + str(timesTable * counter1) + ".")
#         wouldLikeToContinue = input("Would you like to do another one? Input Yes or No: ")
#         if wouldLikeToContinue == "No":
#             print("Goodbye! ")
#             counter34 = counter33 - three
#             counter33 = counter34 - three
#         if wouldLikeToContinue == "Yes":
#             print("Ok.")
#             counter34 = counter33 + three
#             counter33 = counter34 + three



    


#attempt 2 working
# for counter8 in range(2):




# #ignore (also attempt 1) (if True did not work)
# wouldLikeToContinue = bool(input("Would you like to do another one? "))
# if "yes":
#     timesTable = int(input("Enter the times table you would like to see: "))
#     howFarItShouldGo = int(input("Enter how far it should go: "))
#     for counter in range(1, howFarItShouldGo + 1):
#         print(str(counter1) + " times " + str(timesTable) + " equals " + str(timesTable * counter1) + ".")
# if "no":
#     print("Have a nice day! Thank you for using Alina's calculator.")


# # More stuff
# yesOrNo = input("Enter Yes or No: ")
# if yesOrNo == "Yes":
#     print("You said Yes, correct?")
# elif yesOrNo == "No":
#     print("You said No, correct?")
# else:
#     print("You didn't do it, did you?")


# for counter1 in range(3):
#     yesOrNo2 = input("Enter Yes or No: ")
#     if yesOrNo2 == "Yes":
#         timesTable = int(input("Enter the times table: "))
#         howFarItShouldGo = int(input("How far should it go? "))
#         print("This is the " + str(timesTable) + " times table.")
#         for counter in range(1, howFarItShouldGo + 1):
#             print(str(counter) + " times " + str(timesTable) + " equals " + str(timesTable * counter))
#     elif yesOrNo2 == "No":
#         print("Sure thing.")
#     else:
#         print("I asked you to do one thing...")


# userSaysNo = input("Please Yes or No to begin: ")
# for counter3 in range(1):
#     if userSaysNo == "Yes":
#         for counter1 in range(1):
#             yesOrNo2 = input("Enter Yes or No: ")
#             if yesOrNo2 == "Yes":
#                 print("work pleaseeeee")
#                 userSaysNo = input("Enter Yes or No: ")
#             elif yesOrNo2 == "No":
#                 print("Sure thing.")
#             else:
#                 print("I asked you to do one thing...")
#     elif userSaysNo == "No":
#         print("Okay then, have a nice day!")




