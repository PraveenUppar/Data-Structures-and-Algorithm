from collections import Counter
from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        count = Counter(nums)

        for key in count:
            if count[key] > 1:
                return key

        # Brute Force - TLE

        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i] == nums[j]:
        #             return nums[i]
        