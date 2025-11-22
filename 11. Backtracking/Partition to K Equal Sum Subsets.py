class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if sum(nums) % k != 0:
            return False
        
        nums.sort(reverse = True)
        target = sum(nums) // k
        subset = [0] * k

        def dfs(i):

            if i == len(nums):
                return True

            for j in range(k):
                if subset[j] + nums[i] <= target:
                    subset[j] += nums[i]
                    if dfs(i + 1):
                        return True
                    subset[j] -= nums[i] 
                    if subset[j] == 0:
                        break     
            return False

        return dfs(0)
        