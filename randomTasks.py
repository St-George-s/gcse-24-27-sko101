# # Extension Task A:
# # Guess the Number 
# # Generate a random number between 1 and 50. The user has to guess the number, with the program giving feedback: 
# # "Too high!" or "Too low!" after each guess. 
# # Congratulate the user once they guess correctly and tell them how many tries it took. 
# # Extensions: 
# # Add a "hint mode" that tells the user if they are within 5 numbers of the correct answer. 
# # Add a "hard mode" that allows only 6 guesses. 

# import random
# isCorrect = False
# randomNumber = int(random.randint(1, 50))
# while isCorrect == False:
#     user_sNumber = int(input("Please enter your guess: "))
#     if user_sNumber > randomNumber:
#         print("Too high! ")
#     if user_sNumber < randomNumber:
#         print("Too low! ")
#     if user_sNumber == randomNumber:
#         isCorrect = True
# print("You did it!")

# # Extension of Entension Task A

# import random
# loops = 0
# youDidIt = False
# isCorrect = False
# gameMode = input("Please enter a game mode (Hint/Normal/Hard): ")
# randomNumber = int(random.randint(1, 50))
# while (isCorrect == False):
#     loops = loops + 1
#     user_sNumber = int(input("Please enter your guess: "))
#     if user_sNumber > randomNumber:
#         print("Too high! ")
#     if user_sNumber < randomNumber:
#         print("Too low! ")
#     if (gameMode == "Hint"):
#         if randomNumber % user_sNumber <= 5:
#              print("The number you are trying to find is within 5. ")
#         else:
#              print("The number you are trying to find is not within 5. ")
#     if (gameMode == "Hard"):
#         if loops > 5:
#              isCorrect = True
#     if user_sNumber == randomNumber:
#             isCorrect = True
#             youDidIt = True
# if youDidIt == True: 
#     print("You did it!")
# if youDidIt != True:
#      print("You did not manage to guess it within 6 guesses. ")


# # Extension task B
# # Username Validation 
# # Write a program that checks if a username is valid based on these rules: 
# # Must be at least 5 characters long. 
# # Cannot contain spaces. 
# # Cannot use any special characters like @, #, $, %, etc.. 
# # After validating, the program should confirm the username is valid or let the user retry. 
# # Extensions: 
# # Include a fixed loop that gives the user 3 chances to create a valid username. 
# # Suggest improvements for an invalid username (e.g., "No spaces allowed!"). 

# user_sUsername = "NoUsername"
# goodPassword = "no"
# while goodPassword == "no":
#     user_sUsername = input("Please enter a possible username: ")
#     if (((len(user_sUsername)) >= 5) and (user_sUsername.isalnum() == True)):
#         print("Password accepted. ")
#         goodPassword = "yes"
#     else:
#         print("Password not accepted. Try again. ")

# # Extension of Extension Task B

chance = 0
user_sUsername = "NoUsername"
goodPassword = "no"
while goodPassword == "no":
    chance = chance + 1
    if chance > 2:
        goodPassword = "failed"
    user_sUsername = input("Please enter a possible username (5 or over letters and no special characters): ")
    if (((len(user_sUsername)) >= 5) and (user_sUsername.isalnum() == True)):
        print("Password accepted. ")
        goodPassword = "yes"
    if (((len(user_sUsername)) < 5)):
        print("Your password is too short. ")
    if (user_sUsername.isalnum() == False):
        print("Your password contains special characters. ")
if goodPassword == "failed":
    print("You have run out of attempts. Try again later. ")
if goodPassword == "yes":
    print("Your password has been accepted.")
