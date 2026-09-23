# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

def max_area(grid):

    row = len(grid)
    cols = len(grid[0])
    res = 0
    visited = set()

    def findarea(r,c):

        if r < 0 or c < 0 or r >= row or c >= cols or (r,c) in visited or grid[r][c] == 0:
            return 0

        visited.add((r,c))

        curr_area = findarea(r + 1, c) + findarea(r - 1, c) + findarea(r, c + 1) + findarea(r, c - 1) + 1
        return curr_area 

    for r in range(row):
        for c in range(cols):
            if grid[r][c] == 1:
                area = findarea(r,c)
                res = max(res, area)
    return res
