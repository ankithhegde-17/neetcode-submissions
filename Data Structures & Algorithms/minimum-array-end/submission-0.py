class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n -= 1
        b = 1
        while n:
            if not x & b:
                x |= (n & 1) * b
                n >>= 1
            b <<= 1
        return x