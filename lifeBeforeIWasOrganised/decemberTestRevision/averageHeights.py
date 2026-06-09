# # 5 min task on average heights

# # Ver 1
# totalHeight = 0
# height = 0
# numberOfPeople = int(input("How many people are there?: "))
# for i in range(numberOfPeople):
#     height = float(input("Enter a height: "))
#     totalHeight = totalHeight + height
# print("The average of these heights is "  + str(totalHeight / numberOfPeople) + ".")

# # Ver 2
# totalHeight = 0
# numberOfPeople = int(input("How many people are there?: "))
# for i in range(numberOfPeople):
#     totalHeight = totalHeight + float(input("Enter a height: "))
# print("The average of these heights is "  + str(totalHeight / numberOfPeople) + ".")


# # 1. A programmer is developing a fitness app that will challenge the user to complete one of three physical activities each week. 
# # Write program code that will generate a random number between 1 and 3. [2] 
# # Create an algorithm that will generate a random number between 1 and 3 and then use this to display a message to either walk 10km, run 5km or swim 1km. [3] 

# import random
# myRandomNumber = random.randint(0, 2)
# walkRunSwim = ["walk 10km", "run 5km", "swim 1km"]
# print("This week you should " + walkRunSwim[myRandomNumber] + ".")

# # OR

# import random
# myRandomNumber = random.randint(1, 3)
# walkRunSwim = ["walk 10km", "run 5km", "swim 1km"]
# print("This week you should " + walkRunSwim[myRandomNumber - 1] + ".")


# # 2. Create an algorithm that will allow the user to enter a word and then count how many times the letter A appears in that word.
# # Both upper case (“A”) and lower case (“a”) letters must be counted.                                                                                                                                                                     
# # The algorithm should repeat until a word is entered that has 3 or more letter As. [4] 

# letterCount = 0
# cont = True
# while cont == True:
#     enteredWord = input("Enter a word: ").upper()
#     for letter in enteredWord:
#         if letter == "A":
#             letterCount = letterCount + 1
#     if letterCount >= 3:
#         cont = False
#     else:
#         print("Add another word. ")
# print("You have entered at least 3 a or As.")


# 3. The data below is stored in an array called trainingdata.
# The training sessions are stored in a text file called allsessions.txt 
# a) Finish the algorithm below to add the new trainingdata to the text file.  
# trainingdata = ["2", "New Trent Park", "True", "12.7"] [4] 
# b) Using the trainingdata array from the previous question, give the pseudocode that a programmer would use to output just the training venue details (“Bycars Park”) from this array.
# You may assume that the array is zero-indexed. [4] 


trainingdata = ["2", "New Trent Park", "True", "12.7"]
with open("decemberTestRevision/allsessions.txt", "w") as file:
    for item in trainingdata:
        file.write(item + "\n")



