# Question 12

import random
goodOrNaughty = "Neutral"
for numberOfChild in range(1, 11):
    randomScore = random.randint(1, 100)
    if randomScore > 50:
        goodOrNaughty = "Good"
    else:
        goodOrNaughty = "Naughty"
    print(str(numberOfChild) + ": " + str(randomScore) + ", " + str(goodOrNaughty) + ". ")

