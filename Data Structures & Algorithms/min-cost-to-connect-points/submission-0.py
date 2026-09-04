class Solution:
    def minCostConnectPoints(self, points):
        n = len(points)
        dist = [float('inf')] * n
        used = [False] * n
        dist[0] = 0
        ans = 0

        for _ in range(n):
            u = -1

            for i in range(n):
                if not used[i] and (u == -1 or dist[i] < dist[u]):
                    u = i

            used[u] = True
            ans += dist[u]

            for v in range(n):
                if not used[v]:
                    d = abs(points[u][0] - points[v][0]) + abs(points[u][1] - points[v][1])
                    dist[v] = min(dist[v], d)

        return ans