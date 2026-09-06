class Solution:
    def pacificAtlantic(self, heights):
        m, n = len(heights), len(heights[0])

        def dfs(starts):
            seen = set(starts)
            stack = starts[:]

            while stack:
                r, c = stack.pop()
                for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                        seen.add((nr, nc))
                        stack.append((nr, nc))

            return seen

        p = [(i, 0) for i in range(m)] + [(0, j) for j in range(n)]
        a = [(i, n - 1) for i in range(m)] + [(m - 1, j) for j in range(n)]

        pacific = dfs(p)
        atlantic = dfs(a)

        return [[r, c] for r, c in pacific & atlantic]