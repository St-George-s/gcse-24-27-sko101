# notes

#areUHappy = "Y"
#while "Y":
#   print("This will go on forever. ")
#   areUHappy = input("Are u happy? Y/N: ")
#print("You are sad. ")


# # Question 11 
# # Write a Python program to keep asking for a code until it equals "rzy" and print "Code accepted" once the user enters "rzy". 

# code = input("Enter the code: ")
# while code != "rzy":
#     print("Code not accepted. ")
#     code = input("Enter the code: ")
# print("Code accepted. ")

# #  Question 12 
# # Write a Python program to keep asking for a code until it equals 4003 and print "Code accepted" when the code is correct. 

# code1 = input("Enter the code: ")
# while code1 != "4003":
#     print("Code not accepted. ")
#     code1 = input("Enter the code: ")
# print("Code accepted. ")


# # Question 13 
# # Write a Python program to keep asking for the user's age until it is over 14 and print "Age accepted" once the user enters an age over 14. 

# usersAgeOver14 = int(input("Enter your age as a number: "))
# while int(usersAgeOver14) <= 14:
#     print("Age not accepted. You are too young. ")
#     usersAgeOver14 = input("Enter your age as a number: ")
# print("Age accepted. ")


# # Question 14 
# # Write a Python program to keep asking the user to input a password until it is longer than 5 characters and print "Password accepted" once the password is longer than 5 characters. 

# passwordOver5 = input("Enter a password with over 5 characters: ")
# while len(passwordOver5) <= 5:
#     print("Password not accepted. It is too short. Try again. ")
#     passwordOver5 = input("Enter a password with over 5 characters: ")
# print("Password accepted. ")


# # Question 15 
# # Write a Python program to ask the user if they would like to watch another episode of Modern Family.
# # If they enter the word "yes," then print "playing another episode" and repeat. Otherwise, print "See you later!" and stop. 

# watchMore = input("Would you like to watch an episode of Modern Family (Yes/No): ")
# while watchMore == "Yes":
#     print("Playing an episode. ")
#     watchMore = input("Would you like to watch another episode? ")
# print("See you later! ")


# # Question 16 
# # Write a Python program to keep asking for money until the total amount of money is greater than 100. Print "I accept your offer" once the total money is greater than 100. 

# howMuchMoneyDoUOffer = input("How much money do you offer? ")
# while int(howMuchMoneyDoUOffer) <= 100:
#     print("That's way too little! ")
#     howMuchMoneyDoUOffer = input("How about some more? How much money do you offer? ")
# print("That'll do. I accept your offer. ")


# Extension Activity 
# Write a Python program that simulates an ATM machine: 
# Start with a balance of £100. 
# Keep asking the user if they want to deposit, withdraw, or quit. 
# If they deposit, ask how much and add it to the balance. 
# If they withdraw, ask how much and subtract it (only if there’s enough money). 
# Print the balance after each transaction. 
# The loop should stop when the user types quit. 


# balance = 100
#     dWQ = input("Do you want to Deposit, Withdraw, Quit, or Check Balance? ")
#     while dWQ == "Deposit":
#         howMuchDeposit = input("How much do you want to deposit? ")
#         balance = int(balance) + int(howMuchDeposit)
#         dWQ = input("Do you want to Deposit, Withdraw, Quit, or Check Balance? ")
#     while dWQ == "Withdraw":
#         howMuchWithdraw = input("How much do you want to withdraw? ")
#         balance = int(balance) - int(howMuchWithdraw)
#         if balance < 0:
#             print("You do not have enough money. ")
#             balance = int(balance) + int(howMuchWithdraw)
#         dWQ = input("Do you want to Deposit, Withdraw, Quit, or Check Balance? ")
#     if dWQ == "Quit":
#         print("Thank you for using Alina's ATM. Have a nice day!")




# # extra check balance function because it is an ATM and so otherwise how would you use it
# balance = 100
# dWQ = "yay"
# while dWQ != "Quit":
#     dWQ = input("Do you want to Deposit, Withdraw, Quit, or Check Balance? ")
#     if dWQ == "Deposit":
#         howMuchDeposit = input("How much do you want to deposit? ")
#         balance = int(balance) + int(howMuchDeposit)
#     if dWQ == "Withdraw":
#         howMuchWithdraw = input("How much do you want to withdraw? ")
#         balance = int(balance) - int(howMuchWithdraw)
#         if balance < 0:
#             print("You do not have enough money. ")
#             balance = int(balance) + int(howMuchWithdraw)
#     if dWQ == "Check Balance":
#         print("Your balance is " + str(balance) + ". ")
# print("Thank you for using Alina's ATM. Have a nice day!")


# extra check balance function because it is an ATM and so otherwise how would you use it as well as accounts, passwords, transferring money across accounts and also log out

# Accounts: muskarasAcc90, EFFBSIHHHHHHSCCCOBRB21_100, fifisAcc110
# Passwords: 90code, 100code, 110code
# Starting balances: 90, 100, 110


print("Welcome to Alina's ATM.")

muskarasAcc90balance = 90
EFFBSIHHHHHHSCCCOBRB21_100balance = 100
fifisAcc110balance = 110


account = input("Enter a username: ")
if account == "muskarasAcc90":
    balance = muskarasAcc90balance 
    user = "Muskaan"
    muskarasAcc90code = input("Enter your passcode: ")
    while muskarasAcc90code != "90code":
        balance = muskarasAcc90balance
        print("Password is incorrect. ")
        muskarasAcc90code = input("Enter your passcode: ")
if account == "EFFBSIHHHHHHSCCCOBRB21_100":
    balance = EFFBSIHHHHHHSCCCOBRB21_100balance
    user = "Elizabeth"
    EFFBSIHHHHHHSCCCOBRB21_100code = input("Enter your passcode: ")
    while EFFBSIHHHHHHSCCCOBRB21_100code != "100code":
        print("Password is incorrect. ")
        EFFBSIHHHHHHSCCCOBRB21_100code = input("Enter your passcode. ")
if account == "fifisAcc110":
    balance = fifisAcc110balance
    user = "Alina"
    fifisAcc110code = input("Enter your passcode: ")
    while fifisAcc110code != "110code":
        print("Password is incorrect. ")
        fifisAcc110code = input("Enter your passcode: ")
print("Password accepted. ")


dWQ = "it doesn't really matter what I write here"
while dWQ != "Quit":
    dWQ = input("Do you want to Deposit, Withdraw, Quit, Check Balance, Log Out, or Transfer? ")
    if dWQ == "Deposit":
        howMuchDeposit = input("How much do you want to deposit? ")
        balance = int(balance) + int(howMuchDeposit)
    if dWQ == "Withdraw":
        howMuchWithdraw = input("How much do you want to withdraw? ")
        balance = int(balance) - int(howMuchWithdraw)
        if balance < 0:
            print("You do not have enough money. ")
            balance = int(balance) + int(howMuchWithdraw)
    if dWQ == "Check Balance":
        print("Your balance is " + str(balance) + ". ")
    if dWQ == "Log Out":
        print("Thank you for using Alina's ATM. Have a nice day!")
        if user == "Muskaan":
            muskarasAcc90balance = balance
        if user == "Elizabeth":
            EFFBSIHHHHHHSCCCOBRB21_100balance = balance
        if user == "Alina":
            fifisAcc110balance = balance
        account = input("Enter a username: ")
        if account == "muskarasAcc90":
            balance = muskarasAcc90balance 
            user = "Muskaan"
            muskarasAcc90code = input("Enter your passcode: ")
            while muskarasAcc90code != "90code":
                balance = muskarasAcc90balance
                print("Password is incorrect. ")
                muskarasAcc90code = input("Enter your passcode: ")
        if account == "EFFBSIHHHHHHSCCCOBRB21_100":
            balance = EFFBSIHHHHHHSCCCOBRB21_100balance
            user = "Elizabeth"
            EFFBSIHHHHHHSCCCOBRB21_100code = input("Enter your passcode: ")
            while EFFBSIHHHHHHSCCCOBRB21_100code != "100code":
                print("Password is incorrect. ")
                EFFBSIHHHHHHSCCCOBRB21_100code = input("Enter your passcode. ")
        if account == "fifisAcc110":
            balance = fifisAcc110balance
            user = "Alina"
            fifisAcc110code = input("Enter your passcode: ")
            while fifisAcc110code != "110code":
                print("Password is incorrect. ")
                fifisAcc110code = input("Enter your passcode: ")
        print("Password accepted. ")
    if dWQ == "Transfer":
        howMuchToTransfer = input("How much would you like to transfer? ")
        toWhomShouldItBeTransferred = input("To whom should it be transferred? ")
        balance = int(balance) - int(howMuchToTransfer) 
        if toWhomShouldItBeTransferred == "muskarasAcc90":
            muskarasAcc90balance = int(muskarasAcc90balance) + int(howMuchToTransfer)
            if balance < 0:
                print("You do not have enough money. ")
                muskarasAcc90balance = int(muskarasAcc90balance) - int(howMuchToTransfer)
                balance = int(balance) + int(howMuchToTransfer)
        if toWhomShouldItBeTransferred == "EFFBSIHHHHHHSCCCOBRB21_100":
            EFFBSIHHHHHHSCCCOBRB21_100balance = int(EFFBSIHHHHHHSCCCOBRB21_100balance) + int(howMuchToTransfer)
            if balance < 0:
                print("You do not have enough money. ")
                EFFBSIHHHHHHSCCCOBRB21_100balance = int(EFFBSIHHHHHHSCCCOBRB21_100balance) - int(howMuchToTransfer)
                balance = int(balance) + int(howMuchToTransfer)
        if toWhomShouldItBeTransferred == "fifisAcc110":
            fifisAcc110balance = int(fifisAcc110balance) + int(howMuchToTransfer)
            if balance < 0:
                print("You do not have enough money. ")
                fifisAcc110balance = int(fifisAcc110balance) - int(howMuchToTransfer)
                balance = int(balance) + int(howMuchToTransfer)
        

print("Thank you for using Alina's ATM. Have a nice day!")







# fix: when you type in a number it gets confused





#transfer prototype

# if dWQ == "Transfer":
#         howMuchToTransfer = input("How much would you like to transfer? ")
#         toWhomShouldItBeTransferred = input("To whom should it be transferred? ")
#         if toWhomShouldItBeTransferred == "muskarasAcc90":
#             muskarasAcc90balance = int(muskarasAcc90balance) + int(howMuchToTransfer)
#         if balance < 0:
#             print("You do not have enough money. ")
#             balance = int(muskarasAcc90balance) + int(howMuchToTransfer)