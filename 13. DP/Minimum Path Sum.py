class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        row = len(grid)
        cols = len(grid[0])

        # Reursion using dfs
        # def dfs(i,j):
        #     if i == (row-1) and j == (cols - 1):
        #         return grid[i][j]

        #     if i >= row or j >= cols:
        #         return float("inf")

        #     res = grid[i][j] + min(dfs(i + 1, j) , dfs(i, j + 1))
        #     return res

        # return dfs(0,0)

        # Top down DP
        dp = [[-1] * cols for _ in range(row)]

        def dfs(i,j):
            if i == (row-1) and j == (cols - 1):
                return grid[i][j]

            if i >= row or j >= cols:
                return float("inf")
            
            if dp[i][j] != -1:
                return dp[i][j]

            dp[i][j] = grid[i][j] + min(dfs(i + 1, j) , dfs(i, j + 1))
            return dp[i][j]

        return dfs(0,0)

        # Bottom up DP

        # dp = [[float("inf")] * (cols + 1) for _ in range(row + 1)]
        # dp[row - 1][cols] = 0

        # for i in range(row - 1, -1, -1):
        #     for j in range(cols - 1, -1, -1):
        #         dp[i][j] = grid[i][j] + min(dp[i + 1][j], dp[i][j + 1])
        # return dp[0][0]
        