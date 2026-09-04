class Solution:
    def findCheapestPrice(self, n, flights, src, dst, k):
        dist = [float('inf')] * n
        dist[src] = 0

        for _ in range(k + 1):
            cur = dist[:]

            for u, v, price in flights:
                if dist[u] != float('inf'):
                    cur[v] = min(cur[v], dist[u] + price)

            dist = cur

        return -1 if dist[dst] == float('inf') else dist[dst]