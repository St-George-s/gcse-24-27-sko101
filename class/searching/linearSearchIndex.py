# Linear search
# Create an array
names= ["Debbie", "Jessie", "Vigdis", "Emilia"]
searchValue = "Emilia"
found = False
index = 0

# Conditional loop that stops when either the search value is found or the search is at the end of the list.
# while not found is the same as while found == false
while not found and index < len(names):
    if searchValue == names[index]:
        found = True
    else:
        index += 1
# After the loop (unindent)
if found:
    print("Found at index " + str(index) + ". ")
else:
    print("Not found. ")