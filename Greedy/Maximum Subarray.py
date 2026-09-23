# Given an array of integers nums, find the subarray with the largest sum and return the sum.

# A subarray is a contiguous non-empty sequence of elements within an array.

def kadane(nums):
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num 
        max_sum = max(max_sum, curr_sum)
    return max_sum