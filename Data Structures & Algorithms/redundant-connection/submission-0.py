class Solution:
    def findRedundantConnection(self, edges):
        p = list(range(len(edges) + 1))

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        for a, b in edges:
            x, y = find(a), find(b)
            if x == y:
                return [a, b]
            p[x] = y