


# Functions:

# Removes the guessed letter from the displayed keyboard if incorrect.
def removeLetterFromKeyboard(keyboard, keyboardLine2, keyboardLine3, letterGuessed):
    # Checks line 1 for the letter.
    for counter in range(len(keyboard)):
        if letterGuessed == keyboard[counter]:
            keyboard = keyboard[0:counter] + " " + keyboard[counter+1:]
    # Checks line 2 for the letter.
    for counter in range(len(keyboardLine2)):
        if letterGuessed == keyboardLine2[counter]:
            keyboardLine2 = keyboardLine2[0:counter] + " " + keyboardLine2[counter+1:]
    # Checks line 3 for the letter.
    for counter in range(len(keyboardLine3)):
        if letterGuessed == keyboardLine3[counter]:
            keyboardLine3 = keyboardLine3[0:counter] + " " + keyboardLine3[counter+1:]
    return keyboard, keyboardLine2, keyboardLine3


# Main code:
exampleWord = "swoop"

keyboard = "q w e r t y u i o p"
keyboardLine2 = " a s d f g h j k l"
keyboardLine3 = "   z x c v b n m"


wordGuessed = input("guess: ").upper()

keyboard, keyboardLine2, keyboardLine3 = removeLetterFromKeyboard(keyboard, keyboardLine2, keyboardLine3, wordGuessed)

print(keyboard)
print(keyboardLine2)
print(keyboardLine3)