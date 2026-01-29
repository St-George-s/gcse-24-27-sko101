
# Extension task B
# Username Validation 
# Write a program that checks if a username is valid based on these rules: 
# Must be at least 5 characters long. 
# Cannot contain spaces. 
# Cannot use any special characters like @, #, $, %, etc.. 
# After validating, the program should confirm the username is valid or let the user retry. 
# Extensions: 
# Include a fixed loop that gives the user 3 chances to create a valid username. 
# Suggest improvements for an invalid username (e.g., "No spaces allowed!"). 

user_sUsername = "NoUsername"
goodPassword = "no"
while goodPassword == "no":
    user_sUsername = input("Please enter a possible username: ")
    if (((len(user_sUsername)) >= 5) and (user_sUsername.isalnum() == True)):
        print("Password accepted. ")
        goodPassword = "yes"
    else:
        print("Password not accepted. Try again. ")