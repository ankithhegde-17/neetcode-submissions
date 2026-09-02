import heapq

class MedianFinder:
    def __init__(self):
        self.l = []
        self.r = []

    def addNum(self, num):
        heapq.heappush(self.l, -num)
        heapq.heappush(self.r, -heapq.heappop(self.l))

        if len(self.r) > len(self.l):
            heapq.heappush(self.l, -heapq.heappop(self.r))

    def findMedian(self):
        if len(self.l) > len(self.r):
            return float(-self.l[0])
        return (-self.l[0] + self.r[0]) / 2