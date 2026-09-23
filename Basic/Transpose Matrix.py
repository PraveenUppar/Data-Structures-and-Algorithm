# You are given a 2D integer array matrix, return the transpose of matrix.

# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

def transpose(matrix):

    res = []

    for c in range(len(matrix[0])):
        temp = []
        for r in range(len(matrix)):
            temp.append(matrix[r][c])
        res.append(temp)
    return res