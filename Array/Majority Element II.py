# You are given an integer array nums of size n, find all elements that appear more than ⌊ n/3 ⌋ times. 
# You can return the result in any order.

from collections import Counter

def majority(nums):

    count = Counter(nums)
    res = []

    for key in count:
        if count[key] > len(nums) // 3:
            res.append(key)

    return res