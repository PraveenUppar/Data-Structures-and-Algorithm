# You are given a row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1.

# Return the perimeter of the island.

def perimeter(grid):

    row = len(grid)
    cols = len(grid[0])
    visited = set()

    def findperimeter(r,c):

        if r < 0 or c < 0 or r >= row or c >= cols or grid[r][c] == 0:
            return 1

        if (r,c) in visited:
            return 0

        visited.add((r,c))
        res = findperimeter(r + 1, c) + findperimeter(r - 1, c) + findperimeter(r, c + 1) + findperimeter(r, c - 1)
        return res


    for r in range(row):
        for c in range(cols):
            if grid[r][c] == 1:
                return findperimeter(r,c)
    return 0