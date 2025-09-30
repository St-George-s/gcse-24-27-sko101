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

# Extension

import random
youDidIt = False
isCorrect = False
gameMode = input("Please enter a game mode (Hint/Normal/Hard): ")
randomNumber = int(random.randint(1, 50))
while (isCorrect == False):
    user_sNumber = int(input("Please enter your guess: "))
    if user_sNumber > randomNumber:
        print("Too high! ")
    if user_sNumber < randomNumber:
        print("Too low! ")
    if (gameMode == "Hint"):
        if randomNumber % user_sNumber <= 5:
             print("The number you are trying to find is within 5. ")
        else:
             print("The number you are trying to find is not within 5. ")
    if user_sNumber == randomNumber:
            isCorrect = True
            youDidIt = True
if youDidIt == True: 
    print("You did it!")
