from collections import deque

class Solution:
    def foreignDictionary(self, words):
        graph = {c: set() for word in words for c in word}
        indegree = {c: 0 for c in graph}

        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            found = False

            for x, y in zip(a, b):
                if x != y:
                    if y not in graph[x]:
                        graph[x].add(y)
                        indegree[y] += 1
                    found = True
                    break

            if not found and len(a) > len(b):
                return ""

        q = deque(c for c in graph if indegree[c] == 0)
        ans = []

        while q:
            c = q.popleft()
            ans.append(c)

            for nei in graph[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return "".join(ans) if len(ans) == len(graph) else ""