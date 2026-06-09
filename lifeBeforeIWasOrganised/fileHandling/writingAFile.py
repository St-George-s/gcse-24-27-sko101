#create and write
with open("practice.txt", "w") as file:
    for counter in range(1000):
        file.write("Hello world.\n")
