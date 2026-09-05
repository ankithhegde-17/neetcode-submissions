class Solution:
    def generateParenthesis(self, n):
        res = []

        def dfs(s, op, cl):
            if len(s) == 2 * n:
                res.append(s)
                return
            if op < n:
                dfs(s + "(", op + 1, cl)
            if cl < op:
                dfs(s + ")", op, cl + 1)

        dfs("", 0, 0)
        return res