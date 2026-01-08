# print("To find out the file size, please: ")
# width = int(input("Enter your image width: "))
# height = int(input("Enter your image height: "))
# colourDepth = int(input("Enter your image colour depth: "))
# fileSize = width * height * colourDepth
# fileSizeInBytes = fileSize / 8
# if fileSizeInBytes < 1:
#     print("Your estimated file size is " + str(fileSize) + " in bits.")
# else:
#     print("Your estimated file size is " + str(fileSizeInBytes) + " in bytes.")




# wantToContinue = True
# stayInBits = False
# bbkmgtpCounter = 0
# bbkmgtp = ["bits", "bytes", "kilobytes", "megabytes", "gigabytes", "terabytes", "petabytes"]
# while wantToContinue == True:
#     print("To find out the file size, please: ")
#     width = int(input("Enter your image width: "))
#     height = int(input("Enter your image height: "))
#     colourDepth = int(input("Enter your image colour depth: "))
#     fileSize = width * height * colourDepth
#     if fileSize > 1:
#         fileSize = fileSize / 8
#         bbkmgtpCounter = 1
#         if fileSize < 1:
#             fileSize = fileSize * 8
#             bbkmgtpCounter = bbkmgtpCounter - 1
#     while fileSize > 1:
#         fileSize = fileSize * 1000
#         bbkmgtpCounter = bbkmgtpCounter + 1
#     if fileSize < 1:
#             fileSize = fileSize * 1000
#             bbkmgtpCounter = bbkmgtpCounter - 1
#     print("Your estimated file size is " + str(fileSize) + " in " + bbkmgtp[bbkmgtpCounter] + ". ")



print("To find out the file size, please: ")
width = int(input("Enter your image width: "))
height = int(input("Enter your image height: "))
colourDepth = int(input("Enter your image colour depth: "))
fileSize = width * height * colourDepth
fileSize2 = fileSize / 8
if fileSize2 < 1:
    print("Your estimated file size is " + str(fileSize) + " in bits.")
else:
    while fileSize2 > 1:
        fileSize2 = fileSize2 * 1000    
print("Your estimated file size is " + str(fileSize2) + " in bytes.")



