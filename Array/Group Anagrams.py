# Given an array of strings strs, group all anagrams together into sublists. 
# You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, 
# but the order of the characters can be different.

from collections import defaultdict


def group(strs):
    res = defaultdict(list)
    for s in strs:
        sortedS = ''.join(sorted(s))
        res[sortedS].append(s)
    return list(res.values())

