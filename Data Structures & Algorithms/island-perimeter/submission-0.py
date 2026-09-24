class Solution:
    def islandPerimeter(self, grid):
        p = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    p += 4
                    if i and grid[i-1][j]:
                        p -= 2
                    if j and grid[i][j-1]:
                        p -= 2
        return p