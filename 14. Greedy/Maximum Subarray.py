class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        # Brute Force
        # res = nums[0]
        # for i in range(len(nums)):
        #     curr_sum = 0
        #     for j in range(i, len(nums)):
        #         curr_sum += nums[j]
        #         res = max(curr_sum, res)
        # return res

        # Kadane Algo
        # Kadane's algorithm is an efficient dynamic programming algorithm used to find the maximum sum of a contiguous subarray

        max_sum = nums[0]
        curr_sum = 0

        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(curr_sum, max_sum)
        return max_sum
