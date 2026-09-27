class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 0, 1, 1  # T0, T1, T2

        for _ in range(n):
            a, b, c = b, c, a + b + c

        return a