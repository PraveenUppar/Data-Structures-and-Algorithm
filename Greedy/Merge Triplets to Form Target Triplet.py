# You are given a 2D array of integers triplets, where triplets[i] = [ai, bi, ci] represents the ith triplet. 
# You are also given an array of integers target = [x, y, z] which is the triplet we want to obtain.

# To obtain target, you may apply the following operation on triplets zero or more times:

# Choose two different triplets triplets[i] and triplets[j] and update triplets[j] to become [max(ai, aj), max(bi, bj), max(ci, cj)].
# * E.g. if triplets[i] = [1, 3, 1] and triplets[j] = [2, 1, 2], triplets[j] will be updated to [max(1, 2), max(3, 1), max(1, 2)] = [2, 3, 2].

# Return true if it is possible to obtain target as an element of triplets, or false otherwise.


def merge(triplets, target):
    t1 = False
    t2 = False
    t3 = False

    for t in triplets:
        if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
            continue

        if t[0] == target[0]:
            t1 = True

        if t[1] == target[1]:
            t2 = True

        if t[2] == target[2]:
            t3 = True

    return t1 and t2 and t3