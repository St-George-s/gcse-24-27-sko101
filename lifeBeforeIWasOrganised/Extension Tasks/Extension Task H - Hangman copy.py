
# The Hangman One




# Hangman program - description of code here v2
import random
wantToContinue = "Y"

print("Welcome to this hangman game. ") 
# Loop until user wants to stop 
while wantToContinue == "Y":
    number = random.randint(0, 1)
    wordList = ["hello", "bye"]
    word = wordList[number]
    unguessedWord = ""
    # Makes empty string length of random word
    for counter1 in range(int(len(word))):
        unguessedWord = unguessedWord + "_"
    incorrectLetters = ""
    lettersAfter = ""
    numberOfGuesses = 5
    numberOfGuessesLeft = numberOfGuesses
    guessedLettersIncorrect = ""
    everyGuessedLetter = ""
    letterTwice = 0


    numberOfIncorrectGuesses = 0
    # Loops and asks the user to guess for the number of guesses they have left.
    while numberOfGuessesLeft != 0 and unguessedWord != word:
        # Keeps looping until they guess the whole word.
        if unguessedWord != word:
            found = False
            loseLetterAfterGuessingAgainChecker = 0
            stayTheSame = 0
            
            guess = input("Enter your guess: ")
            guess = guess.lower()
            everyGuessedLetter = everyGuessedLetter + guess
            for counter3 in range(len(word)):
                # If the guess is the same as any letter in the word, it is added to the empty word (unguessedWord).
                if guess == word[counter3]:
                    unguessedWord = unguessedWord[0:counter3] + guess + unguessedWord[counter3+1:]
                    found = True
            print(unguessedWord)
            # If the guess is not in the word at all, it is added to the list of incorrectly guessed letters. 
            if found == False:
                if numberOfIncorrectGuesses == 0:
                    guessedLettersIncorrect = guess
                else:

                    for counter4 in range(len(guessedLettersIncorrect)):
                        if guess == guessedLettersIncorrect[counter4]:
                            letterTwice = letterTwice + 1
                    if letterTwice == 0:
                        guessedLettersIncorrect = guessedLettersIncorrect + ", " + guess
                numberOfIncorrectGuesses = numberOfIncorrectGuesses + 1
            # Prints the incorrectly guessed letters.
            if numberOfIncorrectGuesses == 0:
                print("There are no incorrectly guessed letters. ")
            else:
                print("Your incorrectly guessed letters are " + guessedLettersIncorrect + ". ")
            

            numberOfGuessesLeft = numberOfGuessesLeft - 1
                
        







            # Prints the number of guesses remaining. 
            if numberOfGuessesLeft > 1:
                print("You have " + str(numberOfGuessesLeft) + " guesses left. ")
            elif numberOfGuessesLeft == 1:
                print("You have " + str(numberOfGuessesLeft) + " guess left. ")
    print("______________________________________")
    # Final messages.
    if unguessedWord == word:
        print("You win! ")
        print("The word was " + word + ". ")
        print("It took you " + str(numberOfGuesses - numberOfGuessesLeft) + " guesses. ")
        if numberOfIncorrectGuesses == 0:
            print("There were no incorrectly guessed letters. ")
        else:
            print("Your incorrectly guessed letters were " + guessedLettersIncorrect + ". ")
    else:
        print("You ran out of guesses. ")
        print("The word was " + word + ". ")
        if numberOfIncorrectGuesses == 0:
            print("There were no incorrectly guessed letters. ")
        else:
            print("Your incorrectly guessed letters were " + guessedLettersIncorrect + ". ")

    # Gives the player an option whether they want to keep playing by changing the value determining whether the loop at the beginning will continue.
    wantToContinue = input("Would you like to play again? Y/N: ")
# End of game.
print("______________________________________")
print("Bye! Thank you for playing. ")








