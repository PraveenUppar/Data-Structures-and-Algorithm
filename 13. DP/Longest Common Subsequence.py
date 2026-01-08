class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        # Recursion using dfs

        # def dfs(i,j):
        #     if i == len(text1) or j == len(text2):
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i + 1, j + 1)
        #     return max(dfs(i + 1, j), dfs(i, j + 1))
        
        # return dfs(0,0)

        # Top down DP

        # memo = {}

        def dfs(i,j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i,j) in memo:
                return memo[(i,j)]

            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + dfs(i + 1, j + 1)
            else:
                memo[(i,j)] = max(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i,j)]

        return dfs(0,0)

        # Bottom up DP

        # dp = [[0] * (n + 1) for _ in range(m + 1)]

        # for i in range(len(text1) - 1, -1, -1):
        #     for j in range(len(text2) - 1, -1, -1):
        #         if text1[i] == text2[j]:
        #             dp[i][j] = 1 + dp[i + 1][j + 1]
        #         else:
        #             dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        # return dp[0][0]

        