grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]

# grid = [["0", "1", "1", '1', "0", '0', "0"],
#         ["0", "0", "1", "1", "0", "1", "0"]]


def dfs(grid, r, c):
    grid[r][c] = 0
    # This is just for horizontally and vertically connected 1's if diagonally is also mentioned added this [r+1, c+1], [r-1, c-1], [r-1, c+1], [r+1, c-1] to the list with the previously added elements
    lst = [[r-1, c], [r+1, c], [r, c-1], [r, c+1]]

    for row, column in lst:
        if row >= 0 and column >= 0 and row < len(grid) and column < len(grid[row]) and grid[row][column] == "1":
            dfs(grid, row, column)


def numIslands(grid):

    number_of_islands = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[r][c] == "1":
                dfs(grid, r, c)
                number_of_islands += 1

    return number_of_islands


print(numIslands(grid))
