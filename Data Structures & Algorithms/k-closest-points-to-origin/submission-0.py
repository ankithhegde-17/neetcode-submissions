import heapq

class Solution:
    def kClosest(self, points, k):
        h = []
        for x, y in points:
            d = x * x + y * y
            heapq.heappush(h, (-d, x, y))
            if len(h) > k:
                heapq.heappop(h)
        return [[x, y] for _, x, y in h]