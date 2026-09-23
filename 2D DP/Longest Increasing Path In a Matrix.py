# You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

# Return the length of the longest strictly increasing path within matrix.

# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.

def longest(matrix):

    row = len(matrix)
    cols = len(matrix[0])

    memo = {}

    def recursion(r,c,prev_val):

        if r < 0 or c < 0 or r == row or c == cols or matrix[r][c] <= prev_val:
            return 0 

        if (r, c) in memo:
            return memo[(r,c)]

        res = 1 + max(recursion(r + 1, c, matrix[r][c]),
            recursion(r - 1, c, matrix[r][c]),
            recursion(r, c + 1, matrix[r][c]),
            recursion(r, c - 1, matrix[r][c]))

        memo[(r,c)] = res  
        return res 

    for r in range(row):
        for c in range(cols):
            recursion(r, c, -1)
            
    return max(memo.values())