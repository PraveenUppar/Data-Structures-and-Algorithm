# There is an m x n grid where you are allowed to move either down or to the right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that can be taken 
# from the top-left corner of the grid (grid[0][0]) to the bottom-right corner (grid[m - 1][n - 1]).

def unique(m, n):

    memo = {}

    def recursion(i, j):

        if i == (m - 1) and j == (n - 1):
            return 1

        if i >= m or j >= n:
            return 0

        if (i,j) in memo:
            return memo[(i, j)]

        res = recursion(i, j + 1) + recursion(i + 1, j)
        memo[(i,j)] = res
        return res

    recursion(0,0)