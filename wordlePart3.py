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



# Removes incorrect letters from the visible keyboard.
def removeIncorrectLettersFromKeyboard(wordGuessed, exampleWord, correctLetters, incorrectLetters, keyboard, keyboardLine2, keyboardLine3):
    # Searches words for matching letters.
    for counter in range(len(wordGuessed)):
        for counter2 in range(len(exampleWord)):
            if wordGuessed[counter] == exampleWord[counter2]:
                correctLetters = correctLetters + wordGuessed[counter]
    # Removes the matching letters from the word to create a variable containing the incorrect letters.
    for counter in range(len(wordGuessed)):
        for counter2 in range(len(correctLetters)):
            if wordGuessed[counter] == correctLetters[counter2]:
                incorrectLetters = incorrectLetters[0:counter] + " " + incorrectLetters[counter+1:]
    # Removes the guessed letter from the displayed keyboard if incorrect.
    # Checks line 1 for the letter.
    for counter in range(len(incorrectLetters)):
        for counter1 in range(len(keyboard)):
            if incorrectLetters[counter] == keyboard[counter1]:
                keyboard = keyboard[0:counter1] + " " + keyboard[counter1+1:]
    # Checks line 2 for the letter.
    for counter in range(len(incorrectLetters)):
        for counter1 in range(len(keyboardLine2)):
            if incorrectLetters[counter] == keyboardLine2[counter1]:
                keyboardLine2 = keyboardLine2[0:counter1] + " " + keyboardLine2[counter1+1:]
    # Checks line 3 for the letter.
    for counter in range(len(incorrectLetters)):
        for counter1 in range(len(keyboardLine3)):
            if incorrectLetters[counter] == keyboardLine3[counter1]:
                keyboardLine3 = keyboardLine3[0:counter1] + " " + keyboardLine3[counter1+1:]
    return wordGuessed, exampleWord, correctLetters, incorrectLetters, keyboard, keyboardLine2, keyboardLine3






# Setup of Variables

exampleWord = "swoop"
display = "1:   "
wordGuessed = ""
wordHasBeenGuessed = False
keyboard = "q w e r t y u i o p"
keyboardLine2 = " a s d f g h j k l"
keyboardLine3 = "   z x c v b n m"
correctLetters = ""
incorrectLetters = wordGuessed



# Main code:

print("Welcome to Wordle. Please try to guess a word with 5 letters. ")

display, wordGuessed = userGuessesAWord(wordGuessed, wordHasBeenGuessed, exampleWord, display)
wordGuessed, exampleWord, correctLetters, incorrectLetters, keyboard, keyboardLine2, keyboardLine3 = removeIncorrectLettersFromKeyboard(wordGuessed, exampleWord, correctLetters, incorrectLetters, keyboard, keyboardLine2, keyboardLine3)



print("")
print(display)
print("")
print(keyboard)
print(keyboardLine2)
print(keyboardLine3)




