# weather = input("Enter weather (sunny/rain)")
# timeOfDay = input("Enter time (day/night)")

# if weather == "sunny" and timeOfDay == "day":
#     print("Nice")
# elif weather == "rain" and (timeOfDay == "day" or timeOfDay == "night"):
#     "Bring an umbrella"




# # Question 1
# # Write a Python program that checks if a swimmer’s time is under 60 seconds and prints whether they qualify.
# swimTime = float(input("Enter your swim time: "))
# if swimTime < 60.0:
#     print("Participant qualifies. ")
# else:
#     print("Participant does not qualify. ")

# # Question 2
# # Write a Python program that categorises swimmers into Gold, Silver, Bronze, or Not Qualified based on their times.

# swimTime = float(input("Enter your swim time: "))
# if swimTime < 55.0:
#     print("Participant qualifies for gold category. ")
# elif swimTime > 55.0 and swimTime <= 60.0:
#     print("Participant qualifies for silver category. ")
# elif swimTime > 60.0 and swimTime < 65.0:
#     print("Participant qualifies for bronze category. ")
# else:
#     print("Participant does not qualify. ")

# # Question 3
# # Write a Python program that asks for freestyle, backstroke, and butterfly times, then prints which strokes the swimmer qualifies for.

# freestyleTime = float(input("Enter your freestyle time: "))
# backstrokeTime = float(input("Enter your backstroke time: "))
# butterflyTime = float(input("Enter your butterfly time: "))
# if freestyleTime < 60:
#     print("You have qualified for freestyle. ")
# else:
#     print("You have not qualified for freestyle. ")
# if backstrokeTime < 60:
#     print("You have qualified for backstroke. ")
# else:
#     print("You have not qualified for backstroke. ")
# if butterflyTime < 60:
#     print("You have qualified for butterfly. ")
# else:
#     print("You have not qualified for butterfly. ")


# # Question 4
# # Write a Python program that uses conditional logic to check if a swimmer qualifies for multiple strokes at once (e.g., Freestyle and Backstroke, Freestyle and Butterfly).

# freestyleTime = float(input("Enter your freestyle time: "))
# backstrokeTime = float(input("Enter your backstroke time: "))
# butterflyTime = float(input("Enter your butterfly time: "))

# if freestyleTime < 60:
#     print("You qualified for freestyle only. ")
# elif freestyleTime < 60 and backstrokeTime < 60:
#     print("You qualified for freeestyle and backstroke")

#     # not done


# # Question 5
# # Write a Python program that assigns values to variables representing the temperature and whether it is sunny. Check if the temperature is greater than 15 and it is sunny. Print the result.

# temp = float(input("Enter the temperature: "))
# weather = input("Is it sunny (Yes/No): ")

# if temp > 15.0 and weather == "Yes":
#     print("The weather is good today. ")
# else:
#     print("The weather is not that good today. ")


# Question 6
# Write a Python program that assigns values to variables representing the temperature and whether it is raining. Check if the temperature is greater than 15 or it is raining. Print the result.

