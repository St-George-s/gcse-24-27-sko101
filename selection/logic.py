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


# # Question 6 or 2
# # Write a Python program that assigns values to variables representing the temperature and whether it is raining.
# # Check if the temperature is greater than 15 or it is raining. Print the result.

# temp = float(input("Please enter the temperature: "))
# sunOrRain = input("Please enter the weather (Sun/Rain): ")
# if temp < 15.0 and sunOrRain == "Rain":
#     print("It is under 15 degrees and raining, so it is cold and wet. ")
# elif temp < 15.0 and sunOrRain == "Sun":
#     print("It is under 15 degrees but sunny, so it is cold and dry. ")
# elif temp >= 15.0 and sunOrRain == "Rain":
#     print("It is over or equal to 15 degrees and raining, so it is warm and wet. ")
# else:
#     print("It is over 15 degrees and sunny, so it is warm and dry. ")

# # Question 3
# # Write a Python program that assigns a value to a variable representing the number of apples.
# # Check if the number of apples is not greater than 10. Print the result. 

# numberOfApples = int(input("Please enter the number of apples: "))
# if numberOfApples <= 10:
#     print("You have 10 or less apples. ")
# else:
#     print("You have more than 10 apples. ")

# # Question 4
# # Write a Python program that assigns values to variables representing a person’s age and whether they have a driving licence.
# # Check if the person is older than 18 and has a driving licence. Print the result. 

# ageOfPotentialDriver = int(input("Enter your age: "))
# drivingLicense = input("Do you have a license (Yes/No): ")
# if ageOfPotentialDriver >= 18 and drivingLicense == "Yes":
#     print("You can drive. ")
# else:
#     print("Please stay off the roads. ")

# # Question 5
# # Write a Python program that assigns values to variables representing the speed of a car and whether it is raining.
# # Check if the speed is greater than 60 or it is not raining. Print the result. 

# speedOfCar = int(input("Enter the speed of the car if you are not driving because that would be unsafe: "))
# rainLevel = input("Is it raining (Yes/No): ")
# if speedOfCar > 60 and rainLevel == "No":
#     print("Be careful!")
# elif speedOfCar > 60 and rainLevel == "Yes":
#     print("It's probably not safe to drive that fast in that weather. Slow down!")
# else:
#    print("Have a safe trip. ")

# # Question 6
# # Write a Python program that assigns values to variables representing the number of hours studied and whether the student feels prepared.
# # Check if the number of hours studied is greater than 5 or the student feels prepared.
# # Use parentheses to ensure that the or condition is evaluated first. Print the result. 

# hoursStudied = int(input("Enter how many hours you have studied for: "))
# feelPrepped = input("Enter if you feel prepared (Yes/No): ")

# if (hoursStudied > 5) or (feelPrepped == "Yes"):
#     print("I'm sure you'll pass! ")
# else:
#     print("Don't worry, just study some more. ")