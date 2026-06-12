# Connections game.


# Functions:

# Sets the words to the example words.
def useExampleSet():
    set = [
    ["MOVE", "REACH", "SWAY", "TOUCH"],
    ["BINGO", "CORRECT", "DING", "RIGHT"],
    ["CHANGE", "GREEN", "PAPER", "SCRATCH"],
    ["CHIP", "PHONE", "SCOPE", "WAVE"]
    ]
    return set

# Allows the user to choose four words as their guess.
def userGuesses():
    userGuess = []
    userGuess = userGuess, input("Enter the words you would like to guess, one per line: ").upper
    userGuess = userGuess, input("Second word: ").upper
    userGuess = userGuess, input("Third word: ").upper
    userGuess = userGuess, input("Fourth word: ").upper
    return userGuess

# Randomises the order of the words.
def randomise(set):
    randomSet = [
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "],
        [" ", " ", " ", " "]
    ]
    cont = ""
    checkIfUsed = [" "]
    for counter1 in range(4):
        for counter2 in range(4):
            if len(cont) < 17:
                found = True
                while found == True:
                    randomNumberColumn = random.randint(0, 3)
                    randomNumberRow = random.randint(0, 3)
                    wordBeingMoved = set[counter1][counter2]
                    for counter3 in range(len(checkIfUsed)):
                        rowAndCollumn = str(randomNumberColumn) + str(randomNumberRow)
                        if checkIfUsed[counter3] == rowAndCollumn:
                            found = True
                            break
                        else:
                            found = False
                    if found == False:
                        randomSet[randomNumberColumn][randomNumberRow] = wordBeingMoved
                        checkIfUsed.append(str(randomNumberColumn) + str(randomNumberRow))
    return randomSet

# Prints it but more beautifully.
def print_prettily(printVer):
    for counter in range(len(printVer)):
        rowPrint = ""
        for counterTwo in range(len(printVer[counter])):
            rowPrint += str(printVer[counter][counterTwo]) + " "
        print(rowPrint)


# Main code:
import random


# Uses the example set.
set = useExampleSet()

# print(set[0])
# print(set[1])
# print(set[2])
# print(set[3])

# Randomises the set.
randomSet = (randomise(set))

# print(randomSet[0])
# print(randomSet[1])
# print(randomSet[2])
# print(randomSet[3])


wantToContinue = True
while wantToContinue == True:
    userWouldLikeTo = input("Would you like to CHOOSE your four words, RANDOMISE the order of the words, or GIVE UP? ").upper
    if userWouldLikeTo == "RANDOMISE":
        randomSet = (randomise(set))

    else:
        print("Invalid. Please try again. ")
    print(print_prettily(randomSet))
    