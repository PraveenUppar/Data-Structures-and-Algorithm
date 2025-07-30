from typing import List
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:

        diff = 0
        max_diff = 0 

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] < nums[j]:
                    diff = nums[j] - nums[i]
                    max_diff = max(diff,max_diff)

        if max_diff == 0:
            return -1
            
        max_diff = max(diff,max_diff)
        return max_diff

        