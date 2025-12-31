class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Recursion using dfs
        # def dfs(amount):

        #     if amount == 0:
        #         return 0
            
        #     res = float("inf")

        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     return res

        # min_coin = dfs(amount)

        # if min_coin >= float("inf"):
        #     return -1
        # else:
        #     return min_coin

        # DP using memo

        memo = {}

        def dfs(amount):

            if amount == 0:
                return 0

            if amount in memo:
                return memo[amount]

            res = float("inf")
            
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))

            memo[amount] = res
            return res

        minCoins = dfs(amount)
        if minCoins >= float("inf"):
            return -1
        else:
            return minCoins
