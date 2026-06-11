# Version 1

grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def print_grid(grid):
    for counter in range(len(grid)):
        for counter in range(len(grid)):
            print(grid[counter][0], grid[counter][1], grid[counter][2])
        break
print_grid(grid)