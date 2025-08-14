class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        min_len = float("inf")
        curr_sum = 0
        left = 0

        for right in range(len(nums)):
            curr_sum += nums[right]
            while curr_sum >= target:
                min_len = min(min_len,right - left + 1)
                curr_sum -= nums[left]
                left += 1
        return 0 if min_len == float("inf") else min_len


        #  Brute Force - TLE
        # if sum(nums) < target:
        #     return 0

        # min_array = float("inf")

        # for i in range(len(nums)):
        #     curr_sum = 0
        #     len_count = 0
        #     for j in range(i,len(nums)):
        #         curr_sum += nums[j]
        #         len_count += 1
        #         if curr_sum >= target:
        #             min_array = min(min_array,len_count)
        # return min_array