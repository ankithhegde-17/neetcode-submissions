from collections import deque

class Solution:
    def findOrder(self, numCourses, prerequisites):
        g = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses

        for a, b in prerequisites:
            g[b].append(a)
            indeg[a] += 1

        q = deque(i for i in range(numCourses) if indeg[i] == 0)
        ans = []

        while q:
            u = q.popleft()
            ans.append(u)

            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        return ans if len(ans) == numCourses else []