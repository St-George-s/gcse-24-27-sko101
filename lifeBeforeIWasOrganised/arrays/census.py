# # Task 1: Create an Array - This is actually Task 2
# # Create an Array:
# # Create an array called cityNames to store the names of five cities in the UK.
# # Add the following cities to the array: London, Edinburgh, Cardiff, Belfast, and Glasgow.
# # Write a code to display each city's name individually.

# cityNames = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow"]
# for counter in range(len(cityNames)):
#     print(cityNames[counter])


# # Task 3: Introduce Parallel Arrays
# # Create a Parallel Array for Population Data:
# # Create a second array called population that stores the population of each city (in thousands) corresponding to the order in cityNames.
# # Use these population values: 8908, 482, 366, 341, 635.
# # Write a loop to print each city name along with its corresponding population.

# # Parallel
# cityNamesTaskThree = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow"]
# population = [8908, 482, 366, 341, 635]
# for counter in range(len(cityNamesTaskThree)):
#     print(cityNamesTaskThree[counter] + " has a population of " + str(population[counter]) + ". ")


# Task 4: Linear Search for City Population
# Perform a Linear Search to Find City Population:
# Prompt the user to enter the name of a city.
# Write a code that performs a linear search to find the entered city's population.
# If the city is found in the list, print the city's name and its population.
# If the city is not in the list, display a message that the city is not found.

found = False
cityNames = ["London", "Edinburgh", "Cardiff", "Belfast", "Glasgow"]
population = [8908, 482, 366, 341, 635]
usersCity = input("Please enter a name of a city: ")
for counter in range(len(cityNames)):
    if usersCity == cityNames[counter]:
        print(cityNames[counter] + " has a population of " + str(population[counter]) + ". ")
        found = True
if not found:
    print("Your city was not found. ")