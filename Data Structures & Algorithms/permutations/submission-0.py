class Solution:
    def permute(self, nums):
        res = []

        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur[:])
                return

            for x in nums:
                if x not in cur:
                    cur.append(x)
                    dfs(cur)
                    cur.pop()

        dfs([])
        return res