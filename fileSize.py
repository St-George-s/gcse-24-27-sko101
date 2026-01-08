print("To find out the file size, please: ")
width = int(input("Enter your image width: "))
height = int(input("Enter your image height: "))
colourDepth = int(input("Enter your image colour depth: "))
fileSize = width * height * colourDepth
fileSizeInBytes = fileSize / 8
if fileSizeInBytes < 1:
    print("Your estimated file size is " + str(fileSize) + " in bits.")
else:
    print("Your estimated file size is " + str(fileSizeInBytes) + " in bytes.")
