# Given a square n x n matrix of integers matrix, rotate it by 90 degrees clockwise.

# You must rotate the matrix in-place. Do not allocate another 2D matrix and do the rotation.


def image(matrix):
    res = []
    
    for c in range(len(matrix[0])):
        temp = []
        for r in range(len(matrix)):
            temp.append(matrix[r][c])
        res.append(temp)
    return res.reverse()