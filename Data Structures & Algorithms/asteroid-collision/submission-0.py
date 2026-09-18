class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        s = []
        for a in asteroids:
            while s and a < 0 < s[-1]:
                if s[-1] < -a:
                    s.pop()
                    continue
                elif s[-1] == -a:
                    s.pop()
                break
            else:
                s.append(a)
        return s