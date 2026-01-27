# # Extension Task A:
# # Guess the Number 
# # Generate a random number between 1 and 50. The user has to guess the number, with the program giving feedback: 
# # "Too high!" or "Too low!" after each guess. 
# # Congratulate the user once they guess correctly and tell them how many tries it took. 
# # Extensions: 
# # Add a "hint mode" that tells the user if they are within 5 numbers of the correct answer. 
# # Add a "hard mode" that allows only 6 guesses. 

# import random
# isCorrect = False
# randomNumber = int(random.randint(1, 50))
# while isCorrect == False:
#     user_sNumber = int(input("Please enter your guess: "))
#     if user_sNumber > randomNumber:
#         print("Too high! ")
#     if user_sNumber < randomNumber:
#         print("Too low! ")
#     if user_sNumber == randomNumber:
#         isCorrect = True
# print("You did it!")

# # Extension of Entension Task A

# import random
# loops = 0
# youDidIt = False
# isCorrect = False
# gameMode = input("Please enter a game mode (Hint/Normal/Hard): ")
# randomNumber = int(random.randint(1, 50))
# while (isCorrect == False):
#     loops = loops + 1
#     user_sNumber = int(input("Please enter your guess: "))
#     if user_sNumber > randomNumber:
#         print("Too high! ")
#     if user_sNumber < randomNumber:
#         print("Too low! ")
#     if (gameMode == "Hint"):
#         if randomNumber % user_sNumber <= 5:
#              print("The number you are trying to find is within 5. ")
#         else:
#              print("The number you are trying to find is not within 5. ")
#     if (gameMode == "Hard"):
#         if loops > 5:
#              isCorrect = True
#     if user_sNumber == randomNumber:
#             isCorrect = True
#             youDidIt = True
# if youDidIt == True: 
#     print("You did it!")
# if youDidIt != True:
#      print("You did not manage to guess it within 6 guesses. ")


# # Extension task B
# # Username Validation 
# # Write a program that checks if a username is valid based on these rules: 
# # Must be at least 5 characters long. 
# # Cannot contain spaces. 
# # Cannot use any special characters like @, #, $, %, etc.. 
# # After validating, the program should confirm the username is valid or let the user retry. 
# # Extensions: 
# # Include a fixed loop that gives the user 3 chances to create a valid username. 
# # Suggest improvements for an invalid username (e.g., "No spaces allowed!"). 

# user_sUsername = "NoUsername"
# goodPassword = "no"
# while goodPassword == "no":
#     user_sUsername = input("Please enter a possible username: ")
#     if (((len(user_sUsername)) >= 5) and (user_sUsername.isalnum() == True)):
#         print("Password accepted. ")
#         goodPassword = "yes"
#     else:
#         print("Password not accepted. Try again. ")

# # Extension of Extension Task B

# chance = 0
# user_sUsername = "NoUsername"
# goodPassword = "no"
# while goodPassword == "no":
#     chance = chance + 1
#     if chance > 2:
#         goodPassword = "failed"
#     user_sUsername = input("Please enter a possible username (5 or over letters and no special characters): ")
#     if (((len(user_sUsername)) >= 5) and (user_sUsername.isalnum() == True)):
#         print("Password accepted. ")
#         goodPassword = "yes"
#     elif (((len(user_sUsername)) < 5)):
#         print("Your password is too short. ")
#     if (user_sUsername.isalnum() == False):
#         print("Your password contains special characters. ")
# if goodPassword == "failed":
#     print("You have run out of attempts. Try again later. ")
# if goodPassword == "yes":
#     print("Your password has been accepted.")


# # Extension Task C
# # Word Guesser 
# # The program selects a random word from a list (e.g., ["apple", "banana", "grape"]). The user must guess the letters in the word. After each guess, the program: 
# # Updates and shows the current state of the word (e.g., _ p p _ _). 
# # Shows the incorrect guesses and how many guesses are left. 
# # Extensions: 
# # Do not penalise the user for repeating a letter they've already guessed. 
# # Add a "hint mode" that reveals one letter from the word. 

# import random
# wordNumber = random.randint(0, 2)
# wordList = ["apple", "banana", "grape"]
# chosenWord = wordList[wordNumber]
# output = " "
# incorrectGuesses = 0
# while incorrectGuesses < 5:
#     letterGuessed = input("Enter a letter: ")
#     for counter in range(len(chosenWord)):
#         if letterGuessed == chosenWord[counter]:
#             print("yes")
#             # ouput = str(output) + str(letterGuessed)
#             # print(output)
#         else:
#             incorrectGuesses = incorrectGuesses + 1
#             print("no")


# # Extension Task J
# # Mor-se Coding   
# # Create a program that allows you to enter a string and encode it into Morse code, using   ‘ . ‘ and ‘ - ‘ notation. Spaces between words should be replaced with the “|” (pipe) character.  
# # Use a normal space for gaps between each character. 
# # Optional Extensions:  
# # Develop your program to translate from Morse to alphanumeric, using the standards above 

# # Not fixed by teacher
# user_sSentence = input("Enter a sentence: ")
# user_sSentence.upper()
# standardAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W,", "X", "Y", "Z", " ", ". "]
# morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..", " ", " | "]
# for counter1 in range(len(user_sSentence)):
#     for counter2 in range(0, 28):
#         if user_sSentence[counter1] == standardAlphabet[counter2]:
#             user_sSentence[counter1] = morseAlphabet[counter2]
# print(user_sSentence)

# # Fixed by teacher
# alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
#             "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
# morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..",
#          ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-",
#          ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--",
#          "--..", "|"]   # pipe replaces spaces between words
# sentence = input("Enter a sentence: ").upper()
# output = ""
# for letter in sentence:
#     found = False
#     for counter in range(len(alphabet)):
#         if letter == alphabet[counter]:
#             output = output + morse[counter] + " "
#             found = True
#             break    # stop searching once matched
#     if found == False:
#         output = output + "? "   # for unknown characters
# print(output)


# # Extension Task F 
# # Mastermind 
# # Generate a random four digit number.
# # The player has to keep inputting four digit numbers until they guess the randomly generated number.
# # After each unsuccessful try it should say how many numbers they got correct, but not which position they got right.
# # At the end of the game should congratulate the user and say how many tries it took. 
# # Optional Extensions:  
# # Let the user pick an easy mode which shows the user which position that they guessed correctly 
# # Let the user pick a hard mode that gives five digits instead of four 
# # After the game is finished, ask the user for their name and input their score into a table.
# # Show them the high score at the start of the game so that it gives a sense of competition. 

# import random
# randomNumber = str(random.randint(1, 1000))
# while len(randomNumber) > 4:
#     randomNumber = str(str("0") + str(randomNumber))
# print(randomNumber)


# The Hangman One



# # Hangman program - description of code here
# import random
# wantToContinue = "Y"
# loseLetterAfterCorrectGuess = "Y"
# loseLetterAfterGuessingAgain = "Y"
# timesPlayed = 0
# message = "This is automatically on. "
# print("Welcome to this hangman game. ") 
# # Loop until user wants to stop 
# while wantToContinue == "Y":
#     number = random.randint(0, 1)
#     wordList = ["hello", "bye"]
#     word = wordList[number]
#     unguessedWord = ""
#     # Makes empty string length of random word
#     for counter1 in range(int(len(word))):
#         unguessedWord = unguessedWord + "_"
#     incorrectLetters = ""
#     lettersAfter = ""
#     numberOfGuesses = 5
#     numberOfGuessesLeft = numberOfGuesses
#     guessedLettersIncorrect = ""
#     everyGuessedLetter = ""
#     letterTwice = 0

#     # Allows the user to change their settings.
#     print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
#     if timesPlayed > 0:
#         message = "Your settings are currently the same as last round. "

#     changeSettings = input("Would you like to change your settings? Y/N: ")
#     if changeSettings == "Y":
#         print("______________________________________")
#         loseLetterAfterCorrectGuess = input("- Would you like to lose letters after guessing correctly? " + message + "(" + (str(loseLetterAfterCorrectGuess)) + ") " + "Y/N: ")
#         loseLetterAfterGuessingAgain = input("- Would you like to lose letters after guessing a letter you have guessed before? " + message + "(" + (str(loseLetterAfterGuessingAgain)) + ") " + "Y/N: ")
#         print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")



#     numberOfIncorrectGuesses = 0
#     # Loops and asks the user to guess for the number of guesses allowed.
#     for counter2 in range(numberOfGuesses):
#         # Keeps looping until they guess the whole word.
#         if unguessedWord != word:
#             found = False
#             print("______________________________________")
#             guess = input("Enter your guess: ")
#             guess = guess.lower()
#             for counter3 in range(len(word)):
#                 # If the guess is the same as any letter in the word, it is added to the empty word (unguessedWord).
#                 if guess == word[counter3]:
#                     unguessedWord = unguessedWord[0:counter3] + guess + unguessedWord[counter3+1:]
#                     found = True
#             print(unguessedWord)
#             # If the guess is not in the word at all, it is added to the list of incorrectly guessed letters. 
#             if found == False:
#                 if numberOfIncorrectGuesses == 0:
#                     guessedLettersIncorrect = guess
#                 else:

#                     for counter4 in range(len(guessedLettersIncorrect)):
#                         if guess == guessedLettersIncorrect[counter4]:
#                             letterTwice = letterTwice + 1
#                     if letterTwice == 0:
#                         guessedLettersIncorrect = guessedLettersIncorrect + ", " + guess
#                 numberOfIncorrectGuesses = numberOfIncorrectGuesses + 1
#             # Prints the incorrectly guessed letters.
#             if numberOfIncorrectGuesses == 0:
#                 print("There are no incorrectly guessed letters. ")
#             else:
#                 print("Your incorrectly guessed letters are " + guessedLettersIncorrect + ". ")
#             # Prints the number of guesses remaining. 
#             numberOfGuessesLeft = numberOfGuessesLeft - 1
#             if numberOfGuessesLeft > 1:
#                 print("You have " + str(numberOfGuessesLeft) + " guesses left. ")
#             elif numberOfGuessesLeft == 1:
#                 print("You have " + str(numberOfGuessesLeft) + " guess left. ")
#     print("______________________________________")
#     # Final messages.
#     if unguessedWord == word:
#         print("You win! ")
#         print("The word was " + word + ". ")
#         print("It took you " + str(numberOfGuesses - numberOfGuessesLeft) + " guesses. ")
#         if numberOfIncorrectGuesses == 0:
#             print("There are no incorrectly guessed letters. ")
#         else:
#             print("Your incorrectly guessed letters are " + guessedLettersIncorrect + ". ")
#     else:
#         print("You ran out of guesses. ")
#         print("The word was " + word + ". ")
#         if numberOfIncorrectGuesses == 0:
#             print("There are no incorrectly guessed letters. ")
#         else:
#             print("Your incorrectly guessed letters are " + guessedLettersIncorrect + ". ")
#     timesPlayed = timesPlayed + 1
#     # Gives the player an option whether they want to keep playing by changing the value determining whether the loop at the beginning will continue.
#     wantToContinue = input("Would you like to play again? Y/N: ")
# # End of game.
# print("Bye! Thank you for playing. ")





# Hangman program - description of code here
import random
wantToContinue = "Y"
loseLetterAfterCorrectGuess = "Y"
loseLetterAfterGuessingAgain = "Y"
timesPlayed = 0
message = "This is automatically on. "
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

    # Allows the user to change their settings.
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    if timesPlayed > 0:
        message = "Your settings are currently the same as last round. "

    changeSettings = input("Would you like to change your settings? Y/N: ")
    if changeSettings == "Y":
        print("______________________________________")
        loseLetterAfterCorrectGuess = input("- Would you like to lose letters after guessing correctly? " + message + "(" + (str(loseLetterAfterCorrectGuess)) + ") " + "Y/N: ")
        loseLetterAfterGuessingAgain = input("- Would you like to lose letters after guessing a letter you have guessed before? " + message + "(" + (str(loseLetterAfterGuessingAgain)) + ") " + "Y/N: ")
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")




    numberOfIncorrectGuesses = 0
    # Loops and asks the user to guess for the number of guesses allowed.
    for counter2 in range(numberOfGuesses):
        # Keeps looping until they guess the whole word.
        if unguessedWord != word:
            found = False
            print("______________________________________")
            guess = input("Enter your guess: ")
            guess = guess.lower()
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
            # Prints the number of guesses remaining. 





            # if loseLetterAfterCorrectGuess == "Y" and found == True: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
            numberOfGuessesLeft = numberOfGuessesLeft - 1







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
            print("There are no incorrectly guessed letters. ")
        else:
            print("Your incorrectly guessed letters are " + guessedLettersIncorrect + ". ")
    else:
        print("You ran out of guesses. ")
        print("The word was " + word + ". ")
        if numberOfIncorrectGuesses == 0:
            print("There are no incorrectly guessed letters. ")
        else:
            print("Your incorrectly guessed letters are " + guessedLettersIncorrect + ". ")
    timesPlayed = timesPlayed + 1
    # Gives the player an option whether they want to keep playing by changing the value determining whether the loop at the beginning will continue.
    wantToContinue = input("Would you like to play again? Y/N: ")
# End of game.
print("Bye! Thank you for playing. ")
