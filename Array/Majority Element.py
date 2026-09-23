# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times in the array. 
# You may assume that the majority element always exists in the array.

def major(nums):
    nums.sort()
    return nums[len(nums) // 2]