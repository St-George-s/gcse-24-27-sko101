# Wordle.

# Functions:

# Allows the user to guess a letter of the specified length.
def userGuessesAWord(wordGuessed, wordHasBeenGuessed, exampleWord, display):
    while wordHasBeenGuessed == False:
        wordGuessed = input("Enter your 5 letter guess: ").upper()
        if len(wordGuessed) == len(exampleWord):
            for counter in range(len(wordGuessed)):
                display = display + wordGuessed[counter] + " "
                wordHasBeenGuessed = True
        else:
            print("Your word does not have the right number of letters. ")
    wordHasBeenGuessed = False
    return display, wordGuessed


# Removes the guessed letter from the displayed keyboard if incorrect.
def removeLetterFromKeyboard(keyboard, keyboardLine2, keyboardLine3, incorrectLettersAsAString):
    # Checks line 1 for the letter.
    for counter in range(len(incorrectLettersAsAString)):
        for counter1 in range(len(keyboard)):
            if incorrectLettersAsAString[counter] == keyboard[counter1]:
                keyboard = keyboard[0:counter1] + " " + keyboard[counter1+1:]
    # Checks line 2 for the letter.
    for counter in range(len(incorrectLettersAsAString)):
        for counter1 in range(len(keyboardLine2)):
            if incorrectLettersAsAString[counter] == keyboardLine2[counter1]:
                keyboardLine2 = keyboardLine2[0:counter1] + " " + keyboardLine2[counter1+1:]
    # Checks line 3 for the letter.
    for counter in range(len(incorrectLettersAsAString)):
        for counter1 in range(len(keyboardLine3)):
            if incorrectLettersAsAString[counter] == keyboardLine3[counter1]:
                keyboardLine3 = keyboardLine3[0:counter1] + " " + keyboardLine3[counter1+1:]
    return keyboard, keyboardLine2, keyboardLine3, incorrectLettersAsAString







# Setup of Variables

exampleWord = "swoop"
display = "1:   "
wordGuessed = ""
wordHasBeenGuessed = False
keyboard = "q w e r t y u i o p"
keyboardLine2 = " a s d f g h j k l"
keyboardLine3 = "   z x c v b n m"
correctLetters = ""
incorrectLetters = ""



# Main code:

print("Welcome to Wordle. Please try to guess a word with 5 letters. ")

display, wordGuessed = userGuessesAWord(wordGuessed, wordHasBeenGuessed, exampleWord, display)
# wordGuessed, exampleWord, correctLetters, incorrectLetters, keyboard, keyboardLine2, keyboardLine3 = removeIncorrectLettersFromKeyboard(wordGuessed, exampleWord, correctLetters, incorrectLetters, keyboard, keyboardLine2, keyboardLine3)


wordGuessed = wordGuessed.lower()
incorrectLetters = set(wordGuessed) - set(exampleWord)
wordGuessed = wordGuessed.upper()
incorrectLettersAsAString = " ".join(str(item) for item in incorrectLetters)
keyboard, keyboardLine2, keyboardLine3, incorrectLetters = removeLetterFromKeyboard(keyboard, keyboardLine2, keyboardLine3, incorrectLettersAsAString)







print("")
print(display)
print("")
print(keyboard)
print(keyboardLine2)
print(keyboardLine3)
