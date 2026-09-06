class Solution:
    def numIslands(self, grid):
        n, m = len(grid), len(grid[0])
        ans = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    ans += 1
                    stack = [(i, j)]
                    grid[i][j] = '0'

                    while stack:
                        x, y = stack.pop()
                        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == '1':
                                grid[nx][ny] = '0'
                                stack.append((nx, ny))

        return ans