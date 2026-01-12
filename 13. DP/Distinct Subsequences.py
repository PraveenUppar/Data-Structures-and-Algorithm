class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(t) > len(s):
            return 0
        
        dp = {}

        def dfs(i,j):

            if i == len(s) and j != len(t):
                return 0

            if j == len(t):
                return 1
            
            if (i,j) in dp:
                return dp[(i, j)]

            res = dfs(i + 1, j)

            if s[i] == t[j]:
                res += dfs(i + 1, j + 1)
                
            dp[(i, j)] = res
            return dp[(i, j)]

        return dfs(0,0)
        