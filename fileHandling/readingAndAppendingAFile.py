#read
with open("/workspaces/gcse-24-27-sko101/fileHandling/practiceRead.txt", "r") as file:
    content = file.read()
    print(content)

#append
with open("/workspaces/gcse-24-27-sko101/fileHandling/practiceRead.txt", "a") as file:
    file.write("\nThis is a new line added later.")