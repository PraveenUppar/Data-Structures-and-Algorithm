#  prefix sum of a matrix is a powerful technique used to efficiently compute the sum of elements in a submatrix.

# A prefix sum matrix is a new matrix sum[][] where:
# sum[i][j] represents the sum of all elements in the rectangle from (0,0) to (i-1,j-1) in the original matrix.


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        # prefix[i][j] = matrix[i][j] + top + left - top_left
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                top = self.prefix[i-1][j] if i > 0 else 0
                left = self.prefix[i][j-1] if j > 0 else 0
                diag = self.prefix[i-1][j-1] if i > 0 and j > 0 else 0

                self.prefix[i][j] = matrix[i][j] + top + left - diag

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        total = self.prefix[row2][col2]
        top = self.prefix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix[row2][col1-1] if col1 > 0 else 0
        diag = self.prefix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + diag
            
