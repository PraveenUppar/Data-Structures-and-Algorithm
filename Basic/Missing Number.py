# Given an array nums containing n integers in the range [0, n] without any duplicates, 
# return the single number in the range that is missing from nums.

def missingNumber(nums):
    num_set = set(nums)
    n = len(nums)
    for i in range(n + 1):
        if i not in num_set:
            return i