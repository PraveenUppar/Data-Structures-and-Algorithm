class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        row = len(matrix)
        col = len(matrix[0])

        left = 0
        right = (row * col) - 1

        while left <= right:
            i = left + (right - left) // 2
            search_row = i // col
            search_col = i % col
            if target > matrix[search_row][search_col]:
                left = i + 1
            elif target < matrix[search_row][search_col]:
                right = i - 1
            else:
                return True
        return False

        # Brute Force - O(n**2)
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if matrix[i][j] == target:
        #             return True
        # return False
        