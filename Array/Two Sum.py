# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

def twosum(nums, target):
    
    dict = {}  

    for i, n in enumerate(nums):
        diff = target - n
        if diff in dict:
            return [dict[diff], i]
        dict[n] = i