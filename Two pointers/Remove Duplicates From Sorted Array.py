# You are given an integer array nums sorted in non-decreasing order. 
# Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, 
# denoted as k, such that the first k elements of nums contain the unique elements.

def remove(nums):

    res = set(nums)
    return list(res)