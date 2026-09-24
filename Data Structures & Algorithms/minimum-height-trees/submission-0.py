class Solution:
    def findMinHeightTrees(self, n, edges):
        if n <= 2:
            return list(range(n))

        g = [set() for _ in range(n)]
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        leaves = [i for i in range(n) if len(g[i]) == 1]

        while n > 2:
            n -= len(leaves)
            new = []
            for leaf in leaves:
                nei = g[leaf].pop()
                g[nei].remove(leaf)
                if len(g[nei]) == 1:
                    new.append(nei)
            leaves = new

        return leaves