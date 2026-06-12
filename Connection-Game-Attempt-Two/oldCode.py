# Connections game.


# Functions:

# Sets the words to the example words.
def useExampleSet():
    set1 = ["MOVE", "REACH", "SWAY", "TOUCH"]
    set2 = ["BINGO", "CORRECT", "DING", "RIGHT"]
    set3 = ["CHANGE", "GREEN", "PAPER", "SCRATCH"]
    set4 = ["CHIP", "PHONE", "SCOPE", "WAVE"]
    return set1, set2, set3, set4

# Allows the user to choose four words as their guess.
def userGuesses():
    userGuess1 = input("Enter the words you would like to guess, one per line: ").upper
    userGuess2 = input("Second word: ").upper
    userGuess3 = input("Third word: ").upper
    userGuess4 = input("Fourth word: ").upper
    return userGuess1, userGuess2, userGuess3, userGuess4


# Main code:
import random



# Uses the example set.
set1, set2, set3, set4 = useExampleSet()

print(set1)
print(set2)
print(set3)
print(set4)


userGuess1, userGuess2, userGuess3, userGuess4 = userGuesses()

print(userGuess1)



# Currently has no use:

# affect, you got it, slang for money, objects with the prefix "micro-"


# # Generates an order for the words to be displayed in.
# def generateOrder():
#     wordsInOrder = ""
#     for counter in range(16):
#         numberForSetChosen = random.randint(0,3)
#         numberForWordInSetChosen = random.randint(0,3)
#         if numberForSetChosen == 1:
#             setChosen = set1
#         elif numberForSetChosen == 2:
#             setChosen = set2
#         elif numberForSetChosen == 3:
#             setChosen = set3
#         else:
#             setChosen = set4
#         print(setChosen[numberForWordInSetChosen])

