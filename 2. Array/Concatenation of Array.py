from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        ans = []

        # Method 1
        # Do something n times which in this case is 2

        for i in range(2):
            for num in nums:
                ans.append(num)

        # Method 2
        # Use 2 loop

        # for i in range(len(nums)):
        #     ans.append(nums[i])
        # for i in range(len(nums)):
        #     ans.append(nums[i])
        return ans

print(Solution().getConcatenation(nums = [1,3,2,1]))