"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        import heapq

        intervals.sort(key=lambda x: x.start)
        h = []

        for x in intervals:
            if h and h[0] <= x.start:
                heapq.heappop(h)
            heapq.heappush(h, x.end)

        return len(h)