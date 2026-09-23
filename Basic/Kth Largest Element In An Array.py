# Given an unsorted array of integers nums and an integer k, return the kth largest element in the array.

# By kth largest element, we mean the kth largest element in the sorted order, not the kth distinct element.

# Follow-up: Can you solve it without sorting?


def kthlargest(nums, k):
    nums.sort()
    return nums[len(nums) - k]