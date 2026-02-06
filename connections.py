# Connections game.


# Functions:

# Sets the words to the example words.
def useExampleSet():
    set1 = ["MOVE", "REACH", "SWAY", "TOUCH"]
    set2 = ["BINGO", "CORRECT", "DING", "SWAY"]
    set3 = ["CHANGE", "GREEN", "PAPER", "SCRATCH"]
    set4 = ["CHIP", "PHONE", "SCOPE", "WAVE"]
    return set1, set2, set3, set4

# Generates an order for the words to be displayed in.
def generateOrder():
    wordsInOrder = ""
    for counter in range(16):
        numberForSetChosen = random.randint(0,3)
        numberForWordInSetChosen = random.randint(0,3)
        if numberForSetChosen == 1:
            setChosen = set1
        elif numberForSetChosen == 2:
            setChosen = set2
        elif numberForSetChosen == 3:
            setChosen = set3
        else:
            setChosen = set4
        setChosen[numberForWordInSetChosen]
        print(setChosen[numberForWordInSetChosen])


# Main code:
import random



# Uses the example set.
set1, set2, set3, set4 = useExampleSet()

generateOrder()






# affect, you got it, slang for money, objects with the prefix "micro-"