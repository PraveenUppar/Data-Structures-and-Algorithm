# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

def island(grid):

    row = len(grid)
    cols = len(grid[0])
    res = 0

    def countIsland(r,c):

        if r < 0 or c < 0 or r >= row or c >= cols or grid[r][c] == "0":
            return

        if grid[r][c] == "1":
            grid[r][c] = "0"

        countIsland(r + 1, c)
        countIsland(r - 1, c)
        countIsland(r, c + 1)
        countIsland(r, c - 1)

    for r in range(row):
        for c in range(cols):
            if grid[r][c] == "1":
                countIsland(r,c)
                res += 1
    return res