# You are given an array of non-overlapping intervals intervals where intervals[i] = [start_i, end_i] represents the start and the end time of the ith interval. 
# intervals is initially sorted in ascending order by start_i.

# You are given another interval newInterval = [start, end].

# Insert newInterval into intervals such that intervals is still sorted in ascending order by start_i and also intervals still does not have any overlapping intervals. 
# You may merge the overlapping intervals if needed.

# Return intervals after adding newInterval.


def insert(intervals, newInterval ):

    intervals.append(newInterval)
    intervals.sort()

    res = [intervals[0]]

    for i in range(1, len(intervals)):
        if res[-1][1] >= intervals[i][0]:
            res[-1][1] = max(res[-1][1], intervals[i][1])
        else:
            res.append(intervals[i])
    return res