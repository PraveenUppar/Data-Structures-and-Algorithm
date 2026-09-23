# Given an integer array nums, find a subarray that has the largest product, and return the product.

# A subarray is a contiguous non-empty sequence of elements within an array.

# You can assume the output will fit into a 32-bit integer.

# Note that the product of an array with a single element is the value of that element.


def max_product(nums):
    curr_max = nums[0]
    curr_min = nums[0]
    res = nums[0]


    for i in range(1, len(nums)):
        option1 = nums[i]
        option2 = nums[i] * curr_min
        option3 = nums[i] * curr_max

        curr_max = max(option1, option2, option3)
        curr_min = min(option1, option2, option3)

        res = max(res, curr_max)

    return res