# Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), 
# determine if a person could add all meetings to their schedule without any conflicts. 
# The intervals may be provided in any order.

def meeting(intervals):
    intervals.sort()

    for i in range(1, len(intervals)):
        i1 = intervals[i - 1]
        i2 = intervals[i]

        if i1.end > i2.start:
            return False 

    return True