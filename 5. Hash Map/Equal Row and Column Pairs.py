from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        count = 0

        # Step 1: Iterate through each row by its index 'i'
        for i in range(n):
            # Step 2: For each row, iterate through each column by its index 'j'
            for j in range(n):
                # Step 3: Assume the current row (grid[i]) and current column (column j) match
                match = True
                # Step 3a: Compare element by element
                for k in range(n):
                    # Compare grid[i][k] (k-th element of row i) with grid[k][j] (k-th element of column j)
                    if grid[i][k] != grid[k][j]:
                        match = False
                        break  # If a mismatch is found, this pair is not equal, so break the inner loop
                
                # Step 4: If 'match' is still True after comparing all elements, increment the count
                if match:
                    count += 1
        
        return count

# Test Cases
sol = Solution()

print(f"Grid: [[3,2,1],[1,7,6],[2,7,7]] -> {sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]])}")
# Expected: 1

print(f"Grid: [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]] -> {sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]])}")
# Expected: 3

print(f"Grid: [[1,1,1],[1,1,1],[1,1,1]] -> {sol.equalPairs([[1,1,1],[1,1,1],[1,1,1]])}")
# Expected: 9

print(f"Grid: [[1,2],[3,4]] -> {sol.equalPairs([[1,2],[3,4]])}")
# Expected: 0

print(f"Grid: [[0]] -> {sol.equalPairs([[0]])}")
# Expected: 1

print(f"Grid: [[1,0],[0,1]] -> {sol.equalPairs([[1,0],[0,1]])}")
# Expected: 0

print(f"Grid: [[5,5,5],[5,5,5],[5,5,5]] -> {sol.equalPairs([[5,5,5],[5,5,5],[5,5,5]])}")
# Expected: 9

print(f"Grid: [[1,2,3],[4,5,6],[7,8,9]] -> {sol.equalPairs([[1,2,3],[4,5,6],[7,8,9]])}")
# Expected: 0