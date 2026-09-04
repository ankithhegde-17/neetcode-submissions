from collections import defaultdict

class Solution:
    def findItinerary(self, tickets):
        graph = defaultdict(list)

        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)

        ans = []

        def dfs(u):
            while graph[u]:
                dfs(graph[u].pop())
            ans.append(u)

        dfs("JFK")
        return ans[::-1]