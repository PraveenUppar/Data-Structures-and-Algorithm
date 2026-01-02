class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        # Recustion using dfs
        # nums.sort()

        # def dfs(target):
            
        #     if target == 0:
        #         return 1
                
        #     res = 0
            
        #     for i in range(len(nums)):
        #         if nums[i] > target:
        #             break
        #         res += dfs(target - nums[i])
        #     return res
            

        # return dfs(target)

        # DP
        nums.sort()
        memo = { 0 : 1 }

        def dfs(target):

            if target in memo:
                return memo[target]

            res = 0

            for num in nums:
                if target < num:
                    break
                res += dfs(target - num)
                
            memo[target] = res
            return res
            
        return dfs(target)

        
        