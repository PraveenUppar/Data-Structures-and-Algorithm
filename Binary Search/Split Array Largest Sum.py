# You are given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest sum of any subarray is minimized.

# Return the minimized largest sum of the split.

# A subarray is a contiguous part of the array.

def split(nums, k):
    left = max(nums)
    right = sum(nums)
    arr_sum = right

    while left <= right:
        mid = (right + left) // 2
        curr_sum = 0
        curr_k = 1

        for i in nums:
            if curr_sum + i > mid:
                curr_k += 1
                curr_sum = i 
            else:
                curr_sum += i

        if curr_sum <= k:
            arr_sum = mid
            right = mid - 1
        else:
            left = mid + 1 
    return arr_sum