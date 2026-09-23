# You are given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

def subarr(nums, k):

    count = 0
    curr_sum = 0
    hashmap = {}

    for num in nums:
        curr_sum += num 
        diff = curr_sum - k 

        if diff in hashmap:
            count += hashmap[diff]

        if curr_sum in hashmap:
            hashmap[curr_sum] += 1
        else:
            hashmap[curr_sum] = 1

    return count