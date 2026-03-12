# Linear search
# Create an array



# def linearSearch(searchValue):
#     names= ["Debbie", "Jessie", "Vigdis", "Emilia"]
#     index = 0
#     found = False
#     while not found and index < len(names):
#         if searchValue == names[index]:
#             found = True
#         else:
#             index += 1
#     return found
# searchValue = "Emilia"
# found = linearSearch(searchValue)


# # After the function
# if found:
#     print("Found. ")
# else:
#     print("Not found. ")



# OR




def linearSearch(searchValue, searchList):
    index = 0
    found = False
    while not found and index < len(searchList):
        if searchValue == searchList[index]:
            found = True
        else:
            index += 1
    return found
searchValue = "Emilia"
searchList= ["Debbie", "Jessie", "Vigdis", "Emilia"]
found = linearSearch(searchValue, searchList)


# After the function
if found:
    print("Found. ")
else:
    print("Not found. ")