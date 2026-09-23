# You are given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

def find(nums):
    nums.sort()
    missing = 1
    for num in nums:
        if num > 0 and missing == num:
            missing += 1
    return missing