# You are given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead.

# A subarray is a contiguous non-empty sequence of elements within an array.


def minSubarray(nums, target):
    left = 0
    curr_sum = 0
    min_len = float("inf")

    for right in range(len(nums)):
        curr_sum += nums[right]
        while curr_sum >= target:
            min_len = min(min_len, right - left + 1)
            curr_sum -= nums[left]
            left += 1

    if min_len == float("inf"):
        return 0
    else:
        return min_len