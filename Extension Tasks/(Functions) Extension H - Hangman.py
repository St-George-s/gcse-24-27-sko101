import random

timesPlayed = 0
loseLetterAfterCorrectGuessOn = False
loseLetterAfterGuessingAgainOn = True

def setUp():
    wantToContinue = "Y"
    loseLetterAfterCorrectGuess = "N"
    loseLetterAfterGuessingAgain = "Y"
    print("Welcome to this hangman game. ") 


def getRandomWordAndBlankString():
    number = random.randint(0, 1)
    wordList = ["hello", "bye"]
    randomWord = wordList[number]
    blankString = ""
    # Makes empty string length of random word
    for _ in randomWord:
        blankString = blankString + "_"
    return randomWord, blankString

def pickGameSettings():
    message = "This is automatically off. "
    message2 = "This is automatically on. "

        # Allows the user to change their settings.
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    if timesPlayed > 0:
        message = "Your settings are currently the same as last round. "
    changeSettings = input("Would you like to change your settings? Y/N: ")
    if changeSettings == "Y":
        print("______________________________________")
        print("Your settings will remain the same if you play another round. ")
        print("______________________________________")
        print("Recommended Settings: \n - N  \n - Y ")
        print("______________________________________")
        loseLetterAfterCorrectGuess = input("- Would you like to lose guesses after guessing correctly? " + message + "(" + (str(loseLetterAfterCorrectGuess)) + ") " + "Y/N: ")
        loseLetterAfterGuessingAgain = input("- Would you like to lose guesses after guessing a letter you have guessed before? " + message2 + "(" + (str(loseLetterAfterGuessingAgain)) + ") " + "Y/N: ")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")

# Main program
randomWord, blankString = setUp()
