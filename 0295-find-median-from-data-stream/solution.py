from heapq import *

class MedianFinder:

    def __init__(self):
        self.heaps = None, [], []
        self.i = 1

    def addNum(self, num):
        heappush(self.heaps[-self.i], -heappushpop(self.heaps[self.i], num * self.i))
        self.i *= -1

    def findMedian(self):
        return (self.heaps[self.i][0] * self.i - self.heaps[-1][0]) / 2.0
