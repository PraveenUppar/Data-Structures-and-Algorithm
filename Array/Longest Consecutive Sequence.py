# Given an array of integers nums, return the length of the longest consecutive sequence of elements that can be formed.

# A consecutive sequence is a sequence of elements in which each element is exactly 1 greater than the previous element.
# The elements do not have to be consecutive in the original array.

# You must write an algorithm that runs in O(n) time.

def longest(nums):

    nums = sorted(set(nums))
    longest_streak = 1
    curr_streak = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            curr_streak += 1
            longest_streak = max(longest_streak, curr_streak)
        else:
            curr_streak = 1

    return longest_streak