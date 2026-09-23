# You are given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:

# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:

# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.

def turbulance(nums):

    res = 0
    count = 0
    sign = -1

    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            if sign == 0:
                count += 1
            else:
                count = 1
        elif nums[i] < nums[i + 1]:
            if sign == 1:
                count += 1
            else:
                count = 1
            sign = 0
        else:
            sign = -1
            count = 0

        res = max(res, count)
        
    return res
