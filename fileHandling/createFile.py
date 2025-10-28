# # wantToContinue = True
# # while wantToContinue == True:

# Write:
with open("/workspaces/gcse-24-27-sko101/fileHandling/whatIDidInMyHolidays.txt", "w") as file:
    file.write(input("Begin writing: "))
# Append:
with open("/workspaces/gcse-24-27-sko101/fileHandling/whatIDidInMyHolidays.txt", "a") as file:
    file.write("\n")
    file.write(input(""))
# Read:
with open("/workspaces/gcse-24-27-sko101/fileHandling/whatIDidInMyHolidays.txt", "r") as file:
    content = file.read()
    print(content)
# Count Lines:
with open("/workspaces/gcse-24-27-sko101/fileHandling/whatIDidInMyHolidays.txt", "r") as file:
    counter = 0
    for line in file:
        counter = counter + 1
    print("There are ", counter, " lines. ")    
