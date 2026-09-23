# You are given an array of non-negative integers height which represent an elevation map. 
# Each value height[i] represents the height of a bar, which has a width of 1.

# Return the total amount of water that can be trapped between the bars.

def trap(nums):

    max_left = [0] * len(nums)
    max_left = nums[0]

    max_right = [0] * len(nums)
    max_right[len(nums) - 1] = nums[len(nums) - 1]

    total = 0

    for i in range(1, len(nums)):
        max_left[i] = max(max_left[i - 1], nums[i])

    for i in range(len(nums) - 2, -1, -1):
        max_right[i] = max(max_right[i + 1], nums[i])

    for i in range(len(nums)):
        total += min(max_left[i], max_right[i]) - nums[i]

    return total

