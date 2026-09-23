# You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
# The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). 
# The robot can only move either down or right at any point in time.

# An obstacle and space are marked as 1 or 0 respectively in grid. 
# A path that the robot takes cannot include any square that is an obstacle.

# Return the number of possible unique paths that the robot can take to reach the bottom-right corner

def unique(grid):
    row = len(grid)
    cols = len(grid[0])

    memo = {}

    def recursion(i,j):

        if i == row or j == cols or grid[i][j] == 1:
            return 0
        
        if i == row - 1 and j == cols - 1:
            return 1

        if (i, j) in memo:
            return memo[(i, j)]

        res = recursion(i + 1, j) + recursion(i, j + 1)
        memo[(i, j)] = res
        return res

    return recursion(0,0)