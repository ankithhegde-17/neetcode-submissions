from typing import List
from functools import lru_cache

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dfs(r, c):
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return grid[r][c]

            if r == len(grid) or c == len(grid[0]):
                return float('inf')

            down = dfs(r + 1, c)
            right = dfs(r, c + 1)

            return grid[r][c] + min(down, right)

        return dfs(0, 0)