class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        row = len(grid)
        cols = len(grid[0])
        res = 0 

        for i in range(row):
            for j in range(cols):
                if grid[i][j] == 1:
                    res += (i + 1 >= row or grid[i + 1][j] == 0)
                    res += (j + 1 >= cols or grid[i][j + 1] == 0)
                    res += (i - 1 < 0 or grid[i - 1][j] == 0)
                    res += (j - 1 < 0 or grid[i][j - 1] == 0)
        return res
        