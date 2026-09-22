import itertools

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return [list(comb) for comb in itertools.combinations(range(1, n + 1), k)]