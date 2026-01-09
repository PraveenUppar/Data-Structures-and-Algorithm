class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        # Recursion using dfs
        # def dfs(i, target):

        #     if i >= len(coins) or target < 0:
        #         return 0
            
        #     if target == 0:
        #         return 1
            
        #     res = dfs(i + 1, target)
            
        #     if target >= coins[i]:
        #         res += dfs(i, target - coins[i])
        #     return res

        # return dfs(0, amount)

        # Top Down DP
        memo = {} 

        def dfs(i, target):
            if target == 0:
                return 1
            if i == len(coins) or target < 0:
                return 0
            
            if (i, target) in memo:
                return memo[(i, target)]
            
            res = dfs(i + 1, target)
            
            if target >= coins[i]:
                res += dfs(i, target - coins[i])
            
            memo[(i, target)] = res
            return res

        return dfs(0, amount)