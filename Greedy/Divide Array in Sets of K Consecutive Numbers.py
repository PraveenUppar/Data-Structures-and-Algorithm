# Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

# Return true if it is possible. Otherwise, return false.

from collections import Counter

def divide(nums, k):

    if len(nums) % k != 0:
        return False 

    count = Counter(nums)
    nums.sort()

    for num in nums:
        if count[num]:
            for i in range(num, num + k):
                if not count[i]:
                    return      False
                count[i] -= 1

    return True