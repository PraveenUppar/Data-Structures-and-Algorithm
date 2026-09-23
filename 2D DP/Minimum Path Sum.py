# You are given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, 
# which minimizes the sum of all numbers along its path.

def find(grid):

    row = len(grid)
    cols = len(grid[0])

    memo = {}

    def recursion(i, j):

        if i == row - 1 and j == cols - 1:
            return grid[i][j]

        if i == row and j == cols:
            return float("inf")

        if (i,j) in memo:
            return memo[(i,j)]

        res = grid[i][j] + min(recursion(i + 1, j), recursion(i, j + 1))
        memo[(i,j)] = res
        return res

    recursion(0,0)