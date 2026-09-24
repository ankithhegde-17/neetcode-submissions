class Solution:
    def openLock(self, deadends, target):
        dead = set(deadends)
        if "0000" in dead:
            return -1

        q = [("0000", 0)]
        seen = {"0000"}

        for s, d in q:
            if s == target:
                return d
            for i in range(4):
                for x in (-1, 1):
                    t = s[:i] + str((int(s[i]) + x) % 10) + s[i+1:]
                    if t not in dead and t not in seen:
                        seen.add(t)
                        q.append((t, d + 1))
        return -1