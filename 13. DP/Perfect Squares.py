class Solution:
    def numSquares(self, n: int) -> int:

        # Recursion using dfs
        # def dfs(target):

        #     if target == 0:
        #         return 0

        #     res = target
        #     for i in range(1,target):
        #         if i * i > target:
        #             break
        #         res = min(res, 1 + dfs(target - i * i))

        #     return res

        # return dfs(n)

        # DP with memo

        memo = {}

        def dfs(target):

            if target == 0:
                return 0

            if target in memo:
                return memo[target]

            res = target
            for i in range(1,target):
                if i * i > target:
                    break
                res = min(res, 1 + dfs(target - i * i))
            memo[target] = res
            return res

        return dfs(n)
        