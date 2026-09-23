# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

def contains(nums):
    nums_Set = set(nums)
    return len(nums) == len(nums_Set)
