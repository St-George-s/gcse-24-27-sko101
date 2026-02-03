import random

timesPlayed = 0
loseLetterAfterCorrectGuessOn = False
loseLetterAfterGuessingAgainOn = True
numberOfIncorrectGuesses = 0
wantToContinue = "Y"
numberOfGuesses = 5

def setUp():
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
    if changeSettings == "N":
        print("______________________________________")

def getUserGuesses(randomWord, blankString):
    everyGuessedLetter = []
    # Keeps looping until they guess the whole word.
    if blankString != randomWord:
        letterInRanWordCounter = 0
        letterInRanWord = False

        userLetterGuess = input("Enter your guess: ").lower()
        everyGuessedLetter.append(userLetterGuess)

        for counter in range(len(randomWord)):
            # If the guess is the same as any letter in the word, it is added to the empty word (blankString).
            if userLetterGuess == randomWord[counter]:
                blankString = blankString[0:counter] + userLetterGuess + blankString[counter+1:]
                letterInRanWord = True
                letterInRanWordCounter = letterInRanWordCounter + 1
        print(blankString)
        # If the letter they guessed has already been guessed, inform the player.
        return blankString, everyGuessedLetter, userLetterGuess, letterInRanWordCounter, letterInRanWord

def checkForDoubleLetter(everyGuessedLetter, userLetterGuess, letterInRanWordCounter):
    # letterGuessedCounter = 0

    # for counter in range(len(everyGuessedLetter)):
    #     if userLetterGuess == everyGuessedLetter[counter]:
    #         letterGuessedCounter = letterGuessedCounter + 1
    # if letterGuessedCounter > letterInRanWordCounter and letterInRanWordCounter < letterGuessedCounter + 2:
    #     print("This letter has already been guessed. ")
    pass

def addIncorrectGuessesToArray(everyGuessedLetter, letterInRanWord, userLetterGuess):
    # If the guess is not in the word at all, it is added to the list of incorrectly guessed letters. 
    if letterInRanWord == False:
        if letterInRanWord not in everyGuessedLetter:
            everyGuessedLetter.append(userLetterGuess)
        numberOfIncorrectGuesses = numberOfIncorrectGuesses + 1


# Main program
randomWord, blankString = getRandomWordAndBlankString()
getRandomWordAndBlankString()
pickGameSettings()

# Loops and asks the user to guess for the number of guesses they have left.
while numberOfGuesses != 0 and blankString != word:
    blankString, everyGuessedLetter, userLetterGuess, letterInRanWordCounter, letterInRanWord = getUserGuesses(randomWord, blankString)
    # checkForDoubleLetter(everyGuessedLetter, userLetterGuess, letterInRanWordCounter)
    addIncorrectGuessesToArray(everyGuessedLetter, letterInRanWord, userLetterGuess)