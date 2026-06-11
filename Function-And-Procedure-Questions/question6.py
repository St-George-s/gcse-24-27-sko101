def linear_search(numbers, target):
    found = False
    for counter in range(len(numbers)):
        if numbers[counter] == target:
            found = True
            break
    return found
    


numbers = [3, 8, 2, 10, 7]
print(linear_search(numbers, 10))