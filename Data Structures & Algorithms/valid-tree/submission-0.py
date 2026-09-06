class Solution:
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False

        p = list(range(n))

        def find(x):
            while x != p[x]:
                p[x] = p[p[x]]
                x = p[x]
            return x

        for a, b in edges:
            a, b = find(a), find(b)
            if a == b:
                return False
            p[a] = b

        return True