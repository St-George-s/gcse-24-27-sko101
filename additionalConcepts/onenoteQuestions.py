# 4. ❓ String manipulation and random numbers 

# # 1: Write a Python program to extract the first and last characters of a string entered by the user. 
# usersString = input("Enter a sentence: ")
# print(usersString[0])
# print(usersString[-1])

# # 2: Write a Python program to reverse a string entered by the user. 
# userString = input("Enter a sentence: ")
# reversedString = ""
# for character in userString:
#     reversedString = character + reversedString
# print(reversedString)

# # 3: Write a Python program to check if a string is a palindrome (reads the same forward and backward). 
# userString = input("Enter a sentence: ")
# reversedString = ""
# for character in userString:
#     reversedString = character + reversedString
# if userString == reversedString:
#     print("It is a palindrome. ")
# else:
#     print("It is not a palindrome. ")

# 4: Write a Python program to count the number of vowels in a string. 
userNewString = input("Enter a new sentence: ")
vowels = ["a", "e", "i", "o", "u"]
vowelsInWord = 0
for character in userNewString:
    if character == vowels[character]:
        vowelsInWord = vowelsInWord + 1
if vowelsInWord > 0:
    print("There are ", str(vowelsInWord), " vowels in your sentence. ")
else:
    print("There are no vowels in your sentence. ")

# for character in userNewString:
#     if userNewString[character] == vowels:
#         vowelsInWord = vowelsInWord + 1

# # 6: Generate and print one random integer from 1 to 6. 
# import random
# randomInteger = random.randint(1, 6)
# print(randomInteger)

# # 7: Roll two dice (1–6) and print both values and their total using + string concatenation. 
# import random
# myFirstDice = random.randint(1, 6)
# mySecondDice = random.randint(1, 6)
# print(str(myFirstDice), " + ", str(mySecondDice), " =")
# print(str(myFirstDice + mySecondDice))
