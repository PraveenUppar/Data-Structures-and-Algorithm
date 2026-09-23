# You are given an integer array heights where heights[i] represents the height of the ith bar.

# You may choose any two bars to form a container. Return the maximum amount of water a container can store.


def area(heights):
    l = 0
    r = len(heights) - 1
    res = 0

    while l < r:
        area = min(heights[l], heights[r]) * (r - l)
        res = max(res, area)
        if heights[l] <= heights[r]:
            l += 1
        else:
            r -= 1
    return res