# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
# find the minimum number of rooms required to schedule all meetings without any conflicts.

import heapq

def meetings(intervals):

    intervals.sort()
    min_heap = []

    for i in intervals:
        if min_heap and min_heap[0] <= i.start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, i.end)
    return len(min_heap)