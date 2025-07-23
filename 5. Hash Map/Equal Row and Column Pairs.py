class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        n = len(grid)
        count = 0

        # Step 1: Iterate through each row
        for i in range(n):
            # Step 2: For each row, iterate through each column
            for j in range(n):
                # Step 3: Compare current row (grid[i]) with current column (grid[][j])
                match = True
                for k in range(n):
                    # Compare element grid[i][k] (from row i) with grid[k][j] (from column j)
                    if grid[i][k] != grid[k][j]:
                        match = False
                        break  # No need to compare further elements for this pair

                # Step 4: If all elements matched, increment count
                if match:
                    count += 1
        
        return count