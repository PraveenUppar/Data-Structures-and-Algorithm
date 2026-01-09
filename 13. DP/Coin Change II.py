class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Recursion using dfs
        # coins.sort()
        # def dfs(i, target):

        #     if i >= len(coins):
        #         return 0
            
        #     if target == 0:
        #         return 1
            
        #     res = 0
            
        #     if target >= coins[i]:
        #         res = dfs(i + 1, target)
        #         res += dfs(i, target - coins[i])
        #     return res

        # return dfs(0, amount)

        # Top Down DP
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]

        def dfs(i, target):

            if i >= len(coins):
                return 0
            if target == 0:
                return 1
            if memo[i][target] != -1:
                return memo[i][target]
            
            res = 0
            if target >= coins[i]:
                res = dfs(i + 1, target)
                res += dfs(i, target - coins[i])
            memo[i][target] = res
            return res

        return dfs(0, amount)