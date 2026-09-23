# Given an array nums of unique integers, return all the possible permutations. You may return the answer in any order.

import itertools

def permutaions(nums):

    arr = list(itertools.permutations(nums))

    res = []

    for permutaion in arr:
        res.append(list(permutaion))
    return res

print(permutaions([1,2,3]))