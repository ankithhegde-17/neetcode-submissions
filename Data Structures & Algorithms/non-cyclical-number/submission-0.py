class Solution:
    def isHappy(self, n: int) -> bool:
        f = lambda x: sum(int(d) ** 2 for d in str(x))
        slow, fast = n, f(n)
        while fast != 1 and slow != fast:
            slow, fast = f(slow), f(f(fast))
        return fast == 1