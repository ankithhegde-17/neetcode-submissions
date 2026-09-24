class Solution:
    def calcEquation(self, equations, values, queries):
        g = {}
        for (a, b), v in zip(equations, values):
            g.setdefault(a, []).append((b, v))
            g.setdefault(b, []).append((a, 1 / v))

        def dfs(a, b, seen):
            if a not in g:
                return -1.0
            if a == b:
                return 1.0
            seen.add(a)
            for x, v in g[a]:
                if x not in seen:
                    r = dfs(x, b, seen)
                    if r != -1:
                        return v * r
            return -1.0

        return [dfs(a, b, set()) for a, b in queries]