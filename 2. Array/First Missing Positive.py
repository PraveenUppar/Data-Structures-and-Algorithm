class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        nums.sort()
        missing = 1

        for num in nums:
            if num > 0 and missing == num:
                missing += 1
        return missing

        # Brute Force - TLE
        # nums.sort()

        # if 1 not in nums:
        #     return 1

        # for i in range(len(nums)):
        #     if nums[i] > 0 and nums[i]+1 not in nums:
        #         return nums[i] + 1
        