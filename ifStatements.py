# 1. Write a Python program that asks the user for their age and prints whether they are eligible to watch 18-rated movies.

usersAge = int(input("Enter your age: "))
if usersAge >= 18:
    print("You are eligible to watch 18+ movies. ")
else:
    print("no")