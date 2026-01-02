class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # Rcursion using dfs
        # if sum(nums) % 2:
        #     return False
        
        # max_res = sum(nums) / 2

        # def dfs(i, target):

        #     if target == 0:
        #         return True

        #     if target < 0 or i >= len(nums):
        #         return False

        #     exclude = dfs(i + 1, target)
        #     include = dfs(i + 1, target - nums[i])

        #     return exclude or include
        
        # return dfs(0, max_res)

        # DP
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)

        dp[0] = True
        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

        # DP using memo
        # total = sum(nums)

        # if total % 2 != 0:
        #     return False

        # target = total / 2

        # n = len(nums)
        # memo = []
        # for _ in range(n + 1):
        #     row = [-1] * (target + 1)
        #     memo.append(row)

        # def dfs(i, target):

        #     if target == 0:
        #         return True

        #     if target < 0 or i >= len(nums):
        #         return False
            
        #     if memo[i][target] != -1:
        #         return memo[i][target]

        #     memo[i][target] = (dfs(i + 1, target) or dfs(i + 1, target - nums[i]))

        #     return memo[i][target]
        
        # return dfs(0,target)
        
