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
    return display






# Setup of Variables

exampleWord = "swoop"
display = "1:   "
wordGuessed = ""
wordHasBeenGuessed = False
keyboard = "q w e r t y u i o p"
keyboardLine2 = " a s d f g h j k l"
keyboardLine3 = "   z x c v b n m"



# Main code:

print("Welcome to Wordle. Please try to guess a word with 5 letters. ")

display = userGuessesAWord(wordGuessed, wordHasBeenGuessed, exampleWord, display)
keyboard, keyboardLine2, keyboardLine3 = removeLetterFromKeyboard(keyboard, keyboardLine2, keyboardLine3, wordGuessed)

print("")
print(display)
print("")
print(keyboard)
print(keyboardLine2)
print(keyboardLine3)



for counter in range(len(wordGuessed)):
    if wordGuessed[counter] ==