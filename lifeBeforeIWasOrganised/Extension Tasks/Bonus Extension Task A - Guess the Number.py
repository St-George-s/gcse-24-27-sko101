
# Extension of Entension Task A

import random
loops = 0
youDidIt = False
isCorrect = False
gameMode = input("Please enter a game mode (Hint/Normal/Hard): ")
randomNumber = int(random.randint(1, 50))
while (isCorrect == False):
    loops = loops + 1
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
    if (gameMode == "Hard"):
        if loops > 5:
             isCorrect = True
    if user_sNumber == randomNumber:
            isCorrect = True
            youDidIt = True
if youDidIt == True: 
    print("You did it!")
if youDidIt != True:
     print("You did not manage to guess it within 6 guesses. ")

