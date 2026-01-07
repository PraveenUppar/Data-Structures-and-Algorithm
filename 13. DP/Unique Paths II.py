class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        row = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[row - 1][cols - 1] == 1:
            return 0

        dp = [[0] * (cols + 1) for _ in range(row + 1)]
        dp[row - 1][cols - 1] = 1

        for i in range(row - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] += dp[i+1][j]
                    dp[i][j] += dp[i][j+1]
        return dp[0][0]