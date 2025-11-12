class MedianFinder:

    def __init__(self):
        # create a empty arr
        self.data = []

    def addNum(self, num: int) -> None:
        # add the num to the arr
        self.data.append(num)

    def findMedian(self) -> float:
        # sort the arr
        self.data.sort()
        # find the median
        n = len(self.data)
        if n % 2 != 0:
            return self.data[n // 2]
        else:
            return (self.data[n // 2] + self.data[n // 2 - 1]) / 2
