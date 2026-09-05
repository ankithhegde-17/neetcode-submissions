class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def dfs(start, cur, total):
            if total == target:
                res.append(cur[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break
                cur.append(candidates[i])
                dfs(i + 1, cur, total + candidates[i])
                cur.pop()

        dfs(0, [], 0)
        return res