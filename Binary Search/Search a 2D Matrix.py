# You are given an m x n 2-D integer array matrix and an integer target.

# Each row in matrix is sorted in non-decreasing order.
# The first integer of every row is greater than the last integer of the previous row.
# Return true if target exists within matrix or false otherwise.

def grid(matrix, target):
   
    ROWS = len(matrix)
    COLS = len(matrix[0])

    l = 0
    r = ROWS * COLS - 1

    while l <= r:
        m = l + (r - l) // 2
        row = m // COLS
        col =  m % COLS
        if target > matrix[row][col]:
            l = m + 1
        elif target < matrix[row][col]:
            r = m - 1
        else:
            return True
    return False