class Solution:
    def integerBreak(self, n: int) -> int:

        # recursion using dfs

        # def dfs(num):

        #     if num == 1:
        #         return 1

        #     if num == n:
        #         res = 0
        #     else:
        #         res = num

        #     for k in range(1, num):
        #         val = dfs(k) * dfs(num - k)
        #         res = max(res, val)
        #     return res
            
        # return dfs(n)



        # dp using memo
        memo = {1:1}

        def dfs(num):
            if num in memo:
                return memo[num]

            if num == n:
                memo[num] = 0
            else:
                memo[num] = num
                
            for k in range(1, num):
                val = dfs(k) * dfs(num - k)
                memo[num] = max(memo[num], val)
            return memo[num]
            
        return dfs(n)













        