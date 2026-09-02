from collections import Counter

class Solution:
    def leastInterval(self, tasks, n):
        c = Counter(tasks)
        m = max(c.values())
        slots = (m - 1) * (n + 1) + sum(v == m for v in c.values())
        return max(len(tasks), slots)