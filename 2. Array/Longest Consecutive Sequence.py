class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        curr_count = 1
        max_count = 1

        if nums is None:
            return 0

        i = 1

        while i < len(nums):
            if nums[i] == nums[i-1] + 1:
                curr_count += 1
            elif nums[i] != nums[i-1]:
                max_count = max(max_count,curr_count)
                curr_count = 1
            i += 1
        max_count = max(max_count,curr_count)
        return max_count

        
        
        # Did not run all the test cases
        
        # count = 0
        # nums.sort()
        # nums = list(set(nums))

        # if len(nums) <= 1:
        #     return nums

        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[j] == nums[i] + 1:
        #             count += 1
        # return count + 1