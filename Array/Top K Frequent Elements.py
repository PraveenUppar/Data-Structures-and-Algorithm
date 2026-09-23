# Given an integer array nums and an integer k, return the k most frequent elements within the array.

# The test cases are generated such that the answer is always unique.

# You may return the output in any order.

from collections import Counter

def top(nums, k):

    hashmap = Counter(nums)
    freq_bucket = []

    for _ in range(len(nums) + 1):
        freq_bucket.append([])

    for num, freq in hashmap.items():
        freq_bucket[freq].append(num)

    ans = []

    for i in range(len(freq_bucket) - 1, 0, -1):
        for num in freq_bucket[i]:
            ans.append(num)
            if len(ans) == k:
                return ans 

    return ans