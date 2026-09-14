class Solution:
    def reverse(self, x: int) -> int:
        s = -1 if x < 0 else 1
        x *= s
        res = 0
        while x:
            res = res * 10 + x % 10
            x //= 10
        res *= s
        return res if -2**31 <= res <= 2**31 - 1 else 0