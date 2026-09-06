class Solution:
    def maxAreaOfIsland(self, grid):
        n, m = len(grid), len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    area = 0
                    stack = [(i, j)]
                    grid[i][j] = 0

                    while stack:
                        x, y = stack.pop()
                        area += 1

                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny]:
                                grid[nx][ny] = 0
                                stack.append((nx, ny))

                    ans = max(ans, area)

        return ans