class Solution:
    def partition(self, s):
        res = []

        def dfs(i, cur):
            if i == len(s):
                res.append(cur[:])
                return

            for j in range(i + 1, len(s) + 1):
                if s[i:j] == s[i:j][::-1]:
                    cur.append(s[i:j])
                    dfs(j, cur)
                    cur.pop()

        dfs(0, [])
        return res