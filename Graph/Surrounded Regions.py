# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.

# Region: To form a region connect every 'O' cell. 
# Regions can have any shape; they do not need to be squares or rectangles.

# Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. 
# Such regions are completely enclosed by 'X' cells.

# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. 
# You do not need to return anything.

def region(grid):

    row = len(grid)
    cols = len(grid[0])

    def explore(r,c):
        if r < 0 or c < 0 or r >= row or c >= cols or grid[r][c] != "O":
            return 

        grid[r][c] = "S"

        explore(r + 1,c)
        explore(r - 1,c)
        explore(r,c + 1)
        explore(r,c - 1)

    for r in range(row):
        explore(r, 0)
        explore(r, cols - 1)

    for c in range(cols):
        explore(0, c)
        explore(row - 1, c)

    for r in range(row):
        for c in range(cols):
            if grid[r][c] == "O":
                grid[r][c] = "X"
            elif grid[r][c] == "S":
                grid[r][c] = "O"