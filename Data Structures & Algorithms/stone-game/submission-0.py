from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        @lru_cache(None)
        def dfs(l, r):
            if l == r:
                return piles[l]

            left = piles[l] - dfs(l + 1, r)
            right = piles[r] - dfs(l, r - 1)

            return max(left, right)

        return dfs(0, len(piles) - 1) > 0