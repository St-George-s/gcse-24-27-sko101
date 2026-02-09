exampleWord = "swoop"
display = "1:   "
wordGuessed = ""
wordHasBeenGuessed = False
keyboard = "q w e r t y u i o p"
keyboardLine2 = " a s d f g h j k l"
keyboardLine3 = "   z x c v b n m"
alphabet = "abcdefghijklmnopqrstuvwxyz"

wordGuessed = "sweep"
correctLetters = ""
yes = 0

# Searches words for matching letters.
for counter in range(len(wordGuessed)):
    for counter2 in range(len(exampleWord)):
        if wordGuessed[counter] == exampleWord[counter2]:
            correctLetters = correctLetters + wordGuessed[counter]
            yes = yes + 1

print(yes)
print(correctLetters)

incorrectLetters = wordGuessed
no = 0

for counter in range(len(wordGuessed)):
    for counter2 in range(len(correctLetters)):
        if wordGuessed[counter] == correctLetters[counter2]:
            incorrectLetters = incorrectLetters[0:counter] + " " + incorrectLetters[counter+1:]
            no = no + 1
print(no)
print(alphabet)
print(incorrectLetters)