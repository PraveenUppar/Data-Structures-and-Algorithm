# You are given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

def rotate(nums, k):

    k = k % len(nums)

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    reverse(0, len(nums) - 1)
    reverse(0, k - 1)
    reverse(k, len(nums) - 1)