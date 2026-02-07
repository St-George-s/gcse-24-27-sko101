exampleWord = "swoop"

wordGuessed = ""
display = ""

# while wordGuessed != exampleWord:
wordGuessed = input("guess: ").upper()
for counter in range(len(wordGuessed)):
    display = display + wordGuessed[counter] + " "
print(wordGuessed)
print(display)