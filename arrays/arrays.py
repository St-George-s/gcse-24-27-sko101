# Create arrays
heights = [2.4, 3.8, 0.4, 1.9]
names = ["Bob", "Dave", "Simon", "John"]

# Arrays start counting from 0, therefore 2.4 and Bob would be heights[0] and names[0]
print(names[1]) # Prints Dave
print(heights[1]) # Prints 3.8

# Loop over names array and print
for counter in range(len(names)):
    print(names[counter]) # Counter is 0 then 1 then 2
    print(heights[counter])

# Append (add) to an array (the end)
heights.append(2.2)
names.append("Jimmy")

print(heights)
print(names)