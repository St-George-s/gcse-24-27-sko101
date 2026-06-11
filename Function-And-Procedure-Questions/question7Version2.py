# Version 2

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_grid(grid):
    for counter in range(len(grid)):
        rowPrint = ""
        for counterTwo in range(len(grid[counter])):
            rowPrint += str(grid[counter][counterTwo]) + " "
        print(rowPrint)

print_grid(grid)

