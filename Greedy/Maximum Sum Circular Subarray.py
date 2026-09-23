# You are given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning of the array. 
# Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most once. 
# Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.


def circle_sum(nums):

    def kadane_max_sum(nums):
        max_sum = nums[0]
        curr_sum = 0
    
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num 
            max_sum = max(max_sum, curr_sum)
        return max_sum
    
    def kadane_min_sum(nums):
        min_sum = nums[0]
        curr_sum = 0
    
        for num in nums:
            if curr_sum > 0:
                curr_sum = 0
            curr_sum += num 
            min_sum = min(min_sum, curr_sum)
        return min_sum

    total_sum = sum(nums)
    min_subarr = kadane_min_sum(nums)
    max_subarr = kadane_max_sum(nums)
    cir_subarr = total_sum - min_subarr

    if max_subarr > 0:
        return max(max_subarr, cir_subarr)
    else:
        return max_subarr