# You are given an array of integers nums containing n + 1 integers. Each integer in nums is in the range [1, n] inclusive.

# There is exactly one repeated integer in nums, and every other integer appears at most once.

# Return the repeated integer.

def duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1