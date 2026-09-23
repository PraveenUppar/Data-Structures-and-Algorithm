# You are given an array nums, that might contain duplicates , return all possible unique permutations in any order.

import itertools

def permutaions(nums):

    arr = set(itertools.permutations(nums))

    res = []

    for permutaion in arr:
        res.append(list(permutaion))
    return res

print(permutaions([1,1,2]))