# You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

# Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

def binarysearch(nums, target):
    left = 0 
    right = len(nums) - 1

    while left <= right:
        mid = (right + left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1