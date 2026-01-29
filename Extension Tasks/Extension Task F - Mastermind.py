
# Extension Task F 
# Mastermind 
# Generate a random four digit number.
# The player has to keep inputting four digit numbers until they guess the randomly generated number.
# After each unsuccessful try it should say how many numbers they got correct, but not which position they got right.
# At the end of the game should congratulate the user and say how many tries it took. 
# Optional Extensions:  
# Let the user pick an easy mode which shows the user which position that they guessed correctly 
# Let the user pick a hard mode that gives five digits instead of four 
# After the game is finished, ask the user for their name and input their score into a table.
# Show them the high score at the start of the game so that it gives a sense of competition. 

import random
randomNumber = str(random.randint(1, 1000))
while len(randomNumber) > 4:
    randomNumber = str(str("0") + str(randomNumber))
print(randomNumber)
