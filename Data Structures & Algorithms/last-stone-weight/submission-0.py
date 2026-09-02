import heapq

class Solution:
    def lastStoneWeight(self, stones):
        h = [-x for x in stones]
        heapq.heapify(h)

        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x != y:
                heapq.heappush(h, -(x - y))

        return -h[0] if h else 0