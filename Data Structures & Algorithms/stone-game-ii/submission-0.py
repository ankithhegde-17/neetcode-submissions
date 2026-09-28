from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffix = [0] * n
        suffix[-1] = piles[-1]

        for i in range(n - 2, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        dp = [[None] * (n + 1) for _ in range(n)]

        def dfs(i, M):
            if i == n:
                return 0

            if 2 * M >= n - i:
                return suffix[i]

            if dp[i][M] is not None:
                return dp[i][M]

            res = 0

            for X in range(1, 2 * M + 1):
                current = suffix[i] - dfs(
                    i + X,
                    max(M, X)
                )

                res = max(res, current)

            dp[i][M] = res
            return res

        return dfs(0, 1)