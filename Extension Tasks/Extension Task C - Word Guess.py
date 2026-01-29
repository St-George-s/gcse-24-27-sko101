
# Extension Task C
# Word Guesser 
# The program selects a random word from a list (e.g., ["apple", "banana", "grape"]). The user must guess the letters in the word. After each guess, the program: 
# Updates and shows the current state of the word (e.g., _ p p _ _). 
# Shows the incorrect guesses and how many guesses are left. 
# Extensions: 
# Do not penalise the user for repeating a letter they've already guessed. 
# Add a "hint mode" that reveals one letter from the word. 

import random
wordNumber = random.randint(0, 2)
wordList = ["apple", "banana", "grape"]
chosenWord = wordList[wordNumber]
output = " "
incorrectGuesses = 0
while incorrectGuesses < 5:
    letterGuessed = input("Enter a letter: ")
    for counter in range(len(chosenWord)):
        if letterGuessed == chosenWord[counter]:
            print("yes")
            # ouput = str(output) + str(letterGuessed)
            # print(output)
        else:
            incorrectGuesses = incorrectGuesses + 1
            print("no")
