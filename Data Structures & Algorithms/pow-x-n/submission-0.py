class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x, n = 1 / x, -n
        res, curr = 1.0, x
        while n:
            if n & 1:
                res *= curr
            curr *= curr
            n >>= 1
        return res