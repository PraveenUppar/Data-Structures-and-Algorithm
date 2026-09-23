# Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals, 
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

# You may return the answer in any order.

def merge(intervals):

    intervals.sort()
    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res