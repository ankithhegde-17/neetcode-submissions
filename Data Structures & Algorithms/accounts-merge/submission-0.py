class Solution:
    def accountsMerge(self, accounts):
        parent = {}
        owner = {}

        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            parent[find(a)] = find(b)

        for acc in accounts:
            for e in acc[1:]:
                owner[e] = acc[0]
                union(acc[1], e)

        groups = {}
        for e in parent:
            groups.setdefault(find(e), []).append(e)

        return [[owner[r]] + sorted(es) for r, es in groups.items()]