class Solution:
    def countComponents(self, n, edges):
        p = list(range(n))

        def find(x):
            while x != p[x]:
                p[x] = p[p[x]]
                x = p[x]
            return x

        ans = n

        for a, b in edges:
            a, b = find(a), find(b)
            if a != b:
                p[a] = b
                ans -= 1

        return ans