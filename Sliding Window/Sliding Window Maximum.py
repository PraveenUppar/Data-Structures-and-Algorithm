# You are given an array of integers nums and an integer k. There is a sliding window of size k that starts at the left edge of the array. 
# The window slides one position to the right until it reaches the right edge of the array.

# Return a list that contains the maximum element in the window at each step.

def window(nums, k):

    res = []

    for i in range(len(nums) - k + 1):
        max_num = nums[i]
        for j in range(i, i + k):
            max_num = max(max_num, nums[j])
        res.append(max_num)
    return res