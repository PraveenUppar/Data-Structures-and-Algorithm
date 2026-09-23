# You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array 
# such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

def duplicate(nums, k):
    hashmap = {}

    for right in range(len(nums)):
        num = nums[right]
        if num in hashmap:
            left = hashmap[num]
            if abs(left - right) <= k:
                return True
        hashmap[num] = right
    return False