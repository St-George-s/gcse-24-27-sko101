exampleWord = "swoop"


keyboard = "q w e r t y u i o p"
keyboardLine2 = "a s d f g h j k l"
keyboardLine3 = "z x c v b n m"

letterGuessed = input("guess: ")
for counter in range(len(keyboard)):
    if letterGuessed == keyboard[counter]:
        keyboard = keyboard[0:counter] + " " + keyboard[counter+1:]
print(keyboard)