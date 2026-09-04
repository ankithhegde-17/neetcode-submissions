import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        graph = [[] for _ in range(n + 1)]

        for u, v, t in times:
            graph[u].append((v, t))

        dist = [float('inf')] * (n + 1)
        dist[k] = 0
        heap = [(0, k)]

        while heap:
            d, u = heapq.heappop(heap)

            if d != dist[u]:
                continue

            for v, t in graph[u]:
                nd = d + t

                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(heap, (nd, v))

        ans = max(dist[1:])

        return -1 if ans == float('inf') else ans