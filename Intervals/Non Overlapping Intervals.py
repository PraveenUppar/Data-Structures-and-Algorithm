# Given an array of intervals intervals where intervals[i] = [start_i, end_i], 
# return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

def nonoverlapping(intervals):

    res = 0
    intervals.sort(key = lambda x:x[1])

    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if prev_end > intervals[i][0]:
            res += 1
        else:
            prev_end = intervals[i][1]
    return res