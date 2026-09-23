# You are given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. 
# The result should also be sorted in ascending order.

# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b

def closest(arr, k, x):

    left = 0
    right = len(arr) - 1

    while right - left >= k:
        if abs(arr[right] - x) >= abs(arr[left - x]):
            right -= 1
        else:
            left += 1
    return arr[left: right + 1]