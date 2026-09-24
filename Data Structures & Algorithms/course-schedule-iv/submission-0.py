class Solution:
    def checkIfPrerequisite(self, n, prerequisites, queries):
        reach = [[False] * n for _ in range(n)]

        for a, b in prerequisites:
            reach[a][b] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reach[i][j] |= reach[i][k] and reach[k][j]

        return [reach[a][b] for a, b in queries]